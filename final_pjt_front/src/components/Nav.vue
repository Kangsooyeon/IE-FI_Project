<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container">
                <p class="navbar-brand logo" @click="goHome" href="#"><img src="https://edu.ssafy.com/asset/images/header-logo.jpg" alt="Logo" height="40"></p>
                <div v-if="!store.isLogin" class="collapse navbar-collapse" id="navbarNav">
                    <p @click="goLogin" class="navbar-brand btn custom-btn login-btn mr-3">로그인</p>
                    <p @click="goRegister" class="navbar-brand btn custom-btn register-btn">회원가입</p>
                </div>
                <div v-else class="collapse navbar-collapse" id="navbarNav">
                    <p @click="goPofile" class="navbar-brand mr-3 profile">프로필</p>
                    <p @click="Logout" class="navbar-brand btn custom-btn register-btn">로그아웃</p>
                </div>

                <!-- Nav링크 -->
                <div class="collapse navbar-collapse ms-auto" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li @click="goProduct" class="nav-item">
                            <p class="nav-link text-dark" href="#">상품조회</p>
                        </li>
                        <li @click="goExchange" class="nav-item">
                            <p class="nav-link text-dark" href="#">환율계산</p>
                        </li>
                        <li @click="goFindBank" class="nav-item">
                            <p class="nav-link text-dark" href="#">은행지도</p>
                        </li>
                        <li @click="goCommunity" class="nav-item">
                            <p class="nav-link text-dark" href="#">커뮤니티</p>
                        </li>
                    </ul>
                </div>
                
                <!-- 햄버거버튼 -->
                <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <!-- 햄버거 메뉴 -->
                <div class="offcanvas offcanvas-end d-lg-none" tabindex="-1" id="offcanvasNavbar" aria-labelledby="offcanvasNavbarLabel">
                    <div class="offcanvas-header d-lg-none">
                        <p @click="goHome" class="navbar-brand logo" href="#"><img src="https://edu.ssafy.com/asset/images/header-logo.jpg" alt="Logo" height="40"></p>
                        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                    </div>
                    <div class="offcanvas-body d-lg-none">
                        <div v-if="!store.isLogin">
                            <p @click="goLogin" class="navbar-brand btn custom-btn login-btn mr-3 mb-1" href="#">로그인</p>
                            <p @click="goRegister" class="navbar-brand btn custom-btn register-btn mb-3" href="#">회원가입</p>
                        </div>
                        <div v-else>
                            <p @click="goPofile" class="navbar-brand profile mr-3 mb-1" href="#">프로필</p>
                            <p @click="Logout" class="navbar-brand btn custom-btn register-btn mb-3" href="#">로그아웃</p>
                        </div>
                        <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
                            <li @click="goProduct" class="nav-item">
                                <p class="nav-link text-dark" href="#">상품조회</p>
                            </li>
                            <li @click="goExchange" class="nav-item">
                                <p class="nav-link text-dark" href="#">환율계산</p>
                            </li>
                            <li @click="goFindBank" class="nav-item">
                                <p class="nav-link text-dark" href="#">은행지도</p>
                            </li>
                            <li @click="goCommunity" class="nav-item">
                                <p class="nav-link text-dark" href="#">커뮤니티</p>
                            </li>
                        </ul>
                    </div>
                </div>
    
                    
                </div>

        </nav>
    </div>
</template>

<script setup>
    import { useRouter } from 'vue-router';
    import { useProjectStore } from '@/stores/project';
    import axios from 'axios';

    const store = useProjectStore();
    const router = useRouter();

    const goHome = () => {
        router.push('/');
    }
    const goLogin = () => {
        router.push('/login');
    }
    const goRegister = () => {
        router.push('/signup');
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

    const Logout = () => {
        axios({
            method: 'post',
            url: 'http://127.0.0.1:8000/accounts/logout/',
            headers: {
                Authorization: `Token ${store.token}`
            }
            }).then((res) => {
                store.token = null;
                router.push('/');
            }).catch((err) => {
            });
    }

    const goPofile=()=>{
        router.push('/profile')
    }
</script>

<style scoped>
.navbar {
    background-color: white !important;
    max-width: 980px;
    min-width: 395px;
    margin: auto;
}

.custom-btn {
    font-size: 0.9rem;
    font-weight: 900;
    padding: 0.25rem 0.5rem;
    font-size: 0.875rem;
    line-height: 1.5;
    height: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    max-width: 74.2px;
}

.logo {
    margin-right: 1rem;
    cursor: pointer;
}

.login-btn {
    background-color: white;
    color: black;
    border: 1px solid #0082cd;
}

.register-btn {
    background-color: #0082cd;
    color: white;
}
.nav-link {
    font-size: 0.9rem;
    font-weight: 900;
    cursor: pointer;
}
@media (max-width: 992px) {
    .navbar-brand.logo {
        margin-right: auto;
    }
}
.nav-link:hover {
    text-decoration: underline;
}
.profile {
    font-weight: 700;
    font-size: 0.9rem;
    cursor: pointer;
}
.profile:hover {
    text-decoration: underline;
}


</style>