<template>
  <div>
    <div class="mb-4">
      <input type="text" v-model="searchKeyword" @input="search" placeholder="검색어를 입력하세요" class="form-control">
    </div>

    <div class="mb-4">
      <select v-model="searchType" class="form-select">
        <option value="nickname">닉네임</option>
        <option value="title">제목</option>
      </select>
    </div>

    <div v-if="filteredBoardList.length > 0">
      <div v-for="article in filteredBoardList" :key="article.id">
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
        <p>작성자: {{ article.nickname }}</p>
        <p>작성일: {{ article.created_at }}</p>
      </div>
    </div>
    <div v-else>
      <p>검색 결과가 없습니다.</p>
    </div>

    <button @click="createArticle" class="btn btn-primary float-end">게시글 생성</button>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useProjectStore } from '@/stores/project';

const store = useProjectStore();

//임시 데이터
const boardList = ref([
  {
    id: 1,
    title: '게시글 제목1',
    content: '게시글 내용1',
    nickname: '작성자1',
    created_at: '2021-10-01',
  },
  {
    id: 2,
    title: '게시글 제목2',
    content: '게시글 내용2',
    nickname: '작성자2',
    created_at: '2021-10-02',
  },
  {
    id: 3,
    title: '게시글 제목3',
    content: '게시글 내용3',
    nickname: '작성자3',
    created_at: '2021-10-03',
  },
]);

const searchKeyword = ref('');
const searchType = ref('nickname');

const filteredBoardList = computed(() => {
  return boardList.value.filter(article => {
    if (searchType.value === 'nickname') {
      return article.nickname.includes(searchKeyword.value);
    } else if (searchType.value === 'title') {
      return article.title.includes(searchKeyword.value);
    }
  });
});

onMounted(() => {
  // store.getBoardList();
});

const search = () => {
  // 검색 기능
};

const createArticle = () => {
  // 게시글 생성 기능
};
</script>

<style scoped>
/* 스타일 추가 */
</style>
