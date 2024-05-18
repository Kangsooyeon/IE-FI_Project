<template>
    <div class="container">
         <div class="row align-items-center">
             <div class="col-12 d-flex my-3">
                 <h2 class="title">적금 상품 목록</h2>
                 <div class="filter d-flex ml-auto">
                     <div class="my-2 mx-2">
                         <select id="bank" v-model="tempSelectedBank" class="form-control form-control-sm">
                             <option value="">모든 은행</option>
                             <option v-for="bank in store.banks" :key="bank">{{bank}}</option>
                         </select>
                     </div>
         
                     <div class="my-2 mx-2">
                         <select id="term" v-model="tempSelectedTerm" class="form-control form-control-sm">
                             <option value="">모든 기간</option>
                             <option v-for="term in terms" :key="term">{{term}}</option>
                         </select>
                     </div>
         
                     <button @click="applyFilter" class="mx-2 btn btn-primary btn-sm my-2">확인</button>
                 </div>
             </div>
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
                 <tr v-for="product in store.productListSRT[store.pagenumS]" :key="product.fin_prdt_cd">
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
                 <li class="page-item" :class="{ 'disabled': store.pagenumS === 0 }">
                     <span class="page-link" @click="pageDown">Previous</span>
                 </li>
                 <li class="page-item" v-for="(arr,idx) in store.productListSRT" :key="idx" :class="{ 'active': store.pagenumS === idx }" >
                     <span class="page-link" @click="pageSelector(idx)">{{ idx+1 }}</span>
                 </li>
                 <li class="page-item" :class="{ 'disabled': store.pagenumS === store.productListSRT.length - 1 }">
                     <span class="page-link" @click="pageUp">Next</span>
                 </li>
                 </ul>
             </nav>
             </div>
         </div>
     </div>
 </template>
 
 <script setup>
     import { ref,computed,watchEffect,onMounted } from 'vue';
     import {useProjectStore} from '@/stores/project'
     const store=useProjectStore()
     const pageDown=()=>{
         if(store.pagenumS>0){
             store.pagenumS--
         }
     }
     const pageUp=()=>{
         if(store.pagenumS<store.productListSRT.length-1){
             store.pagenumS++
         }
     }
     const pageSelector=(idx)=>{
         store.pagenumS=idx
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
         if (store.productListSRC.length > 0) {
             store.productListSRC.sort((a, b) => {
                 if (a[term] === null) {
                     return 1;
                 } else if (b[term] === null) {
                     return -1;
                 } else {
                     return isAscending ? a[term] - b[term] : b[term] - a[term];
                 }
             });
         store.productListSRT=store.productListSRC.reduce((acc, cur, idx) => {
             if (idx % 10 === 0) {
                 acc.push([cur]);
             } else {
                 acc[acc.length - 1].push(cur);
             }
             return acc;
         }, []);
         }
     }
 
     const tempSelectedBank = ref("");
     const tempSelectedTerm = ref("");
     const selectedBank = ref("");
     const selectedTerm = ref("");
 
     const terms = ['6', '12', '24', '36'];
 
     const applyFilter = () => {
         store.productListSRC=store.productListSR.filter(product => {
             if (tempSelectedBank.value!="" && tempSelectedTerm.value!="") {
                 if (product.bankname === tempSelectedBank.value && product[tempSelectedTerm.value]) {
                     return true;
                 }
             }
             else if(tempSelectedBank.value!=""){
                 if (product.bankname === tempSelectedBank.value) {
                     return true;
                 }
             }
             else if(tempSelectedTerm.value!=""){
                 if (product[tempSelectedTerm.value]) {
                     return true;
                 }
             }
             else{
                 return true;
             }
 
         });
         store.productListSRT=store.productListSRC.reduce((acc, cur, idx) => {
             if (idx % 10 === 0) {
                 acc.push([cur]);
             } else {
                 acc[acc.length - 1].push(cur);
             }
             return acc;
         }, []);
 
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