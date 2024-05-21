<template>
    <div class="container mt-5">
      <div class="card shadow-sm">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">로그인</h2>
          <form @submit.prevent="login">
            
            <div :class="['form-group', { 'has-error': !valid.username && submitted }]">
              <label for="username">아이디</label>
              <input type="text" class="form-control" id="username" v-model.trim="username" required>
            </div>
  
            <div :class="['form-group', { 'has-error': !valid.password && submitted }]">
              <label for="password">비밀번호</label>
              <input type="password" class="form-control" id="password" v-model.trim="password" autoComplete="off" required>
            </div>
  
            <button type="submit" class="btn btn-primary btn-block mt-4">로그인</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { ref, computed } from 'vue';
  import { useProjectStore } from '@/stores/project';
  import { useRouter } from 'vue-router';

    const router = useRouter();

  const store = useProjectStore();
  
  const username = ref('');
  const password = ref('');
  const submitted = ref(false);
  
  const valid = computed(() => {
    return {
      username: username.value.length > 0,
      password: password.value.length > 0,
    };
  });
  
  function login() {
    submitted.value = true;
    if (Object.values(valid.value).every(Boolean)) {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/login/',
        data: {
            id_name: username.value,
          password: password.value,
        },
      })
        .then((res) => {
          console.log(res.data);
          store.token = res.data.token;
          store.userInfo={
            nickname: res.data.nickname,
            email: res.data.email,
            id_name: res.data.id_name,
            birth: res.data.birth,
            sex: res.data.sex,
            main_bank: res.data.main_bank,
            salary: res.data.salary,
            asset: res.data.asset,
            desired_asset: res.data.desired_asset,
          }
          console.log('로그인 성공!');
          router.push('/');
        })
        .catch((err) => {
          alert('로그인 실패! 다시 시도해주세요.');
        });
    } else {
      alert('로그인 정보를 확인해주세요.');
    }
  }
  
  </script>
  
  <style scoped>
  .container {
    max-width: 400px;
  }
  
  .has-error input {
    border-color: red;
  }
  </style>