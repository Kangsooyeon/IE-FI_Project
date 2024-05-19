import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';

export const useProjectStore = defineStore('project', () => {
  // 은행
  const banks = [
    '우리은행',
    '한국스탠다드차타드은행',
    '대구은행',
    '부산은행',
    '광주은행',
    '제주은행',
    '전북은행',
    '경남은행',
    '중소기업은행',
    '한국산업은행',
    '국민은행',
    '신한은행',
    '농협은행주식회사',
    '하나은행',
    '주식회사 케이뱅크',
    '수협은행',
    '주식회사 카카오뱅크',
    '토스뱅크 주식회사',
  ];
  // TopRateCard
  const topRateDeposit = ref(null);
  const topRateSaving = ref(null);
  const getTRDeposit = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/products/deposit-products/top_rate/',
    }).then((res) => {
      topRateDeposit.value = res.data;
    });
  };
  const getTRSaving = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/products/saving-products/top_rate/',
    }).then((res) => {
      topRateSaving.value = res.data;
    });
  };

  //ProductList
  // 예금상품
  const productListD = ref([]);
  const productListDR = ref([]);
  const productListDRC = ref([]);
  const productListDRT = ref([]);
  const pagenumD = ref(0);
  const getProductListD = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/products/deposit-products/',
    }).then((res) => {
      if (productListD.value.length == 0) {
        productListD.value = res.data;
        productListDR.value = productListD.value.map((product) => {
          const result = {
            productname: product.deposit_product.fin_prdt_nm,
            bankname: product.deposit_product.kor_co_nm,
            fin_prdt_cd: product.deposit_product.fin_prdt_cd,
          };
          product.options.forEach((el) => {
            if (el.save_trm % 6 == 0) {
              result[el.save_trm] = el.intr_rate;
            }
          });
          return result;
        });
        for (let i = 0; i < productListDR.value.length; i = i + 10) {
          productListDRT.value.push(productListDR.value.slice(i, i + 10));
        }
      }
      productListDRC.value = productListDR.value;
    });
  };

  // 적금상품
  const productListS = ref([]);
  const productListSR = ref([]);
  const productListSRC = ref([]);
  const productListSRT = ref([]);
  const pagenumS = ref(0);
  const getProductListS = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/products/saving-products/',
    }).then((res) => {
      if (productListS.value.length == 0) {
        productListS.value = res.data;
        productListSR.value = productListS.value.map((product) => {
          const result = {
            productname: product.saving_product.fin_prdt_nm,
            bankname: product.saving_product.kor_co_nm,
            fin_prdt_cd: product.saving_product.fin_prdt_cd,
          };
          product.options.forEach((el) => {
            if (el.save_trm % 6 == 0) {
              result[el.save_trm] = el.intr_rate;
            }
          });
          return result;
        });
        for (let i = 0; i < productListDR.value.length; i = i + 10) {
          productListSRT.value.push(productListSR.value.slice(i, i + 10));
        }
      }
      productListSRC.value = productListSR.value;
    });
  };

  // 환율
  const exchangeRateB1 = ref({});
  const exchangeRateB2 = ref({});
  const exchangeRateS1 = ref({});
  const exchangeRateS2 = ref({});

  const exchangeRate = ref([]);

  const getExchangeRate = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/exchangerate/',
    }).then((res) => {
      exchangeRate.value = res.data;
    });
  };

  // 상품상세
  // const productAll = ref([])
  // const productDetail=ref(null)
  // const detailcd=ref("")
  // const getProduct = function (fin_cd) {
  //   axios({
  //     method: 'get',
  //     url:'http://127.0.0.1:8000/products/products-all/'
  //   }).then((res) => {
  //     productAll.value=res.data
  //     let dors="deposit_product"
  //     const productDetailTMP = productAll.value.find((el) => {
  //       if(el.deposit_product!=-1 && el.deposit_product.fin_prdt_cd === fin_cd){
  //         return el
  //       }
  //       else if(el.saving_product!=-1 && el.saving_product.fin_prdt_cd === fin_cd){
  //         dors="saving_product"
  //         return el
  //       }

  //     })
  //     productDetail.value={
  //       product:productDetailTMP[dors],
  //       options:productDetailTMP.options
  //     }
  //     console.log(productDetail.value);
  //     })}

  //지도
  const koreanBanks = [
    "국민은행",
    "우리은행",
    "신한은행",
    "하나은행",
    "농협은행",
    "IBK기업은행",
    "SC제일은행",
    "한국씨티은행",
    "카카오뱅크",
    "케이뱅크",
    "토스뱅크",
    "수협은행",
    "대구은행",
    "부산은행",
    "광주은행",
    "전북은행",
    "제주은행",
    "경남은행"
  ];
  const regionList = ref([]);
  const provinceList = ref([]);
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/map/get-location/',
  }).then((res) => {
    regionList.value = res.data;
    regionList.value.forEach((el) => {
      if (provinceList.value.includes(el.province) == false) {
        provinceList.value.push(el.province);
      }
    });
  });

  const getCityList = function (province) {
    let cityList = new Set();
    regionList.value.forEach((el) => {
      if (el.province === province) {
        cityList.add(el.city);
      }
    });
    return Array.from(cityList);
  };

  const getSpecificRegionList = function (province, city) {
    let result = [];
    regionList.value.forEach((el) => {
      if (el.province === province && el.city === city) {
        result.push(el.region);
      }
    });
    return result;
  };

  // 로그인 관련
  const token = ref(null);
  const isLogin = computed(() => token.value !== null);

  //게시판 리스트




  return {
    banks,
    topRateDeposit,
    getTRDeposit,
    topRateSaving,
    getTRSaving,
    productListD,
    getProductListD,
    productListDR,
    productListDRT,
    pagenumD,
    productListDRC,
    productListS,
    getProductListS,
    productListSR,
    productListSRT,
    pagenumS,
    productListSRC,
    exchangeRateB1,
    exchangeRateB2,
    exchangeRateS1,
    exchangeRateS2,
    exchangeRate,
    getExchangeRate,
    // productAll, getProduct, productDetail,detailcd,
    regionList,
    provinceList,
    getCityList,
    getSpecificRegionList,
    token,isLogin,
    koreanBanks
  };
},{persist: true});
