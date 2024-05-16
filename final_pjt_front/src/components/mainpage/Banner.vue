<template>
    <div class="carousel-container">
        <div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
            <ol class="carousel-indicators">
                <li data-bs-target="#carouselExample" data-bs-slide-to="0" class="active"></li>
                <li data-bs-target="#carouselExample" data-bs-slide-to="1"></li>
                <li data-bs-target="#carouselExample" data-bs-slide-to="2"></li>
            </ol>
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <img src="@/assets/bannerexample/ex1.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/bannerexample/ex2.jpg" class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                    <img src="@/assets/bannerexample/ex3.jpg" class="d-block w-100" alt="...">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </div>
</template>


<script setup>

</script>


<style scoped>
.carousel-container{
    min-width: 395px;
}
.carousel-inner {
    max-height: 500px;
    max-width: 980px;
    border-radius: 5px;
}
.carousel-indicators li {
    list-style: none;
}
.carousel-item img {
    border-radius: 5px;
}

</style>