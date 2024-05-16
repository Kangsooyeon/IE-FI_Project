<template>
    <div>TRProduct</div>
</template>


<script setup>
    import { ref, onMounted } from 'vue';
    import { useProjectStore } from '@/stores/project';
    import axios from 'axios';
    const store=useProjectStore()
    onMounted(()=>{
        store.getTRDeposit()
    })
</script>


<style scoped>

</style>