<!-- <v-card
  title="전체 상품 목록"
  flat
>
  <template v-slot:text>
    <v-text-field
      v-model="search"
      label="Search"
      prepend-inner-icon="mdi-magnify"
      variant="outlined"
      hide-details
      single-line
    ></v-text-field>
  </template>

  <v-data-table
    :headers="headers"
    :items="store.productList"
    :search="search"
  ></v-data-table>
</v-card> -->
<template>
  <div>

>
    <v-data-table
        v-if="store.productList && store.productList.length > 0"
        :headers="headers"
        :items="store.productList"
        :items-per-page="10"
        class="elevation-1"
    >
    </v-data-table>

  </div>
</template>


<script setup>
  import { ref, onMounted } from 'vue';
  import {useProjectStore} from '@/stores/project'
  const store=useProjectStore()
  onMounted(()=>{
      store.getProductList()
      console.log(1);
  })
  const headers = [
      { text: '은행 이름', value: 'deposit_product.kor_co_nm' },
      { text: '상품 이름', value: 'deposit_product.fin_prdt_nm' },
      { text: '예치 기간', value: 'options.save_trm' },
      { text: '최고 우대 금리', value: 'options.intr_rate2' },
    ];
</script>

<style scoped>
  .PL-container{
      width: 960px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-around;
      min-width: 395px;
  }
</style>