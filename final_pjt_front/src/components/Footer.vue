<template>
    <footer class="footer my-4">
        <ul class="footer-nav nav justify-content-center border-bottom pb-3 mb-3">
            <li @click="goHome" class="nav-item"><a href="#" class="nav-link px-2 text-muted">Home</a></li>
            <li @click="goProduct" class="nav-item"><a href="#" class="nav-link px-2 text-muted">Products</a></li>
            <li @click="goExchange" class="nav-item"><a href="#" class="nav-link px-2 text-muted">Exchange</a></li>
            <li @click="goFindBank" class="nav-item"><a href="#" class="nav-link px-2 text-muted">FindBank</a></li>
            <li @click="goCommunity" class="nav-item"><a href="#" class="nav-link px-2 text-muted">Community</a></li>
        </ul>
        <p class="text-center text-muted small-size">&copy; 2024 SSAFY Busan&Ulsan Campus class2</p>
        <p class="text-center text-muted small-size"> 
            <a href="https://www.flaticon.com/kr/free-icons/-" title="- 아이콘">아이콘 제작자: kerismaker - Flaticon</a>
        </p>
    </footer>
</template>


<script setup>
    import { useRouter } from 'vue-router';
    const router = useRouter();

    const goHome = () => {
        router.push('/');
    }
    const goProduct = () => {
        router.push('/product');
    }
    const goExchange = () => {
        router.push('/er');
    }
    const goFindBank = () => {
        router.push('/map');
    }
    const goCommunity = () => {
        router.push('/article');
    }
</script>


<style scoped>
    footer {
        /* position: absolute; */
        top:150%;
        width: 100%;
        max-width: 980px;  /* Set your maximum width here */
        margin-right: auto;
        margin-left: auto;
        min-width: 395px;
    }
    .small-size {
        font-size: 0.8rem;
        
    }
    @media (max-width: 650px) {
        .footer-nav {
            display: none;
        }
    }
</style>