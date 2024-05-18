<template>
  <div>
    <select @change="changed($event)">
      <option value="" selected>{{ title }}</option>
      <option v-for="region in regionList" :key="region">
        {{ region }}
      </option>
    </select>
  </div>
</template>

<script setup>
defineProps({
  changed: {
    type: Function,
    required: true,
  },
  regionList: {
    type: Array,
    required: true,
  },
  title: {
    type: String,
    required: true,
  },
});
</script>

<style scoped></style>
