<template>
    <div class="quick-menu">
        <div class="quick-menu-container d-flex flex-row my-5 mb-0">	
            <h4 class="mt-2">빠른메뉴></h4>
            <ul class="quick-menu-list d-flex flex-row">
                <li @click="goProduct" class="quick-menu-item"><div class="d-flex flex-column align-items-center"><img src="@/assets/quickmenu/product1.png" width="50" alt="예금·적금"><p>예금·적금</p></div></li>
                <li @click="goHome" class="quick-menu-item"><div class="d-flex flex-column align-items-center"><img src="@/assets/quickmenu/rec1.png" width="50" alt="추천상품"><p>추천상품</p></div></li>
                <li @click="goFindBank" class="quick-menu-item"><div class="d-flex flex-column align-items-center"><img src="@/assets/quickmenu/bank1.png" width="50" alt="은행찾기"><p>은행찾기</p></div></li>	
                <li @click="goExchange" class="quick-menu-item"><div class="d-flex flex-column align-items-center"><img src="@/assets/quickmenu/ER1.png" width="50" alt="환율계산"><p>환율계산</p></div></li>
                <li @click="goCommunity" class="quick-menu-item"><div class="d-flex flex-column align-items-center"><img src="@/assets/quickmenu/article1.png" width="50" alt="커뮤니티"><p>커뮤니티</p></div></li>
            </ul>
        </div>
    </div>

</template>


<script setup>
    import { useRouter } from 'vue-router';
    const router = useRouter();

    const goHome = () => {
        router.push('/');
    }
    const goProduct = () => {
        router.push({name: 'productlist'});
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
.quick-menu-list{
    list-style: none;
}
.quick-menu-item{
    width: 78px;
    height: 100px;
    background: transparent;
    border-radius: 50%;
    color: rgb(0, 0, 0);
    margin: 0 10px;
    cursor: pointer;
}
@media (max-width: 650px) {
        .quick-menu {
            display: none;
        }
}
.quick-menu-item img {
    transition: width 0.3s ease-in-out;
}

.quick-menu-item:hover img {
    width: 60px;
}
h4{
    color:#0d6efd;
    font-weight: bold;
}
</style>