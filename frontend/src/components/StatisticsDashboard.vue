<script setup>
import { ref, onMounted, watch } from 'vue';
import { GetStatistics } from 'src/api/api.js'

import StatisticsCardTable from "./StatisticsCardTable.vue";
import StatisticsCardResumeTable from "./StatisticsCardResumeTable.vue";
import StatisticsCardChart from 'components/StatisticsCardChart.vue'

const props = defineProps({
  retailer: String
})

watch(
  () => props.retailer,
  (newRetailer) => {
    fetchStats(newRetailer);
  }
)

const stats = ref([])
const stats_percent_off = ref([])
const stats_dollar_off = ref([])
const fetchStats = async (retailer = null) => {
  try {
    const response = await GetStatistics(retailer);
    stats.value = response.data;
    stats_percent_off.value = response.data['stats_by_type']['percent-off'];
    stats_dollar_off.value = response.data['stats_by_type']['dollar-off'];
  }
  catch (error) {
    console.error("Failed to fetch stats:", error);
  }
}

onMounted(async () => {
  await fetchStats();
})

</script>

<template>
  <div class="q-pa-md row items-start q-gutter-md">
    <q-card>
      <q-card-section></q-card-section>
        <div class="text-h6">Stats JSON Response</div>
        <div>{{ stats }}</div>
    </q-card>
  </div>

  <div class="q-pa-md row items-start q-gutter-md">

    <StatisticsCardResumeTable :retailer="retailer" :stats="stats" />

    <StatisticsCardTable stats_type="percent-off" :stats="stats_percent_off" />

    <StatisticsCardTable stats_type="dollar-off" :stats="stats_dollar_off" />

    <StatisticsCardChart :stats="stats" />

  </div>

</template>

<style scoped></style>
