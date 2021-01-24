<template>
  <div>
    <v-row class="cart__items__header" align="center" align-content="center">
      <v-col cols="1">
        <v-checkbox
          v-model="selectAll"
          color="primary"
          :value="selectAll"
          hide-details
          class="my-2 ml-3"
        ></v-checkbox>
      </v-col>
      <v-col cols="5"> Item </v-col>
      <v-col cols="3"> Unit Price </v-col>
      <v-col cols="3"> Subtotal </v-col>
    </v-row>
    <v-divider></v-divider>
    <div v-if="getOrderItems.length == 0">
      <h1>No data!!!</h1>
      <v-divider></v-divider>
    </div>
    <div v-else>
      <CartItem :orderItem="orderItem" :isSelected="selectAll" v-for="orderItem in getOrderItems" :key="orderItem.id" />
    </div>
    <v-btn rounded small text class="grey--text pa-0 ma-0">
      <v-icon> mdi-delete </v-icon>
      <span class="text-decoration-underline"> Delete selected items </span>
    </v-btn>
    <v-divider></v-divider>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import CartItem from "@/components/layout/order-summary/CartItem"
export default {
  name: "Cart-Items",
  data() {
    return {
      selectAll: true,
      selected: [],
    };
  },
  props: {},
  components: {
    CartItem,
  },
  mounted() {
    this.getCartItems();
    // this.getUserOrders();
  },
  computed: {
    ...mapGetters(["isAuthenticated", "getOrderItems",]),
  },
  methods: {
    getColor(calories) {
      if (calories > 400) return "red";
      else if (calories > 200) return "orange";
      else return "green";
    },
    // getUserOrders() {
    //   this.$store.dispatch("fetchOrders");
    // },
    getCartItems() {
      this.$store.dispatch("fetchOrderItems");
      console.log("-----");
      console.log(this.getOrderItems);
    },
  },
};
</script>

<style>
.cart__items__header {
  background-color: #f7f7f7;
  text-align: start;
  color: #6d6d6d;
}
.responsive1 {
  height: auto;
  width: 100%;
}
.item__content {
  block-size: 100%;
  writing-mode: horizontal-tb;
}
</style>