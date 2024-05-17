import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProjectStore = defineStore('project', () => {
  // TopRateCard
  const topRateDeposit = ref(null)
  const topRateSaving = ref(null)
  const getTRDeposit = function () {
    axios({
      method: 'get',
      url:'http://127.0.0.1:8000/products/deposit-products/top_rate/',
    }).then((res) => {
      topRateDeposit.value=res.data
    })
  }
  const getTRSaving = function () {
    axios({
      method: 'get',
      url:'http://127.0.0.1:8000/products/saving-products/top_rate/',
    }).then((res) => {
      topRateSaving.value=res.data
    })}

    //ProductList
    const productListD = ref([])
    const productListDR = ref([])
    const getProductListD= function () {
      axios({
        method: 'get',
        url:'http://127.0.0.1:8000/products/deposit-products/',
      }).then((res) => {
        productListD.value=res.data
        productListDR.value=productListD.value.map((product) => {
          const result={
            productname:product.deposit_product.fin_prdt_nm,
            bankname:product.deposit_product.kor_co_nm,
          }
          product.options.forEach(el => {
            if(el.save_trm%6==0){
              result[el.save_trm]=el.intr_rate
            }
          });
          return result
        })
      })}
    
  return {topRateDeposit, getTRDeposit, topRateSaving, getTRSaving , productListD, getProductListD,productListDR}
})
