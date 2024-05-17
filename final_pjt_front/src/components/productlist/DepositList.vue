<template>
  <div>
    <v-data-table
      :headers="headers"
      :items="store.productListDR"
      :search="search"
      hide-actions
      class="elevation-1"
    >

      <template v-slot:items="props">
        <td>{{ props.item.productname }}</td>
        <td class="text-xs-right">{{ props.item.bankname }}</td>
        <td class="text-xs-right">{{ props.item['6'] }}</td>
        <td class="text-xs-right">{{ props.item['12']}}</td>
        <td class="text-xs-right">{{ props.item['24']}}</td>
        <td class="text-xs-right">{{ props.item['36']}}</td>
      </template>
    </v-data-table>
 

  </div>
</template>

<script setup>
  import { ref, onMounted, computed ,onBeforeMount} from 'vue';
  import {useProjectStore} from '@/stores/project'
  const store=useProjectStore()
  onMounted(()=>{
      store.getProductListD()
  })
  const search = ref('');
 
  const headers = [
          {
            text: '상품명',
            align: 'left',
            sortable: false,
            value: 'productname'
          },
          { text: '금융회사명', value: 'bankname' },
          { text: '6개월', value: '6' },
          { text: '12개월', value: '12' },
          { text: '24개월', value: '24' },
          { text: '36개월', value: '36' }
        ]
</script>

<style scoped>
  .PL-container{
      width: 960px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: space-around;
      min-width: 395px;
  }
</style>