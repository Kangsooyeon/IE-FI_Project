<template>
    <div class="main-card-container">
        <TRProduct class="main-card-item my-3"/>
        <ERGraph class="main-card-item my-3"/>
    </div>
</template>

<script setup>
    import TRProduct from './maincard/TRProduct.vue';
    import ERGraph from './maincard/ERGraph.vue';
</script>


<style scoped>
.main-card-container{
    width: 960px;
    display: flex;
    align-items: center;
    justify-content: space-around;
    min-width: 395px;
}

@media (max-width: 991px) {
    .main-card-container {
        flex-direction: column;
    }
}

.main-card-item{
}
</style>