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
      store.pagenumD=0
  })

</script>

<style scoped>

</style>