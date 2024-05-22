<template>
    <div class="exchange-container">
      <h1 class="text-start title">환율 계산기</h1>
      <div class="d-flex flex-row justify-content-center align-items-center text-center">
        <div class="tabs">
          <button @click="setMode('send')" :class="{ active: mode === 'send' }">송금 보낼 때</button>
          <button @click="setMode('receive')" :class="{ active: mode === 'receive' }">송금 받을 때</button>
        </div>
        <button class="btn btn-primary exchange text-center mb-3" @click="goExchange">전환</button>
      </div>
      <div class="exchange-rate-box">
        <div class="currency-row">
          <img v-if="toFlag" :src="toFlag" alt="" width="30px" height="20px">
          <select v-model="toRate" class="form-select">
            <option value="없음" selected>국가선택</option>
            <option v-for="currency in store.exchangeRate" :key="currency.cur_unit" :value="currency.cur_unit">
              {{ currency.country }}
            </option>
          </select>
          <input type="number" v-model.number="toCurrency" class="form-control" />
          <span>{{toUnit}}</span>
        </div>
        <button @click="swapCurrencies" class="swap-button">⇄</button>
        <div class="currency-row">
          <img v-if="fromFlag" :src="fromFlag" alt=" " width="30px" height="20px">
          <select v-model="fromRate" class="form-select">
            <option value="없음" selected>국가선택</option>
            <option v-for="currency in store.exchangeRate" :key="currency.cur_unit" :value="currency.cur_unit">
              {{ currency.country }}
            </option>
          </select>
          <span>{{fromCurrency}} {{fromUnit}}</span>
        </div>
      </div>
      <div>
        <div>
          <img src="@/assets/erg/USD.png" width="400" class="graph-image" />
          <img src="@/assets/erg/JPY.png" width="400" class="graph-image" />
        </div>
        <div>
          <img src="@/assets/erg/EUR.png" width="400" class="graph-image" />
          <img src="@/assets/erg/CNY.png" width="400" class="graph-image" />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { onMounted, ref, watch } from 'vue';
  import { useProjectStore } from '@/stores/project';
  
  const store = useProjectStore();
  const mode = ref('send'); // 'send' or 'receive'
  
  const toRate = ref("없음");
  const fromRate = ref("없음");
  const toCurrency = ref(0);
  const fromCurrency = ref(0);
  const toUnit = ref("단위");
  const fromUnit = ref("단위");
  const toFlag=ref('');
  const fromFlag=ref('');
  
  watch([toRate, fromRate], () => {
    if (toRate.value === "없음") {
      toUnit.value = "단위";
      toFlag.value='';
    } else {
        store.exchangeRate.forEach(el => {
          if (el.cur_unit === toRate.value) {
            toUnit.value = el.cur_nm;
            toFlag.value=el.flag;
          }
        });
    }
    if (fromRate.value === "없음") {
      fromUnit.value = "단위";
      fromFlag.value='';
    } else {
        store.exchangeRate.forEach(el => {
          if (el.cur_unit === fromRate.value) {
            fromUnit.value = el.cur_nm;
            fromFlag.value=el.flag;
          }
        });
    }
  });
  
  const setMode = (newMode) => {
    mode.value = newMode;
    goExchange();
  };
  
  const swapCurrencies = () => {
    const temp = toRate.value;
    toRate.value = fromRate.value;
    fromRate.value = temp;
    if(toCurrency.value==0 &&  fromCurrency.value==0){
    }
    else{
      goExchange()
    }
  };

  const goExchange=function(){
    if(toRate.value==='없음'){
      alert('환전할 국가를 선택해주세요');
      return;
    }
    else if(fromRate.value==='없음'){
      alert('환전할 국가를 선택해주세요');
      return;
    }
    
    if(toCurrency.value==0){
        console.log(parseFloat("123.12"));
      alert('환전할 금액을 입력해주세요');
      return;
    }
    else{
        if(mode.value==='send'){
            let startRate=store.exchangeRate.find(el=>el.cur_unit===toRate.value).tts;
            let endRate=store.exchangeRate.find(el=>el.cur_unit===fromRate.value).tts;
            if(startRate==0){
                startRate=1;
            }
            if(endRate==0){
                endRate=1;
            }
            fromCurrency.value=(toCurrency.value*startRate/endRate).toFixed(2);
        }
        else{
            let startRate=store.exchangeRate.find(el=>el.cur_unit===toRate.value).ttb;
            let endRate=store.exchangeRate.find(el=>el.cur_unit===fromRate.value).ttb;
            if(startRate==0){
                startRate=1;
            }
            if(endRate==0){
                endRate=1;
            }
            fromCurrency.value=(toCurrency.value*startRate/endRate).toFixed(2);
        }
    }
    }
    onMounted(()=>{
        store.getExchangeRate();
    });
  </script>
  
  <style scoped>
  .exchange-container {
    max-width: 980px;
    margin: auto;
    padding: 20px;
    text-align: center;
    height: 1200px;
  }
  
  h1 {
    margin-bottom: 20px;
  }
  
  .tabs {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
  }
  
  .tabs button {
    background: none;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    font-size: 1rem;
    color: #333;
  }
  
  .tabs button.active {
    font-weight: bold;
    color: #007bff;
  }
  
  .exchange-rate-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
  }
  
  .currency-row {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  
  .flag {
    width: 40px;
    height: 30px;
  }
  
  .form-select,
  .form-control {
    width: 200px;
  }
  
  .equals {
    font-size: 2rem;
  }
  
  .swap-button {
    background: none;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    color: #007bff;
    margin: 10px 0;
  }
  
  .exchange {
    height: 30px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .title{
    font-size: 2rem;
    font-weight: 600;
    width: 950px;
  }
  .graph-image {
    border-radius: 5px;
    border:1px solid #e9ecef;
    margin: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  .graph-image:hover {
    transform: scale(1.05);
    transition: transform 0.5s;
  }
  </style>
  