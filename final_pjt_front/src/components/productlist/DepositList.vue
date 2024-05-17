<template>
  <div>
    <DepositListPageView/>  
  </div>
</template>

<script setup>
  import { ref, onMounted, computed ,onBeforeMount} from 'vue';
  import {useProjectStore} from '@/stores/project'
  import DepositListPageView from './DepositListPageView.vue';
  const store=useProjectStore()
  onMounted(()=>{
      store.getProductListD()
  })

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