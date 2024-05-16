<template>
    <div class="quick-menu">
        <div class="quick-menu-container d-flex flex-row my-5 mb-0">	
            <h4 class="mt-2">빠른메뉴</h4>
            <ul class="quick-menu-list d-flex flex-row">
                <li class="quick-menu-item"><a href=""><div><img src="https://www.wooribank.com/img/common/etc/bg_btn/icon_set_011.png" alt="예금·적금"><p>예금·적금</p></div></a></li>
                <li class="quick-menu-item"><a href=""><div><img src="https://www.wooribank.com/img/common/etc/bg_btn/icon_set_022.png" alt="추천상품"><p>추천상품</p></div></a></li>
                <li class="quick-menu-item"><a href=""><div><img src="https://www.wooribank.com/img/common/etc/bg_btn/icon_set_033.png" alt="은행찾기"><p>은행찾기</p></div></a></li>	
                <li class="quick-menu-item"><a href=""><div><img src="https://www.wooribank.com/img/common/etc/bg_btn/icon_set_044.png" alt="환율계산"><p>환율계산</p></div></a></li>
                <li class="quick-menu-item"><a href=""><div><img src="https://www.wooribank.com/img/common/etc/bg_btn/icon_set_055.png" alt="커뮤니티"><p>커뮤니티</p></div></a></li>
                <li class="quick-menu-item"><a href=""><div><img src="https://www.wooribank.com/img/common/etc/bg_btn/icon_set_088.png" alt="QnA"><p>QnA</p></div></a></li>
            </ul>
        </div>
    </div>

</template>


<script setup>

</script>


<style scoped>
.quick-menu-list{
    list-style: none;
}
.quick-menu-item{
    background: transparent;
    border-radius: 50%;
    color: rgb(0, 0, 0);
    margin: 0 10px;
}
@media (max-width: 650px) {
        .quick-menu {
            display: none;
        }
    }
</style>