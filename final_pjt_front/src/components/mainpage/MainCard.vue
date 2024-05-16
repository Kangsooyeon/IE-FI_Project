<template>
    <div class="container mt-4">
        <div class="row">
            <div class="col-xl-6 d-flex justify-content-center">
                <TRProduct/>
            </div>
            <div class="col-xl-6 d-flex justify-content-center">
                <ERGraph/>
            </div>
        </div>
    </div>
</template>

<script setup>
    import TRProduct from './maincard/TRProduct.vue';
    import ERGraph from './maincard/ERGraph.vue';
</script>


<style scoped>

</style>