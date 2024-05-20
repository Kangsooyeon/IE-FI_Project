<template>
        <div class="d-flex flex-column justify-content-center align-items-center mt-4">
            <nav class="navbar navbar-expand-lg navbar-light bg-light profile-selector">
                <div class="container-fluid">
                    <div class="collapse navbar-collapse" id="navbarNav">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <RouterLink class="nav-link" :to="{name:'profile'}">회원정보</RouterLink>
                            </li>
                            <li class="nav-item">
                                <RouterLink class="nav-link" :to="{name:'myinfoupdate'}">회원정보수정</RouterLink>
                            </li>
                            <li class="nav-item">
                                <RouterLink class="nav-link" :to="{name:'subscriptionproduct'}">가입상품</RouterLink>
                            </li>
                            <li class="nav-item">
                                <RouterLink class="nav-link" :to="{name:'recommendproduct'}">추천상품</RouterLink>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>

            <RouterView/>
        </div>
</template>


<script setup>
import { RouterLink,RouterView } from 'vue-router';
</script>


<style scoped>
.profile-selector{
    width: 980px;
}
.nav-link{
    font-size: 1.1rem;
    font-weight: 700;
    color: black;
    margin: 0 10px;
}
.nav-item:hover{
    background-color: #5AC0F6;
    border-radius: 5px;
    color:white
}
.nav-link:hover{
    color:white;
}
</style>