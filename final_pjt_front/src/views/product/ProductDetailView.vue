<template>
  <div class="container mt-5 d-flex flex-column justify-content-center align-items-center">
    <div class="card shadow-sm">
      <div class="card-body">
        <h1 class="card-title mb-4">{{ productDetail.product?.fin_prdt_nm }}</h1>
        <p class="card-text"><strong>금융회사명:</strong> {{ productDetail.product?.kor_co_nm }}</p>
        <p class="card-text"><strong>가입대상:</strong> {{ productDetail.product?.join_member }}</p>
        <p class="card-text"><strong>우대조건:</strong> {{ productDetail.product?.spcl_cnd }}</p>
        <p class="card-text"><strong>만기 후 이율:</strong> {{ productDetail.product?.mtrt_int || "-" }}</p>
        <p class="card-text"><strong>최고한도:</strong> {{ productDetail.product?.max_limit ? (productDetail.product?.max_limit).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "원" : "-" }}</p>
        <p class="card-text"><strong>가입방식:</strong> {{ productDetail.product?.join_way }}</p>
        <p class="card-text"><strong>기타 사항:</strong> {{ productDetail.product?.etc_note }}</p>

        <div class="table-responsive">
          <table class="table table-striped mt-4">
            <thead class="thead-dark">
              <tr>
                <th>계약기간(월)</th>
                <th>최고우대금리</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(option, index) in productDetail.options" :key="index">
                <td>{{ option.save_trm }}</td>
                <td>{{ option.intr_rate2 }}</td>
                <td>
                  <button v-if="store.isLogin" class="btn btn-primary btn-sm" @click="openModal(option)">가입</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- 금액 입력 모달 -->
    <div v-if="isModalOpen" class="modal" tabindex="-1" style="display:block; background-color: rgba(0,0,0,0.5);">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">금액 입력</h5>
            <button type="button" class="btn-close" @click="closeModal"></button>
          </div>
          <div class="modal-body">
            <p>가입할 금액을 입력하세요:</p>
            <input type="number" v-model="modalInputValue" class="form-control">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">취소</button>
            <button type="button" class="btn btn-primary" @click="confirmInput">확인</button>
          </div>
        </div>
      </div>
    </div>

    <!-- 가입 확인 모달 -->
    <div v-if="isConfirmModalOpen" class="modal" tabindex="-1" style="display:block; background-color: rgba(0,0,0,0.5);">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">가입 확인</h5>
            <button type="button" class="btn-close" @click="closeConfirmModal"></button>
          </div>
          <div class="modal-body">
            <p>만기 후 예상 금액: {{ expectedAmount }}</p>
            <p>가입하시겠습니까?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeConfirmModal">취소</button>
            <button type="button" class="btn btn-primary" @click="subscribe">확인</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';
import { useRoute } from 'vue-router';
import axios from 'axios';

const store = useProjectStore();
const route = useRoute();

const productId = ref(route.params.fin_prdt_cd);
const productAll = ref([]);
const productDetail = ref({});
const signMoney = ref(0);
const isModalOpen = ref(false);
const isConfirmModalOpen = ref(false);
const modalInputValue = ref(0);
const selectedOption = ref({});

const DorS= ref('deposit');
const expectedAmount = ref(0);
const subscribtionId = ref(0);


onMounted(() => {
  axios({
    method: 'get',
    url: 'http://127.0.0.1:8000/products/products-all/',
  }).then((res) => {
    productAll.value = res.data;
    let dors = 'deposit_product';
    const productDetailTMP = productAll.value.find((el) => {
      if (
        el['deposit_product'] !== undefined &&
        el.deposit_product.fin_prdt_cd === productId.value
      ) {
        return el;
      } else if (
        el['saving_product'] !== undefined &&
        el.saving_product.fin_prdt_cd === productId.value
      ) {
        dors = 'saving_product';
        return el;
      }
    });
    productDetail.value = {
      product: productDetailTMP[dors],
      options: productDetailTMP.options,
    };
  });
});

const openModal = (option) => {
  subscribtionId.value = option.id;
  selectedOption.value = option;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};

const confirmInput = () => {
  const maxLimit = productDetail.value.product?.max_limit || Infinity;
  if (modalInputValue.value > maxLimit) {
    alert('입력한 금액이 최고 한도를 초과합니다. 다시 입력해주세요.');
  } else {
    signMoney.value = modalInputValue.value;
    calculateExpectedAmount();
    isModalOpen.value = false;
    isConfirmModalOpen.value = true;
  }
};

const closeConfirmModal = () => {
  isConfirmModalOpen.value = false;
};

const calculateExpectedAmount = () => {
  const interestRate = parseFloat(selectedOption.value.intr_rate2) / 100;
  const principal = parseFloat(signMoney.value);
  const period = parseFloat(selectedOption.value.save_trm) / 12; // 계약기간을 연 단위로 변환
  if (productDetail.value.product?.fin_prdt_nm.includes('예금')) {
    // 예금 방식 계산
    expectedAmount.value = (principal + (principal * interestRate * period)).toFixed(2);
  } else {
    // 적금 방식 계산
    DorS.value = 'saving';
    expectedAmount.value = ((principal * period) + (principal * interestRate * (period * (period + 1) / 2) / period)).toFixed(2);
  }
};

const subscribe = () => {
  // 가입 처리 로직 추가
  console.log(productDetail.value.options);
  console.log(subscribtionId.value);
  console.log(signMoney.value);
  console.log( parseInt(expectedAmount.value));
  if(DorS.value === 'deposit'){
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/products/subscribed-${DorS.value}/`,
      data: {
        deposit_option: subscribtionId.value,
        sign_money: signMoney.value,
        mtrt_money: parseInt(expectedAmount.value),
      },
      headers: {
        Authorization: `Token ${store.token}`,
      },
    }).then((res) => {
      alert(`가입이 완료되었습니다. 가입 금액: ${signMoney.value}원`);
    });
  }
  else{
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/products/subscribed-${DorS.value}/`,
      data: {
        saving_option: subscribtionId.value,
        sign_money: signMoney.value,
        mtrt_money: parseInt(expectedAmount.value),
      },
      headers: {
        Authorization: `Token ${store.token}`,
      },
    }).then((res) => {
      alert(`가입이 완료되었습니다. 가입 금액: ${signMoney.value}원`);
    });
  }
  isConfirmModalOpen.value = false;
};
</script>

<style scoped>
.card {
  max-width: 950px;
  min-width: 950px;
}

.modal {
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-dialog {
  max-width: 400px;
  margin: auto;
}
</style>
