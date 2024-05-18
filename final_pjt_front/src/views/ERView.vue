<template>
    <div>ER</div>
</template>


<script setup>
    import { ref,onMounted } from 'vue'
    import { useProjectStore } from '@/stores/project';

    const store = useProjectStore();

    onMounted(() => {
        store.getExchangeRate();
    });

</script>


<style scoped>

</style>