<template>
  <div class="order__summary">
    <CartNavbar />
    <v-container fluid>
      <v-stepper v-model="step" alt-labels non-linear>
        <v-stepper-header>
          <v-stepper-step :complete="step > 1" step="1">
            <!-- <div class="d-flex"> -->
            <!-- <v-icon small>mdi-cart</v-icon> -->
            Shopping Cart
            <!-- </div> -->
          </v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step :complete="step > 2" step="2"
            >Place order</v-stepper-step
          >

          <v-divider></v-divider>

          <v-stepper-step :complete="step > 3" step="3">Payment</v-stepper-step>

          <v-divider></v-divider>

          <v-stepper-step step="4">Order complete</v-stepper-step>
        </v-stepper-header>
        <v-stepper-items>
          <v-stepper-content step="1">
            <!-- <v-card class="mb-6" color="" height="auto"> -->
            <v-row flat>
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

            <v-btn color="primary" @click="step = 2"> Continue </v-btn>

            <!-- <v-btn text>Cancel</v-btn> -->
          </v-stepper-content>

          <v-stepper-content step="2">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>

            <v-btn color="primary" @click="step = 3"> Continue </v-btn>

            <v-btn @click="step = 1">Back</v-btn>
          </v-stepper-content>

          <v-stepper-content step="3">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>

            <v-btn color="primary" @click="step = 4"> Continue </v-btn>

            <v-btn @click="step = 2">Back</v-btn>
          </v-stepper-content>

          <v-stepper-content step="4">
            <v-card
              class="mb-12"
              color="grey lighten-1"
              height="200px"
            ></v-card>

            <v-btn color="primary" @click="step = 1"> Continue </v-btn>

            <!-- <v-btn text>Cancel</v-btn> -->
          </v-stepper-content>
        </v-stepper-items>
      </v-stepper>
    </v-container>
  </div>
</template>

<script>
// import { mapGetters } from "vuex"
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