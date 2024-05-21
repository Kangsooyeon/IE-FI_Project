<template>
    <div class="main-container">
      <div class="row mb-3 upcard">
        <div class="col my-3">
          <TRProduct />
        </div>
        <div class="col my-3">
          <ERGraph />
        </div>
      </div>
      <div class="row">
        <div class="col-12 d-flex flex-row justify-content-center">
          <News />
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import TRProduct from '@/components/mainpage/maincard/TRProduct.vue';
  import ERGraph from '@/components/mainpage/maincard/ERGraph.vue';
  import News from '@/components/mainpage/maincard/News.vue';
  </script>
  
  <style scoped>
  .main-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 20px;
    width: 90%;
    margin: auto;
  }
  
  .row {
    display: flex;
    width: 100%;
    justify-content: space-around;
    margin-bottom: 20px;
  }
  
  .col {
    display: flex;
    justify-content: center;
  }
  
  .col-12 {
    width: 100%;
  }
  
  .upcard {
    width: 980px;
  }
  
  @media (min-width: 920px) {
    .upcard {
      flex-direction: row;
    }
  }
  
  @media (max-width: 920px) {
    .upcard {
      flex-direction: column;
      align-items: center;
    }
  }
  </style>
  