<template>
  <div class="container my-4 d-flex flex-column align-items-center">
    <div class="article-detail card mb-4 p-4 shadow-sm">
      <div v-if="!editArticleMode">
        <h2 class="card-title mb-5">{{ store.articleDetail.title }}</h2>
        <p class="card-text content">{{ store.articleDetail.content }}</p>
      </div>
      <div v-else>
        <input v-model="articleTitle" class="form-control mb-3" />
        <textarea v-model="articleContent" class="form-control mb-3" rows="5"></textarea>
      </div>
      <p class="text-muted">작성자: {{ store.articleDetail.nickname }}</p>
      <p class="text-muted">작성일: {{ new Date(store.articleDetail.created_at).toLocaleDateString() }}</p>
      <div class="d-flex flex">
        <button v-if="store.articleDetail.nickname === store.userInfo.nickname && !editArticleMode" @click="editArticle" class="btn update btn-secondary mt-3">수정하기</button>
        <button v-if="store.articleDetail.nickname === store.userInfo.nickname && !editArticleMode" @click="goDelete" class="btn delete btn-danger mt-3">삭제하기</button>
        <button v-if="editArticleMode" @click="saveArticle" class="btn btn-primary mt-3">저장</button>
        <button v-if="editArticleMode" @click="cancelEditArticle" class="btn btn-secondary mt-3">취소</button>
      </div>
    </div>

    <div class="comments-section card p-4 shadow-sm">
      <h3 class="card-title">댓글</h3>
      <div v-for="comment in store.articleDetail.comments" :key="comment.id" class="comment mb-3 p-2 border-bottom d-flex justify-content-between">
        <div>
          <p v-if="!editMode[comment.id]" class="mb-1 comment-content">{{ comment.content }}</p>
          <input v-else v-model="comment.content" class="form-control mb-1" />
          <p class="text-muted mb-0">작성자: {{ comment.nickname }}</p>
          <p class="text-muted">{{ new Date(comment.created_at).toLocaleDateString() }}</p>
        </div>
        <div v-if="comment.nickname === store.userInfo.nickname" class="d-flex justify-content-end">
          <button v-if="!editMode[comment.id]" @click="editComment(comment)" class="btn btn-sm btn-secondary comment-btn mr-2">수정</button>
          <button v-else @click="saveComment(comment)" class="btn btn-sm btn-primary comment-btn mr-2">저장</button>
          <button @click="deleteComment(comment.id)" class="btn btn-sm btn-danger comment-btn">삭제</button>
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
import { ref, reactive, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const router = useRouter();
const store = useProjectStore();
const route = useRoute();

const article_id = route.params.id;
const newComment = ref('');
const editMode = reactive({});  // To manage edit mode for each comment
const editArticleMode = ref(false);  // To manage article edit mode
const articleTitle = ref('');
const articleContent = ref('');

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
  // Enter edit mode for comment
  editMode[comment.id] = true;
};

const saveComment = (comment) => {
  // Save edited comment
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/articles/${article_id}/comment-update/${comment.id}/`,
    data: {
      content: comment.content,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      store.getArticle(article_id);
      editMode[comment.id] = false;  // Exit edit mode
    })
    .catch((err) => {
      console.error(err);
    });
};

const deleteComment = (commentId) => {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/articles/${article_id}/comment-delete/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  }).then((res) => {
    store.getArticle(article_id);
  });
};

const editArticle = () => {
  // Enter article edit mode
  editArticleMode.value = true;
  articleTitle.value = store.articleDetail.title;
  articleContent.value = store.articleDetail.content;
};

const saveArticle = () => {
  // Save edited article
  axios({
    method: 'put',
    url: `http://127.0.0.1:8000/articles/${article_id}/update/`,
    data: {
      title: articleTitle.value,
      content: articleContent.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      store.getArticle(article_id);
      editArticleMode.value = false;  // Exit edit mode
    })
    .catch((err) => {
      console.error(err);
    });
};

const cancelEditArticle = () => {
  // Cancel article edit mode
  editArticleMode.value = false;
};

const goDelete = () => {
  axios({
    method: 'delete',
    url: `http://127.0.0.1:8000/articles/${article_id}/delete/`,
    headers: {
      Authorization: `Token ${store.token}`,
    }
  })
    .then((res) => {
      router.push({ name: 'articlelist' });
    })
    .catch((err) => {
      console.error(err);
    });
};

onMounted(() => {
  store.getArticle(article_id);
});
</script>

<style scoped>
.container {
  max-width: 950px;
  margin: auto;
}

.article-detail {
  width: 100%;
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

.delete {
  width: 100px;
  margin-left: auto;
}

.update {
  width: 100px;
  margin-right: auto;
}

.btn-sm {
  margin-right: 0.5rem;
}

.comment-btn {
  height: 30px;
}

.comment-content {
  max-width: 600px;
}

.comments-section {
  width: 100%;
}
</style>

