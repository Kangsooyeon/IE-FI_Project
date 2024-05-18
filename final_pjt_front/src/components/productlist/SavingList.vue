<template>
  <div>
    <SavingListPage/>
  </div>
</template>

<script setup>
  import { ref, onMounted, computed ,onBeforeMount} from 'vue';
  import {useProjectStore} from '@/stores/project'
  import SavingListPage from './SavingListPage.vue';
  const store=useProjectStore()
  onMounted(()=>{
      store.getProductListS()
      store.pagenumS=0
  })

</script>

<style scoped>

</style>