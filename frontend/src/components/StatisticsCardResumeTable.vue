<script setup>
defineProps({
  retailer: String,
  stats: Object,
})

</script>

<template>
  <q-card>
    <q-card-section>
      <div class="text-h2">{{ stats['total_coupons'] }}</div>
      <q-separator class="q-ma-md" />
      <div class="text-h6">Total coupons for</div>
      <div class="text-h5">{{ retailer }}</div>

    </q-card-section>
  </q-card>
</template>

<style scoped>

</style>
