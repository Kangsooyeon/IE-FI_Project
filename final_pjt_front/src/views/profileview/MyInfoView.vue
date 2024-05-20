<template>
  <div class="profile-details p-4">
    <table class="table table-bordered ms-auto me-auto mt-4">
      <tbody>
        <tr>
          <th scope="row">아이디</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.id_name }}</span>
            <input v-else v-model="editedUserInfo.id_name" type="text" class="form-control" />
          </td>
        </tr>
        <tr>
          <th scope="row">E-mail</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.email }}</span>
            <input v-else v-model="editedUserInfo.email" type="email" class="form-control" />
          </td>
        </tr>
        <tr>
          <th scope="row">닉네임</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.nickname }}</span>
            <input v-else v-model="editedUserInfo.nickname" type="text" class="form-control" />
          </td>
        </tr>
        <tr>
          <th scope="row">생년월일(YYMMDD)</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.birth }}</span>
            <input v-else v-model="editedUserInfo.birth" type="text" class="form-control" />
          </td>
        </tr>
        <tr>
          <th scope="row">주거래은행</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.main_bank }}</span>
            <select v-else v-model="editedUserInfo.main_bank" class="form-select">
              <option v-for="bank in store.banks" :key="bank" :value="bank">{{ bank }}</option>
            </select>
          </td>
        </tr>
        <tr>
          <th scope="row">연봉</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.salary }}</span>
            <input v-else v-model="editedUserInfo.salary" type="text" class="form-control" />
          </td>
        </tr>
        <tr>
          <th scope="row">자산</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.asset }}</span>
            <input v-else v-model="editedUserInfo.asset" type="text" class="form-control" />
          </td>
        </tr>
        <tr>
          <th scope="row">희망자산</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.desired_asset }}</span>
            <input v-else v-model="editedUserInfo.desired_asset" type="text" class="form-control" />
          </td>
        </tr>
      </tbody>
    </table>
    <div class="text-end mt-3" style="width: 500px; margin-left: auto; margin-right: auto;">
      <button v-if="!isEditing" @click="editProfile" class="btn btn-primary float-end">프로필 수정하기</button>
      <button v-else @click="saveProfile" class="btn btn-primary float-end ms-2">저장</button>
      <button v-if="isEditing" @click="cancelEdit" class="btn btn-secondary float-end ms-2">취소</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useProjectStore } from '@/stores/project';
import axios from 'axios';

const store = useProjectStore();
const isEditing = ref(false);
const editedUserInfo = ref({ ...store.userInfo });

const editProfile = () => {
  isEditing.value = true;
};

const saveProfile = () => {
  axios({
    method: 'put',
    url: 'http://127.0.0.1:8000/accounts/update/',
    data: {"nickname": editedUserInfo.nickname,
  "email": editedUserInfo.email,
  "birth": editedUserInfo.birth,
  "main_bank": editedUserInfo.main_bank,
  "salary": editedUserInfo.salary,
  "asset": editedUserInfo.asset,
  "desired_asset": editedUserInfo.desired_asset},
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      store.userInfo = { ...editedUserInfo.value };
      isEditing.value = false;
    })
    .catch((error) => {
      console.error(error);
    });
};

const cancelEdit = () => {
  isEditing.value = false;
  editedUserInfo.value = { ...store.userInfo };
};
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

.profile-details {
  flex: 1;
  padding: 20px;
}

.table th,
.table td {
  vertical-align: middle;
}

.profile-sidebar ul {
  padding: 0;
  list-style: none;
}

.profile-sidebar ul li {
  margin: 10px 0;
  font-weight: bold;
}

table {
  width: 500px;
  border-radius: 10px;
}

th {
  width: 180px;
}

</style>
