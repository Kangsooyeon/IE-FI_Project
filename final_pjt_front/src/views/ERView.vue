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
        <div class="d-flex flex-row justify-content-center align-items-center">
          <p v-if="!isprdt" class="m-0 text-primary fw-semibold">머신런닝을 사용한 5일 후 환율 예측 그래프 보기</p>
          <p v-else class="m-0 text-danger fw-semibold">예측한 환율에 대한 어떤 법적 책임도 지지 않습니다.</p>
          <label class="toggle_switch ms-5 mb-3">
              <input type="checkbox" @click="console.log(isprdt)" v-model="isprdt">
              <span class="slider"></span>
          </label>
        </div>
        <div v-if="!isprdt">
          <img src="@/assets/erg/USD.png" width="400" class="graph-image" />
          <img src="@/assets/erg/JPY.png" width="400" class="graph-image" />
        </div>
        <div v-else>
          <img src="@/assets/erg/USDpredict.png" width="400" class="graph-image" />
          <img src="@/assets/erg/JPYpredict.png" width="400" class="graph-image" />
        </div>
        <div v-if="!isprdt">
          <img src="@/assets/erg/EUR.png" width="400" class="graph-image" />
          <img src="@/assets/erg/CNY.png" width="400" class="graph-image" />
        </div>
        <div v-else>
          <img src="@/assets/erg/EURpredict.png" width="400" class="graph-image" />
          <img src="@/assets/erg/CNYpredict.png" width="400" class="graph-image" />
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
  
  const isprdt=ref(false);

  watch([toRate, fromRate], () => {
    if (toRate.value === "없음") {
      toUnit.value = "단위";
      toFlag.value='';
    } else {
        store.exchangeRate.forEach(el => {
          if (el.cur_unit === toRate.value) {
            toUnit.value = el.cur_nm.split(' ').length==1? el.cur_nm:el.cur_nm.split(' ')[1];
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
            fromUnit.value = el.cur_nm.split(' ').length==1? el.cur_nm:el.cur_nm.split(' ')[1];
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
    border-radius: 5px;
    border:1px solid #e9ecef;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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
  .toggle_switch { display: inline-block; position: relative; width: 70px; height: 34px; margin-top: 20px;} 
.toggle_switch input[type="checkbox"] { overflow: hidden; position: absolute; width: 1px; height: 1px; margin: -1px; font-size: initial; clip: rect(0 0 0 0); } 
.toggle_switch .slider { position: absolute; top: 0; right: 0; bottom: 0; left: 0; background-color: #ccc; border-radius: 34px; cursor: pointer; transition: 0.4s; } 
.toggle_switch input[type="checkbox"]:checked + .slider { background-color: #007bff; } 
.toggle_switch .slider::before { content: ""; position: absolute; top: 4px; left: 4px; width: 26px; height: 26px; background-color: #fff; border-radius: 50%; transition: 0.4s; } 
.toggle_switch input[type="checkbox"]:checked + .slider::before { transform:translateX(36px); } 
  </style>
  