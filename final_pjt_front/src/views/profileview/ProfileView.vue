<template>
    <div class="profile-container d-flex">
      <div class="profile-sidebar bg-light p-4 text-center">
        <img src="@/assets/profile/cow.png" alt="Profile Image" class="img-fluid rounded-circle mb-5" />
        <h4>{{ store.userInfo.nickname }}</h4>
        <p>{{ store.userInfo.email }}</p>
        <ul class="navbar-nav mt-5">
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'profile' }">회원정보</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'subscriptionproduct' }">가입상품</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" :to="{ name: 'recommendproduct' }">추천상품</RouterLink>
          </li>
        </ul>
      </div>
      <RouterView />
    </div>
  </template>
  
  <script setup>
  import { RouterLink, RouterView } from 'vue-router';
  import { ref } from 'vue';
  import { useProjectStore } from '@/stores/project';

  const store = useProjectStore();
  </script>
  
  <style scoped>
  .profile-container {
    display: flex;
    max-width: 960px;
    margin: 0 auto;
  }
  
  .profile-sidebar {
    height: 1000px;
    width: 300px;
    background-color: #f8f9fa;
  }
  
  .profile-sidebar img {
    width: 150px;
    height: 150px;
  }
  
  .profile-sidebar ul {
    padding: 0;
    list-style: none;
  }
  
  .profile-sidebar ul li {
    margin: 10px 0;
    font-weight: bold;
  }
  
  .nav-link {
    color: inherit;
    text-decoration: none;
  }
  
  .nav-link.active {
    color: #007bff;
  }
  </style>
  