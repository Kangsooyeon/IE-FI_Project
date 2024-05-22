<template>
    <div class="d-flex flex-column justify-content-center align-items-center">
        <div class="selector">
            <span @click="selectFalse" :class="{isSelected: !selected}">예금</span> |
            <span @click="selectTrue" :class="{isSelected: selected}">적금</span>
        </div>
        <DepositListPage v-if="!selected" />
        <SavingListPage v-if="selected" />
    </div>
</template>


<script setup>
    import { ref } from 'vue';
    import DepositListPage from "../../components/productlist/DepositListPage.vue";
    import SavingListPage from "../../components/productlist/SavingListPage.vue";
    
    const selected = ref(false);

    const selectTrue = () => {
        selected.value = true
    }
    const selectFalse = () => {
        selected.value = false
    }
</script>


<style scoped>
.selector{
    max-width: 980px;
}
.selector span{
    font-weight: bold;
    cursor: pointer;
}
.isSelected{
    color: #007bff;
}
.selector span:hover{
    color: #007bff;
}
</style>