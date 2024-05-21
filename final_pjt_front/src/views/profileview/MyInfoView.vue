<template>
  <div class="profile-details p-4">
    <table class="table table-bordered ms-auto me-auto mt-4">
      <tbody>
        <tr>
          <th scope="row">아이디</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.id_name }}</span>
            <input v-else v-model="editedUserInfo.id_name" type="text" class="form-control" disabled />
          </td>
        </tr>
        <tr>
          <th scope="row">E-mail</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.email }}</span>
            <input v-else v-model="editedUserInfo.email" type="email" class="form-control" />
            <span v-if="errors.email" class="text-danger">{{ errors.email }}</span>
          </td>
        </tr>
        <tr>
          <th scope="row">닉네임</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.nickname }}</span>
            <input v-else v-model="editedUserInfo.nickname" type="text" class="form-control" />
            <span v-if="errors.nickname" class="text-danger">{{ errors.nickname }}</span>
          </td>
        </tr>
        <tr>
          <th scope="row">생년월일(YYMMDD)</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.birth }}</span>
            <input v-else v-model="editedUserInfo.birth" type="text" class="form-control" />
            <span v-if="errors.birth" class="text-danger">{{ errors.birth }}</span>
          </td>
        </tr>
        <tr>
          <th scope="row">주거래은행</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.main_bank }}</span>
            <select v-else v-model="editedUserInfo.main_bank" class="form-select">
              <option v-for="bank in store.banks" :key="bank" :value="bank">{{ bank }}</option>
            </select>
            <span v-if="errors.main_bank" class="text-danger">{{ errors.main_bank }}</span>
          </td>
        </tr>
        <tr>
          <th scope="row">연봉</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.salary }}</span>
            <input v-else v-model="editedUserInfo.salary" type="text" class="form-control" />
            <span v-if="errors.salary" class="text-danger">{{ errors.salary }}</span>
          </td>
        </tr>
        <tr>
          <th scope="row">자산</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.asset }}</span>
            <input v-else v-model="editedUserInfo.asset" type="text" class="form-control" />
            <span v-if="errors.asset" class="text-danger">{{ errors.asset }}</span>
          </td>
        </tr>
        <tr>
          <th scope="row">희망자산</th>
          <td>
            <span v-if="!isEditing">{{ store.userInfo.desired_asset }}</span>
            <input v-else v-model="editedUserInfo.desired_asset" type="text" class="form-control" />
            <span v-if="errors.desired_asset" class="text-danger">{{ errors.desired_asset }}</span>
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
const errors = ref({});

const validate = () => {
  errors.value = {};
  let valid = true;

  if (!editedUserInfo.value.email) {
    errors.value.email = '이메일을 입력하세요';
    valid = false;
  } else if (!/\S+@\S+\.\S+/.test(editedUserInfo.value.email)) {
    errors.value.email = '유효한 이메일 주소를 입력하세요';
    valid = false;
  }

  if (!editedUserInfo.value.nickname) {
    errors.value.nickname = '닉네임을 입력하세요';
    valid = false;
  }

  if (!editedUserInfo.value.birth) {
    errors.value.birth = '생년월일을 입력하세요';
    valid = false;
  } else if (!/^\d{6}$/.test(editedUserInfo.value.birth)) {
    errors.value.birth = '유효한 생년월일(YYMMDD)을 입력하세요';
    valid = false;
  }

  if (editedUserInfo.value.salary && (isNaN(editedUserInfo.value.salary) || editedUserInfo.value.salary < 0)) {
    errors.value.salary = '유효한 연봉을 입력하세요';
    valid = false;
  }

  if (editedUserInfo.value.asset && (isNaN(editedUserInfo.value.asset) || editedUserInfo.value.asset < 0)) {
    errors.value.asset = '유효한 자산을 입력하세요';
    valid = false;
  }

  if (editedUserInfo.value.desired_asset && (isNaN(editedUserInfo.value.desired_asset) || editedUserInfo.value.desired_asset < 0)) {
    errors.value.desired_asset = '유효한 희망자산을 입력하세요';
    valid = false;
  }

  return valid;
};

const editProfile = () => {
  isEditing.value = true;
};

const saveProfile = () => {
  if (!validate()) return;

  axios({
    method: 'patch',
    url: 'http://127.0.0.1:8000/accounts/update/',
    data: {
      nickname: editedUserInfo.value.nickname,
      email: editedUserInfo.value.email,
      birth: editedUserInfo.value.birth,
      main_bank: editedUserInfo.value.main_bank,
      salary: editedUserInfo.value.salary,
      asset: editedUserInfo.value.asset,
      desired_asset: editedUserInfo.value.desired_asset,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((response) => {
      store.userInfo.nickname = editedUserInfo.value.nickname;
      store.userInfo.email = editedUserInfo.value.email;
      store.userInfo.birth = editedUserInfo.value.birth;
      store.userInfo.main_bank = editedUserInfo.value.main_bank;
      store.userInfo.salary = editedUserInfo.value.salary;
      store.userInfo.asset = editedUserInfo.value.asset;
      store.userInfo.desired_asset = editedUserInfo.value.desired_asset;

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
.text-danger {
  font-size: 0.8rem;
}
</style>
