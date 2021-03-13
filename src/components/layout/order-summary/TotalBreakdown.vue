<template>
  <div>
      <v-list subheader three-line v-for="order in orders" :key="order.id">
        <div class="d-flex">
          <v-subheader class="subtitle-2 font-weight-regular">
            Subtotal:
          </v-subheader>
          <v-spacer></v-spacer>
          <v-subheader class="black--text font-weight-medium"
            >₱{{ order.sub_total_selected_items }}</v-subheader
          >
        </div>
        <v-divider
          class="mx-3 my-0 pa-0"
          style="border-style: dashed"
          v-if="order.coupon"
        ></v-divider>
        <div class="d-flex" v-if="order.coupon && coupon_status">
          <v-subheader class="subtitle-2 font-weight-regular">
            Coupon:
          </v-subheader>
          <v-spacer></v-spacer>
          <v-subheader class="black--text font-weight-medium"
            >-₱{{ order.coupon.amount }}</v-subheader
          >
        </div>

        <v-divider
          class="mx-3 my-0 pa-0"
          style="border-style: dashed"
        ></v-divider>
        <div class="d-flex">
          <v-subheader class="headline black--text font-weight-regular">
            Total:
          </v-subheader>
          <v-spacer></v-spacer>
          <v-subheader class="black--text text-h5 font-weight-bold"
            >₱{{ order.total }}</v-subheader
          >
        </div>
      </v-list>
  </div>
</template>

<script>
import { mapGetters } from "vuex"
export default {
    name: 'total-break-down',
    data(){
        return {}
    },
    props: {
      orders: Array,
    },
    mounted(){},
    computed: {
      ...mapGetters(['getActiveCoupon', 'getActiveCoupon', 'coupon_status', ])
    },
    methods: {},
}
</script>

<style>

</style>