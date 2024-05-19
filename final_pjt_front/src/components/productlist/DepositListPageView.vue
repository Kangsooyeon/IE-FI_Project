<template>
   <div class="container">
        <div class="row align-items-center">
            <div class="col-12 d-flex my-3">
                <h2 class="title">예금 상품 목록</h2>
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

       

        <div class="d-flex flex-column justify-content-between align-items-center prtable">

            <table class="table table-striped mx-5">
            <thead>
                <tr>
                <th  class="field titleField">상품명</th>
                <th  class="field bankField">금융회사명</th>
                <th @click="toggleSort('6')">6개월 이율 <span>{{ currentSortTerm === '6' && sortState ? '▲' : '▼' }}</span></th>
                <th @click="toggleSort('12')">12개월 이율 <span>{{ currentSortTerm === '12' && sortState ? '▲' : '▼' }}</span></th>
                <th @click="toggleSort('24')">24개월 이율 <span>{{ currentSortTerm === '24' && sortState ? '▲' : '▼' }}</span></th>
                <th @click="toggleSort('36')">36개월 이율 <span>{{ currentSortTerm === '36' && sortState ? '▲' : '▼' }}</span></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="product in store.productListDRT[store.pagenumD]" :key="product.fin_prdt_cd">
                    <td @click="goDetail(product.fin_prdt_cd)" class="onEffect title">{{product.productname}}</td>
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
                <li class="page-item" :class="{ 'disabled': store.pagenumD === 0 }">
                    <span class="page-link" @click="pageDown">Previous</span>
                </li>
                <li class="page-item" v-for="(arr,idx) in store.productListDRT" :key="idx" :class="{ 'active': store.pagenumD === idx }" >
                    <span class="page-link" @click="pageSelector(idx)">{{ idx+1 }}</span>
                </li>
                <li class="page-item" :class="{ 'disabled': store.pagenumD === store.productListDRT.length - 1 }">
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
    import { useRouter } from 'vue-router';

    const router = useRouter();
    const store=useProjectStore()
    const pageDown=()=>{
        if(store.pagenumD>0){
            store.pagenumD--
        }
    }
    const pageUp=()=>{
        if(store.pagenumD<store.productListDRT.length-1){
            store.pagenumD++
            console.log(store.pagenumD);
        }
    }
    const pageSelector=(idx)=>{
        store.pagenumD=idx
    }

    const sortState = ref(true);
    const currentSortTerm = ref(null);

    const toggleSort = (term) => {
         if (currentSortTerm.value === term) {
             sortState.value = !sortState.value;
         } else {
             store.productListDRC=[...store.productListDR]
             currentSortTerm.value = term;
             sortState.value = true;
         }
         sortProducts(term, sortState.value);
         console.log(sortState.value);

     }
 
     const sortProducts = (term, isAscending) => {
    if (store.productListDRC.length > 0) {
        store.productListDRC.sort((a, b) => {
            if (a[term] === undefined && b[term] === undefined) {
                return 0;
            } else if (a[term] === undefined) {
                return isAscending ? 1 : -1;
            } else if (b[term] === undefined) {
                return isAscending ? -1 : 1;
            } else {
                return isAscending ? a[term] - b[term] : b[term] - a[term];
            }
        });
        store.productListDRC=store.productListDRC.reduce((acc,cur,idx,src)=>{
            if(cur[term]===undefined){
                acc[1].push(cur)
            }
            else{
                acc[0].push(cur)
            }

            if(idx===src.length-1)
                return [...acc[0],...acc[1]]
            return acc
            
        },[[],[]])
        store.productListDRT = store.productListDRC.reduce((acc, cur, idx) => {
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
        store.productListDRC=store.productListDR.filter(product => {
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
        store.productListDRT=store.productListDRC.reduce((acc, cur, idx) => {
            if (idx % 10 === 0) {
                acc.push([cur]);
            } else {
                acc[acc.length - 1].push(cur);
            }
            return acc;
        }, []);

    }
    const goDetail=function(fin_cd){
        router.push({name:'productdetail',params:{fin_prdt_cd:fin_cd}})
    }
</script>

<style scoped>
 .container{
     width: 1100px;
 }
.page-link{
    cursor: pointer;
}
.onEffect:hover{
    cursor: pointer;
    color: #007bff;
    }
.title{
    font-weight: 600;
}
.field{
    color: #007bff;
}
.titleField{
    width: 350px;
}
.bankField{
    width: 210px;
}
.prtable{
    height: 648px;
}
</style>