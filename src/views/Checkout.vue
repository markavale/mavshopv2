<template>
  <div>
    <!-- <div style="z-index: 10000">
      <v-app-bar color="#ffffff" id="nav__header">
        <router-link
          style="text-decoration: none"
          class="d-flex"
          :to="{ name: 'index' }"
        >
          <div class="brand-logo-container">
            <v-img src="@/assets/img/logo.png" class="brand-logo"></v-img>
          </div>
          <v-toolbar-title class="headline my-auto">eMav</v-toolbar-title>
        </router-link>
        <v-spacer></v-spacer>
        <div class="green--text nav-link">
          <v-icon color="green">mdi-shield-check</v-icon>
          Secure Checkout
        </div>
      </v-app-bar>
    </div> -->
    <v-stepper v-model="step" alt-labels non-linear>
      <v-stepper-header style="font-size: 1rem; height: auto; padding: 0px">
        <v-row dense class="px-3">
          <v-col cols="12" sm="12" md="6" lg="6" xl="6" class="d-flex my-auto">
            <router-link
              style="text-decoration: none"
              class="d-flex"
              :to="{ name: 'index' }"
            >
              <div class="brand-logo-container">
                <v-img
                  src="@/assets/img/logo.png"
                  class="brand-logo"
                  style="height: 50px; width: 50px"
                ></v-img>
              </div>
              <v-toolbar-title class="headline my-auto"
                >Get Design</v-toolbar-title
              >
            </router-link>
            <span style="color: grey; font-weight: 400" class="my-auto ml-4"
              >|</span
            >
            <div class="green--text nav-link my-auto">
              <v-icon color="green">mdi-shield-check</v-icon>
              Secure Checkout
            </div>
          </v-col>
          <v-col
            cols="12"
            sm="12"
            md="6"
            lg="6"
            xl="6"
            class="d-flex pa-0 my-auto"
            style="font-size: 0.8rem height:auto;"
            
          >
            <v-stepper-step :complete="step > 1" step="1" style="font-size: 0.8rem">
              <div class="d-flex">
                <v-icon small>mdi-cart</v-icon>
                Shopping Cart
              </div>
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step :complete="step > 2" step="2" style="font-size: 0.8rem" 
              ><div class="d-flex">
                <v-icon small>mdi-file-document-box</v-icon>
                Place order
              </div></v-stepper-step
            >
            <v-divider></v-divider>
            <v-stepper-step :complete="step > 3" step="3" style="font-size: 0.8rem"
              ><div class="d-flex">
                <v-icon small>mdi-credit-card-multiple</v-icon>
                Payment
              </div></v-stepper-step
            >
            <v-divider></v-divider>
            <v-stepper-step step="4" style="font-size: 0.8rem"
              ><div class="d-flex">
                <v-icon small>mdi-briefcase-check</v-icon>
                Order complete
              </div></v-stepper-step
            >
          </v-col>
        </v-row>
      </v-stepper-header>
      <v-stepper-items>
        <v-stepper-content step="1"> </v-stepper-content>
        <v-stepper-content step="2">
          <v-row flat>
            <v-col cols="12" xs="12" sm="12" md="8" lg="8">
              <AddressForm />
            </v-col>
            <v-col
              class="sticky__scroll"
              cols="12"
              xs="12"
              sm="12"
              md="4"
              lg="4"
            >
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
                </v-list>
                <TotalBreakdown :orders="getOrders" />
              </v-card>
              <v-btn class="primary my-3" large block> Place Order </v-btn>
            </v-col>
          </v-row>
        </v-stepper-content>

        <v-stepper-content step="3">
          <v-card class="mb-12" color="grey lighten-1" height="200px"></v-card>
          <v-btn color="primary" @click="step = 4"> Continue </v-btn>
          <v-btn @click="step = 2">Back</v-btn>
        </v-stepper-content>
        <v-stepper-content step="4">
          <v-card class="mb-12" color="grey lighten-1" height="200px"></v-card>
          <v-btn color="primary" @click="step = 1"> Continue </v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script>
import TotalBreakdown from "@/components/layout/order-summary/TotalBreakdown";
import AddressForm from "@/components/layout/checkout/AddressForm";
import { mapGetters } from "vuex";
export default {
  name: "",
  data() {
    return {
      step: 2,
    };
  },
  components: {
    TotalBreakdown,
    AddressForm, 
  },
  mounted() {
    this.mountOrderItems();
    this.checkPageValidity();
  },
  computed: {
    ...mapGetters(["getOrders", "getOrderItems"]),
  },
  methods: {
    mountOrderItems() {
      this.$store.dispatch("fetchOrders");
      this.$store.dispatch("fetchOrderItems");
    },
    checkPageValidity() {
      if (
        this.getOrderItems.some((order_item) => order_item.is_selected === true)
      ) {
        console.log("Valid Page");
      } else {
        console.log("not valid!! no active order item");
      }
    },
  },
};
</script>

<style>
</style>