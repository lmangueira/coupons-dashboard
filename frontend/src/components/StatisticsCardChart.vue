<script setup>
import { defineProps, computed } from 'vue'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js'
import { Doughnut } from 'vue-chartjs'

const props = defineProps({
  stats: {
    type: Object,
    required: false,
    default: () => ({}),
  }
})

const labels = computed(() =>
  Object.keys(props.stats?.stats_by_type || {})
)
const dataCounts = computed(() =>
  labels.value.map(key => props.stats?.stats_by_type?.[key]?.count ?? 0)
)

ChartJS.register(Title, Tooltip, Legend, ArcElement)

const backgroundColors = computed(() => {
  const baseColors = [
    'rgba(54, 162, 235, 0.5)',
    'rgba(255, 99, 132, 0.5)',
    'rgba(255, 206, 86, 0.5)',
    'rgba(75, 192, 192, 0.5)',
    'rgba(153, 102, 255, 0.5)',
    'rgba(255, 159, 64, 0.5)',
  ]

  return Array.from({ length: labels.value.length }, (_, i) => baseColors[i % baseColors.length])
})

const chartData = computed(() => ({
  labels: labels.value,
  datasets: [
    {
      label: 'Cantidad de cupones por tipo',
      data: dataCounts.value,
      backgroundColor: backgroundColors.value,
      borderColor: backgroundColors.value.map((c) => c.replace('0.5', '1')),
      borderWidth: 1,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'top' },
  },
}
</script>

<template>
  <q-card class="q-pa-lg">
    <q-card-section>
      <div class="text-h6">Coupon Types Distribution</div>
    </q-card-section>

    <div v-if="labels.length">
      <Doughnut :data="chartData" :options="chartOptions"  />
    </div>
    <div v-else class="text-center q-pa-xl text-grey-6">
      <q-icon name="pie_chart" size="3em" />
      <div>No coupon data to display</div>
    </div>
  </q-card>
</template>

<style scoped></style>
