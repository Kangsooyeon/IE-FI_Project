<!-- TopRates.vue -->
<template>
    <div class="TR-container card">
      <p class="TR-title ms-4 mt-4 mb-0">최고 이율 Top5 상품</p>
      <ul class="TR-selector d-flex justify-content-end my-2 mb-0 me-2">
        <li class="me-2 under-line" @click="toggleDP" :class="{ 'item-selector': !toogleOption }">예금</li>
        <li class="under-line" @click="toggleSV" :class="{ 'item-selector': toogleOption }">적금</li>
      </ul>
      <div v-if="store.topRateDeposit != null && !toogleOption" class="ms-3 TR-list">
        <p
          v-for="(productD, idx) in store.topRateDeposit"
          :key="productD.deposit_product.fin_prdt_nm"
          class="TR-item"
          @click="goDetail(productD.deposit_product.fin_prdt_cd)"
        >
          {{ idx + 1 }}. {{ productD.deposit_product.fin_prdt_nm }} +{{ productD.option.intr_rate2 }}%
        </p>
      </div>
  
      <div v-if="store.topRateSaving != null && toogleOption" class="ms-3 TR-list">
        <p
          v-for="(productS, idx) in store.topRateSaving"
          :key="productS.saving_product.fin_prdt_nm"
          class="TR-item"
          @click="goDetail(productS.saving_product.fin_prdt_cd)"
        >
          {{ idx + 1 }}. {{ productS.saving_product.fin_prdt_nm }} +{{ productS.option.intr_rate2 }}%
        </p>
      </div>
      <div>
        <p class="m-0 text-end me-2 under-line" @click="goProduct">전체 상품</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useProjectStore } from '@/stores/project';
  import { useRouter } from 'vue-router';
  import axios from 'axios';
  
  const store = useProjectStore();
  const toogleOption = ref(false);
  const router = useRouter();
  
  const goProduct = () => {
    router.push('/productlist');
  };
  const toggleDP = () => {
    toogleOption.value = false;
  };
  
  const toggleSV = () => {
    toogleOption.value = true;
  };
  
  const goDetail = function (fin_cd) {
    router.push({ name: 'productdetail', params: { fin_prdt_cd: fin_cd } });
  };
  
  onMounted(() => {
    store.getTRDeposit();
    store.getTRSaving();
  });
  </script>
  
  <style scoped>
  .TR-title {
    font-size: 1.5rem;
    font-weight: 700;
    border-bottom: 2px solid #e9ecef;
    color: #333;
  }
  
  .TR-container {
    border: 1px solid #e9ecef;
    border-radius: 8px;
    width: 400px;
    height: 400px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    overflow-y: auto;
    padding: 10px;
  }
  
  .TR-item {
    font-size: 1.1rem;
    font-weight: 600;
    margin: 8px 0;
    transition: color 0.3s, background-color 0.3s;
  }
  
  .TR-item:hover {
    cursor: pointer;
    color: #0d6efd;
    background-color: #f8f9fa;
  }
  
  .TR-selector {
    font-size: 1rem;
    font-weight: 700;
    list-style-type: none;
    padding-left: 0;
  }
  
  .under-line:hover {
    text-decoration: underline;
    cursor: pointer;
  }
  
  .item-selector {
    text-decoration: underline;
    color: #0d6efd;
  }
  
  .text-end {
    text-align: right;
  }
  
  .text-end .under-line {
    font-size: 1rem;
  }
  </style>
  