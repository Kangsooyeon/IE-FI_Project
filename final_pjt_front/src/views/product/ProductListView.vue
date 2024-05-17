<template>
    <div>
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
        { text: 'Bank Name', value: 'kor_co_nm' },
        { text: 'Financial Product Name', value: 'fin_prdt_nm' },
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