import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useProjectStore = defineStore('project', () => {
  // TopRateCard
  const topRateDeposit = ref([])
  const getTRDeposit = function () {
    axios({
      method: 'get',
      url:'http://127.0.0.1:8000/products/deposit-products/top_rate/',
    }).then((res) => {
      console.log(res.data);
    })
  }
  return {topRateDeposit, getTRDeposit}
})
