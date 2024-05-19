<template>
  <div class="container mt-5 d-flex flex-column justift-content-center align-items-center">
    <div class="card shadow-sm">
      <div class="card-body">
        <h1 class="card-title mb-4">{{ productDetail.product?.fin_prdt_nm }}</h1>
        <p class="card-text"><strong>금융회사명:</strong> {{ productDetail.product?.kor_co_nm }}</p>
        <p class="card-text"><strong>가입대상:</strong> {{ productDetail.product?.join_member }}</p>
        <p class="card-text"><strong>우대조건:</strong> {{ productDetail.product?.spcl_cnd }}</p>
        <p class="card-text"><strong>만기 후 이율:</strong> {{ productDetail.product?.mtrt_int || "-" }}</p>
        <p class="card-text"><strong>최고한도:</strong> {{ productDetail.product?.max_limit || "-" }}</p>
        <p class="card-text"><strong>가입방식:</strong> {{ productDetail.product?.join_way }}</p>

        <div class="table-responsive">
          <table class="table table-striped mt-4">
            <thead class="thead-dark">
              <tr>
                <th>계약기간</th>
                <th>금리</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(option, index) in productDetail.options" :key="index">
                <td>{{ option.save_trm }}</td>
                <td>{{ option.intr_rate2 }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <button class="btn btn-primary btn-block mt-4">가입하기</button>
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
</script>

<style scoped>
.card{
  max-width: 950px;
  min-width: 950px;
}
</style>
