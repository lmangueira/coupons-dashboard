<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat dense round icon="menu" aria-label="Menu" @click="leftDrawerOpen = !leftDrawerOpen" />

        <q-toolbar-title> Coupons Dashboard App </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above elevated>
      <RetailersList @selected-retailer="selectedRetailer"/>
    </q-drawer>

    <q-page-container>
      <q-page padding>

        <q-tabs v-model="coupon_tabs" dense class="bg-grey-2 text-grey-7" active-color="primary" indicator-color="primary" align="justify">
          <q-tab name="stats" label="Stats" />
          <q-tab name="coupons-table" label="Coupons" />
        </q-tabs>

        <q-tab-panels v-model="coupon_tabs" animated keep-alive>
          <q-tab-panel name="stats">
            <StatisticsDashboard :retailer="currentRetailer" />
          </q-tab-panel>

          <q-tab-panel name="coupons-table">
            <CouponsList :retailer="currentRetailer" />
          </q-tab-panel>

        </q-tab-panels>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'

import RetailersList from 'components/RetailersList.vue'
import CouponsList from 'components/CouponList.vue'
import StatisticsDashboard from 'components/StatisticsDashboard.vue'

const leftDrawerOpen = ref(true)

const currentRetailer = ref("All")
const selectedRetailer = async (retailer = null) => {
  currentRetailer.value = retailer;
}

const coupon_tabs = ref('stats');
defineExpose(coupon_tabs);

</script>
