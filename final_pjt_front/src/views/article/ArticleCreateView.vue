<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-8">
        <h2 class="title my-4">게시글 작성</h2>
        <form>
          <div class="mb-3">
            <label for="title" class="form-label">제목</label>
            <input type="text" v-model="newArticle.title" id="title" class="form-control" required>
          </div>
          <div class="mb-3">
            <label for="content" class="form-label">내용</label>
            <textarea v-model="newArticle.content" id="content" class="form-control" rows="15" required></textarea>
          </div>
        </form>
        <button @click="submitArticle" type="submit" class="btn btn-primary">제출</button>
        <button @click="cancel" class="btn btn-secondary ml-2">취소</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import axios from 'axios';
import { useProjectStore } from '@/stores/project';

const router = useRouter();
const store = useProjectStore();
const newArticle = ref({
  title: '',
  content: '',
});

const submitArticle = () => {
  // 여기에 게시글 생성 로직을 추가합니다.
  // 예: 서버로 데이터 전송 또는 상태 업데이트
  axios({
    method: 'post',
    url: 'http://127.0.0.1:8000/articles/create/',
    data: {
      title: newArticle.value.title,
      content: newArticle.value.content,
      nickname: store.userInfo.nickname,
    },
    headers: {
      Authorization: `Token ${store.token}`,
      },
    }
  ).then((res)=>{
    store.getBoardList();
  }).then((res) => {
    router.push('/article');
  });   
  // 게시글 목록 페이지로 리디렉션
};

const cancel = () => {
  router.push('/article');
};
</script>

<style scoped>
.container {
  max-width: 900px;
  height: 750px;
}
.title {
  font-weight: 600;
}
</style>
