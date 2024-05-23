<template>
  <div>
    <div v-if="isSub" class="rec_prdt-container mt-5 d-flex flex-column justify-content-start align-items-center">
        <div class="maincontainer">
          <div class="thecard">
            <div class="thefront d-flex flex-column justify-content-center align-items-center">
              <h1 >{{ selectedProduct?.product?.fin_prdt_nm || store.userInfo.nickname+"님을 위한" }}<br><h1 v-if="!selectedProduct?.product?.fin_prdt_nm">추천상품 리스트</h1></h1>
              <img v-if="!selectedProduct?.product?.fin_prdt_nm" src="@/assets/recprdt/1.png" width="250" alt="">
              <img v-else :src="imgUrl" width="100" height="100" alt="" class="prdtimg">
            </div>
            <div class="theback d-flex flex-column justify-content-center align-items-center">
              <h1 v-if="selectedProduct?.product?.fin_prdt_nm">{{ selectedProduct?.product?.fin_prdt_nm }}</h1>
              <p v-if="!selectedProduct?.product?.fin_prdt_nm">추천 상품을 선택해 주세요</p>
              <p v-if="selectedProduct?.product?.fin_prdt_nm">가입대상 : {{ selectedProduct?.product?.join_member}}</p>
              <p v-if="selectedProduct?.product?.fin_prdt_nm">최고한도 : {{ selectedProduct.product?.max_limit ? (selectedProduct.product?.max_limit).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",") + "원" : "-"}}</p>
              <button v-if="selectedProduct?.product?.fin_prdt_nm" @click="goDetail(selectedProduct?.product)">가입하러 가기</button>
            </div>
          </div>
        </div>
        <div>
          <table class="table mt-4">
            <thead>
              <tr>
                <th>상품명</th>
                <th>금융회사명</th>
                <th>이율</th>
                <th>계약기간</th>
              </tr>
            </thead>
            <tbody>
              <tr class="rec-item" v-for="item in store.recommendProduct.product_list" :key="item.id" @click="selectProduct(item)" :class="{ active: selectedProduct?.id === item.id }">
                <td class="rec-item">{{ item.product.fin_prdt_nm }}</td>
                <td>{{ item.product.kor_co_nm }}</td>
                <td>{{ item.intr_rate2 }}%</td>
                <td>{{ item.save_trm }}개월</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    <div v-else class="d-flex flex-column justify-content-center align-items-center mt-5">
      <h4 class="text-primary">상품추천 서비스를 위해 추가 정보를 입력해 주세요!</h4>
      <br>
      <p>*상품 추천 알고리즘은 본인의 희망자산을 제외한 모든 추가정보가 입력 되어야 합니다*</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';
import { useRouter } from 'vue-router';

const store = useProjectStore();
const router = useRouter();
const isSub = ref(false);

if(store.userInfo.salary!==null && store.userInfo.asset!==null && store.userInfo.birth!==null && store.userInfo.main_bank!==null &&(store.userInfo.salary!==0 && store.userInfo.asset!==0)){
  isSub.value = true;
}

const selectedProduct = ref({});
const imgUrl= ref('');
const isFlipped = ref(false);

const selectProduct = (product) => {
  selectedProduct.value = product;
  imgUrl.value = `/assets/bankimg/${product.product.kor_co_nm}.png`
};

const goDetail = (option) => {
  router.push({ name: 'productdetail', params: { fin_prdt_cd: option.fin_prdt_cd } });
};

onMounted(() => {
  if(isSub.value){
    store.getRecommendProduct();
  }
});
</script>

<style scoped>
.rec_prdt-container {
  width: 660px;
}

.table {
  width: 100%;
  text-align: left;
  margin-top: 20px;
}

.table th,
.table td {
  padding: 10px;
}

.table tr:hover {
  background-color: #f1f1f1;
  cursor: pointer;
}

.table .active {
  background-color: #007bff;
  color: #fff;
}

.maincontainer {
  width: 350px;
  height: 400px;
  background: none;
  top: 50%;
  left: 50%;
}

.thecard {
  position: relative;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  transform-style: preserve-3d;
  transition: all 0.8s ease;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.thecard:hover{
  transform: rotateY(180deg);
}

.thefront,
.theback {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 10px;
  backface-visibility: hidden;
  overflow: hidden;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.thefront {
  background: white;
}

.theback {
  background: #0d6efd;
  color: #fff;
  text-align: center;
  transform: rotateY(180deg);
}

.thefront h1,
.theback h1 {
  font-family: 'zilla slab', sans-serif;
  padding: 30px;
  font-weight: bold;
  font-size: 24px;
  text-align: center;
}

.thefront p,
.theback p {
  font-family: 'zilla slab', sans-serif;
  padding: 30px;
  font-weight: normal;
  font-size: 12px;
  text-align: center;
}
.rec-item{
  cursor: pointer;
}
.rec-item:hover{
  color: #007bff;
}
.prdtimg{
  border-radius: 10px;
  width: 120px;
  height: 120px;
}
</style>
