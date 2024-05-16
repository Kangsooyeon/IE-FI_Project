<template>
    <div class="TR-container">
        <p class="TR-title ms-4 mt-4 mb-0">최고 이율 Top5 상품</p>
        <ul class="TR-selector d-flex justify-content-end my-2 mb-0 me-2">
            <li class="me-2">예금</li>
            <li>적금</li>
        </ul>
        <div v-if="store.topRateDeposit!=null && !toogleOption" class="ms-3 TR-list">
            <p v-for="(productD,idx) in store.topRateDeposit" :key="productD.deposit_product.fin_prdt_nm" class="TR-item">
                <a style="text-decoration: none" @click="console.log(1)">{{idx+1}}. {{ productD.deposit_product.fin_prdt_nm }} +{{ productD.option.intr_rate2 }}%</a>
            </p>
        </div>

        <div v-if="store.topRateSaving!=null && toogleOption" class="ms-3 TR-list">
            <p v-for="(productS,idx) in store.topRateSaving" :key="productS.saving_product.fin_prdt_nm" class="TR-item">
                <a style="text-decoration: none" @click="console.log(1)">{{idx+1}}. {{ productS.saving_product.fin_prdt_nm }}</a>
            </p>
        </div>
        <div>
            <p class="m-0 text-end me-2">전체 상품</p>
        </div>

    </div>
</template>


<script setup>
    import { ref, onMounted } from 'vue';
    import { useProjectStore } from '@/stores/project';
    import axios from 'axios';
    const store=useProjectStore()
    const toogleOption=ref(false)
    onMounted(()=>{
        store.getTRDeposit()
        store.getTRSaving()
    })
</script>


<style scoped>
.TR-title{
    font-size: 1.2rem;
    font-weight: 700
}
.TR-container{
    border: 2px solid black;
    border-radius:10px;
    width: 380px;
    height: 320px;
    
}
.TR-item{
    font-size: 1.0rem;
    font-weight: 700;
}
.TR-selector{
    font-size: 0.9rem;
    font-weight: 700;
    list-style-type: none;
}
.TR-list{
   
}
</style>