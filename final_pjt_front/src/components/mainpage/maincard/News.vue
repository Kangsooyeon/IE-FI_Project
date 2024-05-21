<!-- NewsCard.vue -->
<template>
    <div class="news-container card colorSelector">
      <h2 class="title">금융 뉴스</h2>
      <div class="news-content">
        <p v-for="(news, index) in newsList" :key="index" class="news-item">
          {{ news }}
        </p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  
  const newsList = ref([]);
  
  const fetchNews = () => {
    // 뉴스 데이터를 가져오는 로직을 여기에 추가합니다.
    // 임시로 뉴스 데이터를 설정합니다.
    newsList.value = [
      "금융 시장, 전 세계적으로 안정세 회복",
      "2024년 경제 전망, 경제 성장률 3.5% 예상",
      "암호화폐 시장, 큰 폭의 하락세",
      "부동산 시장, 안정세 유지",
      "주식 시장, 다시 상승세로 전환"
    ];
  };
  
  onMounted(() => {
    fetchNews();
  });
  </script>
  
  <style scoped>
  .news-container {
    border: 1px solid #e9ecef;
    border-radius: 8px;
    width: 880px;
    height: 350px;
    background-color: #fff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    overflow: hidden;
    position: relative;
    padding: 10px;
  }
  
  .title {
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 10px;
    text-align: center;
  }
  
  .news-content {
    padding: 10px;
    height: 300px;
    overflow-y: auto;
  }
  
  .news-item {
    margin-bottom: 10px;
    font-size: 1rem;
  }
  .colorSelector{
    background-color: #f8f9fa;
  }
  </style>
  