<template>
  <div class="news-container">
    <div class="title">오늘의 뉴스</div>
    <div class="tabs">
      <span @click="setCategory('fin')" :class="{ active: category === 'fin' }" class="tab-btn">금융</span>
      <span @click="setCategory('economy')" :class="{ active: category === 'economy' }" class="tab-btn">경제</span>
      <span @click="setCategory('stock')" :class="{ active: category === 'stock' }" class="tab-btn">주식</span>
      <span @click="setCategory('coin')" :class="{ active: category === 'coin' }" class="tab-btn">코인</span>
    </div>
    <p class="m-0 text-end update-time">최신 업데이트 - {{ newsUpdate.slice(0, 25) }}</p>
    <div class="news-content">
      <div v-for="(news, index) in filteredNews" :key="index" class="news-item">
        <a :href="news.link" target="_blank">{{ news.title }}</a>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';

const store = useProjectStore();
const category = ref('fin');
const newsUpdate = ref('');

onMounted(() => {
  store.getFinNews();
  store.getEconomyNews();
  store.getStockNews();
  store.getCoinNews();
});

const setCategory = (cat) => {
  category.value = cat;
};

const filteredNews = computed(() => {
  if (store.finNews["items"] && store.economyNews["items"] && store.stockNews["items"] && store.coinNews["items"]) {
    switch (category.value) {
      case 'fin':
        newsUpdate.value = store.finNews.lastBuildDate;
        return store.finNews?.items.slice(0, 10);
      case 'economy':
        newsUpdate.value = store.economyNews.lastBuildDate;
        return store.economyNews?.items.slice(0, 10);
      case 'stock':
        newsUpdate.value = store.stockNews.lastBuildDate;
        return store.stockNews?.items.slice(0, 10);
      case 'coin':
        newsUpdate.value = store.coinNews.lastBuildDate;
        return store.coinNews?.items.slice(0, 10);
      default:
        return [];
    }
  }
});
</script>

<style scoped>
.news-container {
  border: 1px solid #e9ecef;
  border-radius: 8px;
  width: 880px;
  height: 400px;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  position: relative;
  padding: 20px;
  margin: auto;
  font-family: 'Arial', sans-serif;
}

.title {
  font-size: 1.8rem;
  font-weight: 700;
  text-align: center;
  color: #333;
}

.tabs {
  display: flex;
  justify-content: center;
  gap: 30px;
  margin-bottom: 5px;
}

.tabs span {
  padding: 10px 20px;
  border-radius: 20px;
  cursor: pointer;
  font-weight: 500;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.tabs span:hover, .tabs span.active {
  background-color: #007bff;
  color: #fff;
}

.update-time {
  font-size: 0.9em;
  color: #666;
  margin-bottom: 20px;
}

.news-content {
  padding: 10px;
  height: 250px;
  overflow-y: auto;
  border-top: 1px solid #e9ecef;
}

.news-item {
  margin-bottom: 10px;
  font-size: 1rem;
}

a {
  text-decoration: none;
  color: #333;
  transition: color 0.3s ease, text-decoration 0.3s ease;
}

a:hover {
  color: #007bff;
  text-decoration: underline;
}
.tab-btn{
  width: 72px;
  height: 38px;
}
</style>
