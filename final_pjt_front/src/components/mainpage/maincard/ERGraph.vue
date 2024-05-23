<!-- ExchangeRateGraph.vue -->
<template>
    <div class="ERG-container card">
      <p class="ERG-title ms-4 mt-4 mb-0 text-start">오늘의 환율</p>
      <div class="slider">
        <img :src="currentImage" class="graph-image" />
      </div>
      <div class="dots">
        <span
          v-for="(dot, index) in images.length"
          :key="index"
          class="dot"
          :class="{ active: currentIndex === index }"
          @click="showImage(index)"
        ></span>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, onMounted } from 'vue';
  import axios from 'axios';

  const images = ref([
  new URL('@/assets/erg/USD.png', import.meta.url).href,
  new URL('@/assets/erg/JPY.png', import.meta.url).href,
  new URL('@/assets/erg/EUR.png', import.meta.url).href,
  new URL('@/assets/erg/CNY.png', import.meta.url).href,
]);
  
  const currentIndex = ref(0);
  
  const currentImage = computed(() => {
    return images.value[currentIndex.value];
  });
  
  const showImage = (index) => {
    currentIndex.value = index;
  };
  
  const nextImage = () => {
    currentIndex.value = (currentIndex.value + 1) % images.value.length;
  };
  
  onMounted(() => {

    setInterval(nextImage, 3000);
  });
  </script>
  
  <style scoped>
  .ERG-container {
    border: 1px solid #e9ecef;
    border-radius: 8px;
    width: 400px;
    height: 400px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    position: relative;
    padding: 10px;
  }
  
  .ERG-title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 10px;
    text-align: center;
    border-bottom: 2px solid #e9ecef;
    color: #333;
    height: 38px;
  }
  
  .slider {
    width: 100%;
    height: 300px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .graph-image {
    max-width: 100%;
    max-height: 100%;
    border-radius: 2px;
  }
  
  .dots {
    display: flex;
    justify-content: center;
    position: absolute;
    bottom: 10px;
    width: 100%;
  }
  
  .dot {
    height: 10px;
    width: 10px;
    margin: 0 5px;
    background-color: #bbb;
    border-radius: 50%;
    display: inline-block;
    cursor: pointer;
  }
  
  .dot.active {
    background-color: #717171;
  }
  </style>
  