<template>
    <div class="start">
        <Nav/>
        <router-view></router-view>
        <Footer/>
    </div>
</template>


<script setup>
    import Nav from './components/Nav.vue'
    import Footer from './components/Footer.vue'
</script>


<style scoped>
/* .start{
    height: 2000px;
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 580px;
} */
</style>