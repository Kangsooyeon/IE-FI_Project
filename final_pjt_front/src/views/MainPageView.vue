<template>
    <div class="d-flex flex-column align-items-center justify-content-center">
        <Banner/>
        <QuickMenu class="quick-menu"/>
        <MainCard/>
        <News/>
    </div>
</template>


<script setup>
    import Banner from '@/components/mainpage/Banner.vue'
    import QuickMenu from '@/components/mainpage/QuickMenu.vue';
    import MainCard from '@/components/mainpage/MainCard.vue';
    import News from '@/components/mainpage/News.vue';
</script>


<style scoped>

</style>