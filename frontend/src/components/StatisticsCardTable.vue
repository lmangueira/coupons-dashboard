<script setup>
defineProps({
  stats_type: String,
  stats: Object,
})

</script>

<template>
  <q-card>
    <q-card-section>
      <div class="text-h6">Statistics for</div>
      <div class="text-h5">{{ stats_type }}</div>
    </q-card-section>
    <q-markup-table>
      <thead>
      <tr>
        <th>Concept</th>
        <th>Value</th>
      </tr>
      </thead>
      <tbody>
      <tr>
        <td class="text-bold">Count</td>
        <td>{{ stats['count'] }}</td>
      </tr>
      <tr>
        <td class="text-bold">Minimum</td>
        <td>{{ stats['min'] }}</td>
      </tr>
      <tr>
        <td class="text-bold">Max</td>
        <td>{{ stats['max'] }}</td>
      </tr>
      <tr>
        <td class="text-bold">Average</td>
        <td>{{ stats['avg'] }}</td>
      </tr>
      </tbody>
    </q-markup-table>
  </q-card>
</template>

<style scoped>

</style>
