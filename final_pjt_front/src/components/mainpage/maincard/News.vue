<template>
  <div class="news-container">
    <div class="title">오늘의 뉴스</div>
    <div class="tabs">
      <button @click="setCategory('fin')">금융</button>
      <button @click="setCategory('economy')">경제</button>
      <button @click="setCategory('stock')">주식</button>
      <button @click="setCategory('coin')">코인</button>
    </div>
    <div class="news-content">
      <div v-for="(news, index) in filteredNews" :key="index" class="news-item">
        <a href="">{{ news.title }}</a>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';

const store = useProjectStore();
const category = ref('fin');

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
  switch (category.value) {
    case 'fin':
      return store.finNews.items.slice(0, 6);
    case 'economy':
      return store.economyNews.items.slice(0, 6);
    case 'stock':
      return store.stockNews.items.slice(0, 6);
    case 'coin':
      return store.coinNews.items.slice(0, 6);
    default:
      return [];
  }
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

.tabs {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 10px;
}

.tabs button {
  padding: 10px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
}

.tabs button:hover {
  background-color: #0056b3;
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
a{
  text-decoration: none;
  color: black;
}
a:hover{
  color: #007bff;
  text-decoration: underline;
}
</style>
