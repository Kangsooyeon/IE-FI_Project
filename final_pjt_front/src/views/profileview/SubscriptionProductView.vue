<template>
  <div class="subscription-container">
    <div class="button-container">
      <button @click="showDeposit" :class="{ active: isDeposit }" :disabled="isDeposit">예금</button>
      <button @click="showSavings" :class="{ active: !isDeposit }" :disabled="!isDeposit">적금</button>
    </div>
    <div class="content-wrapper">
      <div class="chart-container">
        <h3 v-if="isDeposit">예금 그래프( 예상수입 | 금리 )</h3>
        <h3 v-else>적금 그래프( 예상수입 | 금리 )</h3>
        <canvas id="chart"></canvas>
      </div>
      <div class="list-container">
        <h3 v-if="isDeposit">예금 리스트(가입금액)</h3>
        <h3 v-else>적금 리스트(가입금액)</h3>
        <ul class="list-group">
          <li v-for="item in currentList" :key="item.id" class="list-group-item">
            <input type="checkbox" :value="item" v-model="selectedItems" :disabled="isDisabled(item)">
            {{ item.id }} - {{ item.deposit_product?.fin_prdt_nm }}{{ item?.saving_product?.fin_prdt_nm }}: {{ item.sign_money }}원 
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted,computed } from 'vue';
import { useProjectStore } from '@/stores/project';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

const store = useProjectStore();
const selectedItems = ref([]);
const isDeposit = ref(true);
let chartInstance = null;

const isDisabled = (item) => {
  return selectedItems.value.length >= 5 && !selectedItems.value.includes(item);
};

const showDeposit = () => {
  isDeposit.value = true;
  selectedItems.value = [];
  renderChart();
};

const showSavings = () => {
  isDeposit.value = false;
  selectedItems.value = [];
  renderChart();
};

const renderChart = () => {
  if(isDeposit.value){
    const ctx1 = document.getElementById('chart').getContext('2d');
  if (chartInstance) {
    chartInstance.destroy();
  }
  chartInstance = new Chart(ctx1, {
    type: 'bar',
    data: {
      labels: selectedItems.value.map(item => item.id),
      datasets: [{
        label: '예상 수입금',
        data: selectedItems.value.map((item) => item.mtrt_money - item.sign_money),
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        yAxisID: 'y',
      },{
        label: '금리',
        data: selectedItems.value.map((item) => {
          if(isDeposit.value){
            console.log(11);
            return item.deposit_option.intr_rate2
          }else{
            console.log(22);
            return item.saving_option.intr_rate2
          }
        }),
        backgroundColor: '#acc236',
        borderColor: '#acc236',
        yAxisID: 'y1',
      }]
    },
    options: {
      responsive: true,
      interaction: {
        mode: 'index',
        intersect: false,
      },
      stacked: false,
      plugins: {
        title: {
          display: true,
          text: 'IE-FI'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          type: 'linear',
          display: true,
          position: 'left',
        },
        y1: {
          beginAtZero: true,
          type: 'linear',
          display: true,
          position: 'right',
          grid: {
            drawOnChartArea: false, // only want the grid lines for one axis to show up
          }
        }
      }
    }
  });
  }
  else{
    const ctx2 = document.getElementById('chart').getContext('2d');
  if (chartInstance) {
    chartInstance.destroy();
  }
  chartInstance = new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: selectedItems.value.map(item => item.id),
      datasets: [{
        label: '예상 수입금',
        data: selectedItems.value.map((item) => item.mtrt_money - item.sign_money),
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        yAxisID: 'y',
      },{
        label: '금리',
        data: selectedItems.value.map((item) => {
          if(isDeposit.value){
            console.log(11);
            return item.deposit_option.intr_rate2
          }else{
            console.log(22);
            return item.saving_option.intr_rate2
          }
        }),
        backgroundColor: '#acc236',
        borderColor: '#acc236',
        yAxisID: 'y1',
      }]
    },
    options: {
      responsive: true,
      interaction: {
        mode: 'index',
        intersect: false,
      },
      stacked: false,
      plugins: {
        title: {
          display: true,
          text: 'IE-FI'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          type: 'linear',
          display: true,
          position: 'left',
        },
        y1: {
          beginAtZero: true,
          type: 'linear',
          display: true,
          position: 'right',
          grid: {
            drawOnChartArea: false, // only want the grid lines for one axis to show up
          }
        }
      }
    }
  });
  }
  
};

watch(selectedItems, () => {
  renderChart();
});

onMounted(() => {
  store.getSubPrdtDep();
  store.getSubPrdtSav();
  renderChart();
});

const currentList = computed(() => {
  return isDeposit.value ? store.sub_prdt_dep : store.sub_prdt_sav;
});
</script>

<style scoped>
.subscription-container {
  width: 660px;
  display: flex;
  flex-direction: column;
  justify-content: start;
  padding: 20px;
  box-sizing: border-box;
}

.button-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.button-container button {
  padding: 10px 20px;
  margin: 0 10px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button-container button.active {
  background-color: #0056b3;
}

.button-container button:hover:not(.active) {
  background-color: #0056b3;
}

.content-wrapper {
  width: 660px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.chart-container {
  width: 100%;
  height: 400px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  background-color: #fff;
}

.list-container {
  width: 100%;
  max-height: 400px;
  overflow-y: auto;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  background-color: #fff;
}

.list-group-item {
  font-size: 1.2rem;
  display: flex;
  align-items: center;
}

.list-group-item input[type="checkbox"] {
  margin-right: 10px;
}

h3 {
  margin-bottom: 20px;
  font-size: 1.5rem;
  color: #333;
  text-align: center;
}

canvas {
  width: 100%;
  height: 100%;
}
</style>
