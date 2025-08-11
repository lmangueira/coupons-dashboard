<script setup>
import { ref, onMounted, watch } from 'vue'
import { GetCoupons } from 'src/api/api.js'

const props = defineProps({
  retailer: String,
})

watch(
  () => props.retailer,
  (newRetailer) => {
    fetchCoupons(newRetailer)
  },
)

const coupons = ref([])
const fetchCoupons = async (retailer = null) => {
  try {
    const response = await GetCoupons(retailer)
    coupons.value = response.data
  } catch (error) {
    console.error('Failed to fetch coupons:', error)
  }
}

onMounted(async () => {
  await fetchCoupons()
})

const columns = [
  // { name: 'id', label: 'ID', field: 'id', align: 'left', sortable: true },
  { name: 'coupon_id', label: 'Coupon ID', field: 'coupon_id', align: 'left', sortable: true },
  {
    name: 'coupon_webshop_name',
    label: 'Retailer',
    field: 'coupon_webshop_name',
    align: 'left',
    sortable: true,
  },
  // { name: 'description', label: 'Description', field: 'description', align: 'left', sortable: false },
  { name: 'title', label: 'Title', field: 'title', align: 'left', sortable: true },
  { name: 'first_seen', label: 'First Seen', field: 'first_seen', align: 'left', sortable: true },
  { name: 'last_seen', label: 'Last Seen', field: 'last_seen', align: 'left', sortable: true },
  {
    name: 'promotion_type',
    label: 'Promotion Type',
    field: 'promotion_type',
    align: 'left',
    sortable: true,
  },
  { name: 'webshop_id', label: 'WebShop ID', field: 'webshop_id', align: 'left', sortable: true },
]
</script>

<template>
  <q-table
    :rows="coupons"
    :columns="columns"
    bordered
    dense
    flat
    virtual-scroll
    :rows-per-page-options="[25, 50, 100, 0]"
    :fullscreen="false"
    title="Coupons"
  />
</template>

<style scoped></style>
