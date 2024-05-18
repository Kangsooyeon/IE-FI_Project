<template>
  <div>
    {{ productDetail }}
    <h1>{{ productDetail.product.fin_prdt_nm }}</h1>
    <!-- <p>{{ productDetail.product.kor_co_nm }}</p>
    <p>{{ productDetail.product.etc_note }}</p>
    <p>{{ productDetail.product.join_member }}</p>
    <p>{{ productDetail.product.join_way }}</p> -->

    <table>
      <thead>
        <tr>
          <th>계약기간</th>
          <th>이율</th>
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
</template>


<script setup>
  import ProductDescription from '@/components/productdetail/ProductDescription.vue';
  import { ref, onMounted } from 'vue'
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
              url:'http://127.0.0.1:8000/products/products-all/'
            }).then((res) => {
              productAll.value=res.data
              let dors="deposit_product"
              const productDetailTMP = productAll.value.find((el) => {
                if(el['deposit_product']!==undefined && el.deposit_product.fin_prdt_cd === productId.value){
                  return el
                }
                else if(el['saving_product']!==undefined && el.saving_product.fin_prdt_cd === productId.value){
                  dors="saving_product"
                  return el
                }

              })
              productDetail.value={
                product:productDetailTMP[dors],
                options:productDetailTMP.options
              }
              console.log(productId.value);
              console.log(productDetail.value);
              })
  });
</script>

<style scoped>

</style>