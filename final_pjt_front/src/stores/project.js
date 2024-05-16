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
  return {topRateDeposit, getTRDeposit, topRateSaving, getTRSaving}
})
