<template>
  <div class="order__summary">
    <CartNavbar />
    <!-- <v-container fluid> -->
      <v-stepper v-model="step" alt-labels non-linear class="mt-3">
        <v-stepper-header style="font-size: 0.8rem height:auto; padding:0px;">
          <v-stepper-step
            :complete="step > 1"
            step="1"
            style="font-size: 0.8rem"
          >
            <div class="d-flex">
              <v-icon small>mdi-cart</v-icon>
              Shopping Cart
            </div>
          </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step
            :complete="step > 2"
            step="2"
            style="font-size: 0.8rem"
          >
            <div class="d-flex">
              <v-icon small>mdi-file-document-box</v-icon>
              Place order
            </div>
          </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step
            :complete="step > 3"
            step="3"
            style="font-size: 0.8rem"
          >
            <div class="d-flex">
              <v-icon small>mdi-credit-card-multiple</v-icon>
              Payment
            </div>
          </v-stepper-step>
          <v-divider></v-divider>
          <v-stepper-step step="4" style="font-size: 0.8rem">
            <div class="d-flex">
              <v-icon small>mdi-briefcase-check</v-icon>
              Order complete
            </div>
          </v-stepper-step>
        </v-stepper-header>
        <v-stepper-items>
          <v-stepper-content step="1">
            <v-row
            flat 
            justify="space-around"
            align="start"
            >
              <v-col cols="12" xs="12" sm="12" md="8" lg="8">
                <CartItems />
              </v-col>
              <v-col
                class="sticky__scroll"
                cols="12"
                xs="12"
                sm="12"
                md="4"
                lg="4"
              >
                 <Summary />
              </v-col>
            </v-row>
            <!-- </v-card> -->

            <!-- <v-btn color="primary" @click="step = 2"> Continue </v-btn> -->

            <!-- <v-btn text>Cancel</v-btn> -->
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    <!-- </v-container> -->
  </div>
</template>

<script>
import Summary from "@/components/layout/order-summary/Summary";
import CartNavbar from "@/components/layout/order-summary/CartNavbar";
import CartItems from "@/components/layout/order-summary/CartItems";
export default {
  name: "Order-Summary",
  data() {
    return {
      step: 1,
    };
  },
  props: {},
  components: {
    Summary,
    CartItems,
    CartNavbar,
  },
  mounted() {},
  computed: {},
  methods: {},
};
</script>

<style>
.order__summary {
  background-color: #ffffff;
}
.sticky__scroll {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
}
</style>