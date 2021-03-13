<template>
  <div>
    <v-card
      color="#f7f7f7"
      flat
      class="summary mx-auto pa-3"
      height="auto"
      max-width="100%"
    >
      <v-list flat subheader three-line color="#f7f7f7">
        <v-list-item-title class="font-weight-bold"
          >Order Summary</v-list-item-title
        >
        <v-list-item>
          <v-list-item-content class="ma-0 pa-0">
            <v-row>
              <v-col cols="12" class="d-flex ma-0">
                <v-radio-group :value="coupon_status">
                  <v-radio :value="true" @click.prevent="coupon_status_inverter_true(coupon_status)">
                    <template v-slot:label>
                      <div>Coupon</div>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-icon
                            class="ml-1"
                            color="grey"
                            dark
                            v-bind="attrs"
                            v-on="on"
                            small
                          >
                            mdi-help-circle
                          </v-icon>
                        </template>
                        <p class="text-caption">
                          1. Coupon can only use by registered user. <br />
                          2. You can use one coupon in one order. <br />
                          3. You can enter the coupon CODE or select the valid
                          coupon. <br />
                          4. Coupon can only be applicable if your total amount
                          is greater than the coupon discount.
                        </p>
                      </v-tooltip>
                    </template>
                  </v-radio>
                  <div class="d-flex ma-0 pa-0">
                    <v-autocomplete
                      :value="getActiveCoupon"
                      :disabled="isLoading"
                      :loading="isLoading"
                      :items="getCoupons"
                      :search-input.sync="search"
                      chips
                      solo
                      full-width
                      :success-messages="is_success ? `${message}` : ''"
                      color="blue-grey lighten-2"
                      label="Use Coupon"
                      item-text="name"
                      item-value="name"
                    >
                      <template v-slot:selection="data">
                        <v-chip
                          v-bind="data.attrs"
                          color="blue-grey"
                          class="white--text"
                          close
                          @click:close="removeCoupon()"
                        >
                          <v-icon left> mdi-sale </v-icon>
                          {{ data.item.code }}
                        </v-chip>
                      </template>
                      <template v-slot:item="data">
                        <div
                          class="d-flex"
                          style="width: 100%"
                          @click.prevent="applyCoupon(data.item)"
                        >
                          <v-list-item-content>
                            <v-list-item-title
                              v-html="data.item.code"
                            ></v-list-item-title>
                            <v-list-item-subtitle
                              v-html="data.item.amount"
                            ></v-list-item-subtitle>
                          </v-list-item-content>
                          <v-spacer></v-spacer>
                          <v-icon right> mdi-sale </v-icon>
                        </div>
                      </template>
                      <template v-slot:no-data>
                        <v-list-item>
                          <v-list-item-title>
                            No available coupon matching {{ search }}
                            <strong>{{ search }}</strong>
                          </v-list-item-title>
                        </v-list-item>
                      </template>
                    </v-autocomplete>
                  </div>
                  <v-radio
                    label="Don't use my discount"
                    :value="false"
                    @click.prevent="coupon_status_inverter_false(coupon_status)"
                  ></v-radio>
                </v-radio-group>
              </v-col>
            </v-row>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>
      <TotalBreakdown :orders="getOrders" />
      <!-- <v-list subheader three-line v-for="order in getOrders" :key="order.id">
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
          <v-chip class="my-auto" color="warning" text-color="white" small
          v-if="getActiveCoupon.amount > order.sub_total_selected_items"
          >
            <v-avatar left class="mr-2">
              <v-icon small>mdi-information-outline</v-icon>
            </v-avatar>
            Not applicable
          </v-chip>
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
      </v-list> -->
    </v-card>
    <v-btn class="primary my-3" large block @click="proceedCheckout()"> Proceed to checkout </v-btn>
    
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import TotalBreakdown from "@/components/layout/order-summary/TotalBreakdown"
export default {
  name: "",
  data() {
    return {
      settings: [],
      isLoading: false,
      coupon: [],
      search: null,
      is_success: false,
      message: "",
      item_total: 0,
    };
  },
  props: {},
  components: {
    TotalBreakdown,
  },
  mounted() {
    this.getAllOrders();
    this.mountCoupons();
    this.$store.dispatch('fetchOrderItems')

    console.log(this.coupon_status)
    // console.log(this.getOrders)
  },
  computed: {
    ...mapGetters(["getOrders", "getCoupons", "getActiveCoupon", "coupon_status", "getOrderItems"]),
    currentCoupon: {
      get() {
        return this.$store.state.activeCoupon;
      },
    },
    set(value) {
      this.$store.commit("setActiveCoupon", value);
      return value; //this.getActiveCoupon
    },
  },
  methods: {
    proceedCheckout(){
      if(this.getOrderItems.some(order_item => order_item.is_selected === true)){
        this.$router.push({name: 'checkout'})
      }
      else{
        alert(`You don't have an active order to proceed.`)
      }
      
    },
    removeCoupon() {
      this.isLoading = true;
      this.$store
        .dispatch("removeCoupon")
        .then(() => {
          this.is_succes = true;
          this.message = "Coupon was removed successfully";
        })
        .catch((err) => {
          this.is_success = false;
          console.log(err);
          console.log(err.message);
        })
        .finally(() => (this.isLoading = false));
    },
    applyCoupon(item) {
      console.log(item);
      this.isLoading = true;
      this.$store
        .dispatch("applyCoupon", item)
        .then(() => {
          this.is_success = true;
          this.message = "Coupon was applied successfully";
        })
        .catch((err) => {
          this.is_success = false;
          console.log(err.message);
          console.log(err);
        })
        .finally(() => (this.isLoading = false));
    },
    mountCoupons() {
      this.$store.dispatch("fetchCoupons");
    },
    getAllOrders() {
      this.$store.dispatch("fetchOrders");
      this.$store.dispatch("fetchCoupons");
    },
    coupon_status_inverter_true(payload){
      if(payload){
        console.log(payload)
      }
      else{
        console.log(!payload)
        this.$store.dispatch('invertUseCoupon', !payload)
      }
    },
    coupon_status_inverter_false(payload){
      if(payload){
        console.log(!payload)
        this.$store.dispatch('invertUseCoupon', !payload)
      }
      else{
        console.log(payload)
      }
    },
  },
};
</script>

<style>
</style>
