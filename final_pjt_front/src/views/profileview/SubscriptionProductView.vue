<template>
  <div class="subscription-container">
    <div class="d-flex justify-content-center mb-4">
      <button @click="showDeposit" :class="{'btn-primary': isDeposit, 'btn-secondary': !isDeposit}" class="btn mx-2">예금</button>
      <button @click="showSaving" :class="{'btn-primary': !isDeposit, 'btn-secondary': isDeposit}" class="btn mx-2">적금</button>
    </div>

    <div :class="{'display': !isDeposit}">
      <div class="d-flex flex-column justify-content-between align-items-center">
        <div class="chart-container">
          <h3>예금 그래프</h3>
          <canvas id="depositChart"></canvas>
        </div>
        <div class="list-container">
          <h3>예금 리스트</h3>
          <ul class="list-group">
            <li v-for="item in store.sub_prdt_dep" :key="item.id" class="list-group-item">
              {{ item.deposit_product.fin_prdt_nm }}: {{ item.sign_money }}원 
            </li>
          </ul>
        </div>
      </div>
    </div>

    <div :class="{'display':isDeposit}">
      <div class="d-flex flex-column justify-content-between align-items-center">
        <div class="chart-container">
          <h3>적금 그래프</h3>
          <canvas id="savingChart"></canvas>
        </div>
        <div class="list-container">
          <h3>적금 리스트</h3>
          <ul class="list-group">
            <li v-for="item in store.sub_prdt_sav" :key="item.id" class="list-group-item">
              {{ item.saving_product.fin_prdt_nm }}: {{ item.sign_money }}원
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useProjectStore } from '@/stores/project';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const store = useProjectStore();
const isDeposit = ref(true);

const showDeposit = () => {
  isDeposit.value = true;
  renderDepositChart();
};

const showSaving = () => {
  isDeposit.value = false;
  renderSavingChart();
};

const renderDepositChart = () => {
  const ctx = document.getElementById('depositChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: store.sub_prdt_dep.map(item => item.deposit_product.fin_prdt_nm),
      datasets: [{
        label: '예금 금액',
        data: store.sub_prdt_dep.map(item => item.sign_money),
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
};

const renderSavingChart = () => {
  const ctx = document.getElementById('savingChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels: store.sub_prdt_sav.map(item => item.saving_product.fin_prdt_nm),
      datasets: [{
        label: '적금 금액',
        data: store.sub_prdt_sav.map(item => item.sign_money),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
};

onMounted(() => {
  if (isDeposit.value) {
    renderDepositChart();
  } else {
    renderSavingChart();
  }
});

watch(isDeposit, (newValue) => {
  if (newValue) {
    renderDepositChart();
  } else {
    renderSavingChart();
  }
});
</script>
<style scoped>
.subscription-container {
  width: 80%;
}

.chart-container {
  width: 100%;
  height: 400px;
}

canvas {
  width: 100% !important;
  height: 400px !important;
}

.list-container {
  width: 100%;
}

.list-group-item {
  font-size: 1.2rem;
}

button {
  width: 100px;
}
.display {
  display: none;
}
</style>
