<template>
    <div class="container">
        <div class="d-flex justify-content-start align-items-center my-5">
            <h2>예금 상품 목록</h2>
        </div>
        <div class="d-felx flex-column">
            <div>
                <label for="bank">은행 선택:</label>
                <select id="bank" v-model="tempSelectedBank" class="form-control">
                    <option value="">모든 은행</option>
                    <option v-for="bank in store.banks" :key="bank">{{bank}}</option>
                </select>
            </div>

            <div>
                <label for="term">예치기간 선택:</label>
                <select id="term" v-model="tempSelectedTerm" class="form-control">
                    <option value="">모든 기간</option>
                    <option v-for="term in terms" :key="term">{{term}}</option>
                </select>
            </div>

            <button @click="applyFilter" class="btn btn-primary">확인</button>
        </div>
        <div class="d-flex flex-column justify-content-center align-items-center">

            <table class="table table-striped mx-5">
            <thead>
                <tr>
                <th>상품명</th>
                <th>금융회사명</th>
                <th @click="toggleSort('6')">6개월 이율 <span>{{ currentSortTerm === '6' && sortState ? '▲' : '▼' }}</span></th>
                <th @click="toggleSort('12')">12개월 이율 <span>{{ currentSortTerm === '12' && sortState ? '▲' : '▼' }}</span></th>
                <th @click="toggleSort('24')">24개월 이율 <span>{{ currentSortTerm === '24' && sortState ? '▲' : '▼' }}</span></th>
                <th @click="toggleSort('36')">36개월 이율 <span>{{ currentSortTerm === '36' && sortState ? '▲' : '▼' }}</span></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="product in store.productListDRT[store.pagenum]" :key="product.productname">
                    <td>{{product.productname}}</td>
                    <td>{{product.bankname}}</td>
                    <td>{{product['6'] ? product['6'] + '%' : '-'}}</td>
                    <td>{{product['12'] ? product['12'] + '%' : '-'}}</td>
                    <td>{{product['24'] ? product['24'] + '%' : '-'}}</td>
                    <td>{{product['36'] ? product['36'] + '%' : '-'}}</td>
                </tr>
            </tbody>
           
            </table>
            <div class="my-4">
            <nav aria-label="Page navigation example">
                <ul class="pagination">
                <li class="page-item" :class="{ 'disabled': store.pagenum === 0 }">
                    <span class="page-link" @click="pageDown">Previous</span>
                </li>
                <li class="page-item" v-for="(arr,idx) in store.productListDRT" :key="idx" :class="{ 'active': store.pagenum === idx }" >
                    <span class="page-link" @click="pageSelector(idx)">{{ idx+1 }}</span>
                </li>
                <li class="page-item" :class="{ 'disabled': store.pagenum === store.productListDRT.length - 1 }">
                    <span class="page-link" @click="pageUp">Next</span>
                </li>
                </ul>
            </nav>
            </div>
        </div>
    </div>
</template>

<script setup>
    import { ref,computed,watchEffect } from 'vue';
    import {useProjectStore} from '@/stores/project'
    const store=useProjectStore()
    const pageDown=()=>{
        if(store.pagenum>0){
            store.pagenum--
            console.log(store.pagenum);
        }
    }
    const pageUp=()=>{
        if(store.pagenum<store.productListDRT.length-1){
            store.pagenum++
            console.log(store.pagenum);
        }
    }
    const pageSelector=(idx)=>{
        store.pagenum=idx
    }

    const sortState = ref(true);
    const currentSortTerm = ref(null);

    const toggleSort = (term) => {
        if (currentSortTerm.value === term) {
            sortState.value = !sortState.value;
        } else {
            currentSortTerm.value = term;
            sortState.value = true;
        }
        sortProducts(term, sortState.value);
    }

    const sortProducts = (term, isAscending) => {
        if (store.productListDRT[store.pagenum]) {
            store.productListDRT[store.pagenum].sort((a, b) => isAscending ? a[term] - b[term] : b[term] - a[term]);
        }
    }

    const tempSelectedBank = ref("");
    const tempSelectedTerm = ref("");
    const selectedBank = ref("");
    const selectedTerm = ref("");

    const terms = ['6', '12', '24', '36'];

    const applyFilter = () => {
        console.log(1);
    }
</script>

<style scoped>
.container{
    max-width: 980px;
    min-height: 850px;
}
.page-link{
    cursor: pointer;
}
</style>