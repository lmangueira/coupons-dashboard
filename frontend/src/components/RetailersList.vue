<script setup>
import { ref, onMounted } from 'vue';

import { GetRetailers } from '../api/api.js'

const retailers = ref([]);
const fetchRetailers = async () => {
  try {
    const response = await GetRetailers()
    retailers.value = response.data
    retailers.value.push('All')
  } catch (error){
    console.log("Failed to fetch retailers.", error)
  }
}

onMounted(() => {
  fetchRetailers();
})
</script>

<template>
  <q-list>
    <q-item-label header>Retailers</q-item-label>
    <q-item v-for="retailer in retailers" :key="retailer">
      <q-item-section>
        <q-btn color="white" text-color="black"
               @click="$emit('selectedRetailer', retailer)">{{ retailer}}</q-btn>
      </q-item-section>
    </q-item>
  </q-list>
</template>

<style scoped></style>
