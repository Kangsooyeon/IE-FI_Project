<template>
    <div class="container mt-5">
      <div class="card shadow-sm">
        <div class="card-body">
          <h2 class="card-title text-center mb-4" @click="asd">회원가입</h2>
          <form @submit.prevent="register">
            
            <div :class="['form-group', { 'has-error': !valid.id_name && submitted }]">
              <label for="id_name">ID(아이디)</label>
              <input type="text" class="form-control" id="id_name" v-model.trim="id_name" maxlength="30" required>
            </div>
  
            <div :class="['form-group', { 'has-error': !valid.password && submitted }]">
              <label for="password">Password(비밀번호)</label>
              <input type="password" class="form-control" id="password" v-model.trim="password" required>
            </div>
  
            <div :class="['form-group', { 'has-error': !valid.password2 && submitted }]">
              <label for="password2">Confirm Password(비밀번호 확인)</label>
              <input type="password" class="form-control" id="password2" v-model.trim="password2" required>
            </div>
  
            <div :class="['form-group', { 'has-error': !valid.nickname && submitted }]">
              <label for="nickname">이름</label>
              <input type="text" class="form-control" id="nickname" v-model.trim="nickname" maxlength="30" required>
            </div>
  
            <div :class="['form-group', { 'has-error': !valid.email && submitted }]">
              <label for="email">Email(이메일)</label>
              <input type="email" class="form-control" id="email" v-model.trim="email" maxlength="30" required>
            </div>
  
            <div class="form-group">
              <label for="birth">생년월일(YYMMDD)</label>
              <input type="text" class="form-control" id="birth" v-model.trim="birth">
            </div>
  
            <div class="form-group">
              <label for="sex">성별</label>
              <select class="form-control" id="sex" v-model="sex">
                <option value="">▼ 성별을 선택해주세요</option>
                <option value="1">남자</option>
                <option value="2">여자</option>
              </select>
            </div>
  
            <div class="form-group">
              <label for="main_bank">주거래계좌</label>
              <select class="form-control" id="main_bank" v-model="main_bank">
                <option value="">▼ 은행을 선택해주세요</option>
                <option v-for="bank1 in store.banks" :key="bank1">{{ bank1 }}</option>
              </select>
            </div>
  
            <div class="form-group">
              <label for="salary">연봉(만원)</label>
              <input type="text" class="form-control" id="salary" v-model.trim="salary">
            </div>
  
            <div class="form-group">
              <label for="asset">자산(만원)</label>
              <input type="text" class="form-control" id="asset" v-model.trim="asset">
            </div>
  
            <div class="form-group">
              <label for="desired_asset">희망자산(만원)</label>
              <input type="text" class="form-control" id="desired_asset" v-model.trim="desired_asset">
            </div>
  
            <button type="submit" class="btn btn-primary btn-block mt-4">가입하기</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import { useProjectStore } from '@/stores/project';
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  
  const router = useRouter();
  const store = useProjectStore();
  
  const id_name = ref('');
  const password = ref('');
  const password2 = ref('');
  const nickname = ref('');
  const email = ref('');
  const birth = ref('');
  const sex = ref('');
  const main_bank = ref('');
  const salary = ref('');
  const asset = ref('');
  const desired_asset = ref('');

  const submitted = ref(false);
  
  const valid = computed(() => {
    return {
      id_name: id_name.value.length > 0,
      password: password.value.length > 0,
      password2: password2.value === password.value && password2.value.length > 0,
      nickname: nickname.value.length > 0,
      email: /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value),
    };
  });
  
  function register() {
    submitted.value = true;
    if (Object.values(valid.value).every(Boolean)) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/accounts/signup/',
            data: {
                id_name: id_name.value,
                password: password.value,
                password2: password2.value,
                nickname: nickname.value,
                email: email.value,
                birth: birth.value,
                sex: parseInt(sex.value),
                main_bank: main_bank.value,
                salary: parseInt(salary.value),
                asset: parseInt(asset.value),
                desired_asset: parseInt(desired_asset.value)
            }
        }).then((response) => {
            alert('회원가입이 완료되었습니다.');
            router.push({ name: 'login' });
        }).catch((error) => {
            alert('회원정보를 올바르게 입력해주세요.');
        });


      console.log('Form submitted', {
        id_name: id_name.value,
        password: password.value,
        nickname: nickname.value,
        email: email.value,
        birth: birth.value,
        sex: parseInt(sex.value),
        main_bank: main_bank.value,
        salary: parseInt(salary.value),
        asset: parseInt(asset.value),
        desired_asset: parseInt(desired_asset.value)
      });
      // Add your form submission logic here
    } else {
      alert('회원정보를 올바르게 입력해주세요.')
    }
  }
  </script>
  
  <style scoped>
  .container {
    max-width: 600px;
  }
  
  .has-error input, .has-error select {
    border-color: red;
  }
  </style>
  