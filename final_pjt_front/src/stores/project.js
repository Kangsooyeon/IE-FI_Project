import { ref, computed } from 'vue';
import { defineStore } from 'pinia';
import axios from 'axios';
import {useRouter} from 'vue-router'

export const useProjectStore = defineStore('project', () => {
  const router = useRouter()
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
              result[el.save_trm] = el.intr_rate2;
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
              result[el.save_trm] = el.intr_rate2;
              console.log(el);
            }
          });
          return result;
        });
        for (let i = 0; i < productListSR.value.length; i = i + 10) {
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
      url: 'http://127.0.0.1:8000/exchangerate/get-ER/',
    }).then((res) => {
      exchangeRate.value = res.data;
    });
  };

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
  const userInfo = ref({
    nickname: '',
    email: '',
    id_name: '',
    birth: null,
    sex:null,
    main_bank: null,
    salary: null,
    asset: null,
    desired_asset: null,
  });
    
  // 상품 가입시
  const sub_prdt_dep=ref([])
  const sub_prdt_sav=ref([])
  const getSubPrdtDep = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/profilepage/subscribed-deposit/',
      headers: {
        Authorization: `Token ${token.value}`,
      },}).then((res) => {
        sub_prdt_dep.value = res.data;
      })
  }
  const getSubPrdtSav = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/profilepage/subscribed-saving/',
      headers: {
        Authorization: `Token ${token.value}`,
      },}).then((res) => {
        sub_prdt_sav.value = res.data;
      })}

  //게시판 리스트
  const boardList = ref([]);
  const boardListC = ref([]);
  const boardListT = ref([]);
  const pagenumL=ref(0)
  const getBoardList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/articles/',
    }).then((res) => {
      boardList.value = res.data;
      boardListC.value = [...boardList.value]
      boardListC.value.reverse()
      boardListT.value=[]
      
      for (let i = 0; i < boardListC.value.length; i = i + 10) {
        boardListT.value.push(boardListC.value.slice(i, i + 10));
      }
    });}

    // 게시판 상세
    const articleDetail = ref({}) 
    const getArticle = function (id) {
      axios({
        method: 'get',
        url:`http://127.0.0.1:8000/articles/${id}/`
      }).then((res) => {
        articleDetail.value=res.data
        })}

    // 뉴스 관련
    const finNews = ref({})
    const economyNews = ref({})
    const stockNews = ref({})
    const coinNews = ref({})

    const getFinNews = function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/news/finance/',
      }).then((res) => {
        finNews.value = res.data;
      });
    }
    const getEconomyNews = function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/news/economy/',
      }).then((res) => {
        economyNews.value = res.data;
      }
    )}
    const getStockNews = function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/news/stock/',
      }).then((res) => {
        stockNews.value = res.data;
      }
    )}
    const getCoinNews = function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/news/coin/',
      }).then((res) => {
        coinNews.value = res.data;
      }
    )}
        
    //추천 상품
    const recommendProduct = ref({})
    const getRecommendProduct = function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/profilepage/recommend-products/',
        headers: {
          Authorization: `Token ${token.value}`,
        },}).then((res) => {
          recommendProduct.value = res.data;
        })
    }


    


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
    regionList,
    provinceList,
    getCityList,
    getSpecificRegionList,
    token,isLogin,
    koreanBanks,
    boardList,
    getBoardList,
    userInfo,
    boardListC,
    boardListT,
    pagenumL,
    articleDetail,
    getArticle,
    sub_prdt_dep,
    sub_prdt_sav,
    getSubPrdtDep,
    getSubPrdtSav,
    finNews,
    getFinNews,
    economyNews,
    getEconomyNews,
    stockNews,
    getStockNews,
    coinNews,
    getCoinNews,
    recommendProduct,
    getRecommendProduct
    

    
  };
},{persist: true});
