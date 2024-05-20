<template>
  <div>
    ArticleDetailView 
    {{ data }}
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useProjectStore } from '@/stores/project';
import { useRouter,useRoute } from 'vue-router';

const router = useRouter();
const store = useProjectStore();
const route = useRoute();

const data=route.data;

</script>

<style scoped>

</style>