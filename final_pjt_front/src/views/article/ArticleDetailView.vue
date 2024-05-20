<template>
  <div class="container my-4">
    <div class="article-detail card mb-4 p-4 shadow-sm">
      <h2 class="card-title mb-5">{{ store.articleDetail.title }}</h2>
      <p class="card-text content">{{ store.articleDetail.content }}</p>
      <p class="text-muted">작성자: {{ store.articleDetail.nickname }}</p>
      <p class="text-muted">작성일: {{ new Date(store.articleDetail.created_at).toLocaleDateString() }}</p>
      <button v-if="store.articleDetail.nickname === store.userInfo.nickname" @click="goEdit" class="btn update btn-primary mt-3">수정하기</button>
    </div>

    <div class="comments-section card p-4 shadow-sm">
      <h3 class="card-title">댓글</h3>
      <div v-for="comment in store.articleDetail.comments" :key="comment.id" class="comment mb-3 p-2 border-bottom">
        <p class="mb-1">{{ comment.content }}</p>
        <p class="text-muted mb-0">작성자: {{ comment.nickname }}</p>
        <p class="text-muted">{{ new Date(comment.created_at).toLocaleDateString() }}</p>
        <div v-if="comment.nickname === store.userInfo.nickname" class="d-flex justify-content-end">
          <button @click="editComment(comment)" class="btn btn-sm btn-secondary mr-2">수정</button>
          <button @click="deleteComment(comment.id)" class="btn btn-sm btn-danger">삭제</button>
        </div>
      </div>

      <div class="comment-form mt-4">
        <textarea v-model="newComment" placeholder="댓글을 입력하세요" class="form-control mb-2"></textarea>
        <button @click="addComment" class="btn btn-primary">댓글 작성</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const store = useProjectStore();
const route = useRoute();

const article_id = route.params.id;
const newComment = ref('');

const addComment = () => {
  if (store.isLogin === false) {
    alert('로그인이 필요합니다.');
    router.push({ name: 'login' });
    return;
  } else {
    if (newComment.value.trim() === '') {
      alert('댓글 내용을 입력해주세요.');
      return;
    }

    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/articles/${article_id}/comment-create/`,
      data: {
        content: newComment.value,
      },
      headers: {
        Authorization: `Token ${store.token}`,
      },
    })
      .then((res) => {
        store.getArticle(article_id);
        newComment.value = '';
      })
      .catch((err) => {
        console.error(err);
      });
  }
};

const editComment = (comment) => {
  // 댓글 수정 기능 구현
};

const deleteComment = (commentId) => {
  // 댓글 삭제 기능 구현
};

const goEdit = () => {
  // 수정 페이지로 이동
  router.push({ name: 'editArticle', params: { id: article_id } });
};

onMounted(() => {
  store.getArticle(article_id);
});
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: auto;
}

.article-detail {
  min-width: 650px;
}

.card-title {
  font-size: 1.5rem;
  font-weight: bold;
}

.card-text {
  font-size: 1.1rem;
  margin-bottom: 1rem;
}

.comment {
  padding: 0.5rem 0;
}

.comment-form textarea {
  resize: none;
}

.content {
  min-height: 200px;
}

.update {
  width: 100px;
  margin-left: auto;
}

.btn-sm {
  margin-right: 0.5rem;
}
</style>
