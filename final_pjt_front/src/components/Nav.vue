<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-light bg-light px-3">
            <div class="container d-flex justify-content-center">
                <a class="navbar-brand logo" href="#"><img src="" alt="Logo" height="30"></a>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <a class="navbar-brand btn custom-btn login-btn mr-3" href="#">로그인</a>
                    <a class="navbar-brand btn custom-btn register-btn" href="#">회원가입</a>
                </div>

                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="#">상품조회</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="#">환율계산</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="#">은행지도</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="#">커뮤니티</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link text-dark" href="#">QnA</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </div>
</template>

<script setup>
</script>

<style scoped>
.navbar {
    background-color: white !important;
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
}

.logo {
    margin-right: 1rem;
}

.login-btn {
    background-color: white;
    color: black;
    border: 1px solid #9cc5fd;
}

.register-btn {
    background-color: #9cc5fd;
    color: white;
}
.nav-link {
    font-size: 0.9rem;
    font-weight: 900;
}
@media (max-width: 992px) {
    .navbar-brand.logo {
        margin-right: 16rem;
    }
}

</style>