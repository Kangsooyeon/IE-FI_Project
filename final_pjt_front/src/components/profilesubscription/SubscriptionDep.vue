<template>
    <div class="subscription-container">
      <div class="content-wrapper">
        <div class="chart-container">
          <h3>예금 그래프( 예상수입 | 금리 )</h3>
          <canvas id="depositChart"></canvas>
        </div>
        <div class="list-container">
          <h3>예금 리스트(가입금액)</h3>
          <ul class="list-group">
            <li v-for="item in store.sub_prdt_dep" :key="item.id" class="list-group-item">
              <input type="checkbox" :value="item" v-model="selectedItems" :disabled="isDisabled(item)">
              {{item.id}} - {{ item.deposit_product.fin_prdt_nm }}: {{ item.sign_money }}원 
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, watch, onMounted } from 'vue';
  import { useProjectStore } from '@/stores/project';
  import { Chart, registerables } from 'chart.js';
  
  Chart.register(...registerables);
  
  const store = useProjectStore();
  const selectedItems = ref([]);
  let chartInstance = null;
  
  const isDisabled = (item) => {
    return selectedItems.value.length >= 5 && !selectedItems.value.includes(item);
  };
  
  const renderDepositChart = () => {
    const ctx = document.getElementById('depositChart').getContext('2d');
    if (chartInstance) {
      chartInstance.destroy();
    }
    chartInstance = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: selectedItems.value.map(item => item.id),
        datasets: [{
          label: '예상 수입금',
          data: selectedItems.value.map(item => item.mtrt_money - item.sign_money),
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          yAxisID: 'y',
        },{
          label: '금리',
          data: selectedItems.value.map(item => item.deposit_option.intr_rate2),
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
  };
  
  watch(selectedItems, () => {
    renderDepositChart();
  });
  
  onMounted(() => {
    renderDepositChart();
  });
  </script>
  
  <style scoped>
  .subscription-container {
    width: 100%;
    display: flex;
    justify-content: center;
    padding: 20px;
    box-sizing: border-box;
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
  