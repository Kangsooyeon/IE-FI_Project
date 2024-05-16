<template>
    <footer class="footer my-4">
        <ul class="footer-nav nav justify-content-center border-bottom pb-3 mb-3">
            <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Home</a></li>
            <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Products</a></li>
            <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Exchange</a></li>
            <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">FindBank</a></li>
            <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Community</a></li>
            <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">QnA</a></li>
        </ul>
        <p class="text-center text-muted small-size">&copy; 2024 SSAFY Busan&Ulsan Campus class2</p>
        <p class="text-center text-muted small-size"> 
            <a href="https://www.flaticon.com/kr/free-icons/-" title="- 아이콘">아이콘 제작자: kerismaker - Flaticon</a>
        </p>
    </footer>
</template>


<script setup>

</script>


<style scoped>
    /* footer {
        position : absolute;
        top : 100%;
        width: 100%;
    } */
    .small-size {
        font-size: 0.8rem;
        
    }
    @media (max-width: 650px) {
        .footer-nav {
            display: none;
        }
    }
</style>