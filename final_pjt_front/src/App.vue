<template>
    <div>
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

</style>