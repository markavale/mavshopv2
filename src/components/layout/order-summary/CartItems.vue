<template>
  <div>
    <p class="title">Shopping Bag( {{ getOrderItems.length }} Items )</p>
    <v-row class="cart__items__header" align="center" align-content="center">
      <v-col cols="1">
        <v-checkbox
          color="primary"
          :input-value="selectAll"
          hide-details
          class="my-2 ml-3"
          @click.prevent="autoInverter(selectAll)"
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
      <CartItem
        :orderItem="orderItem"
        v-for="orderItem in getOrderItems"
        :key="orderItem.id"
      />
    </div>
    <div class="d-flex">
      <v-checkbox
        color="primary"
        :input-value="selectAll"
        hide-details
        class="my-2 mx-3"
        label="Select all"
        @click.prevent="autoInverter(selectAll)"
      ></v-checkbox>
      <v-btn
        rounded
        small
        text
        class="grey--text pa-0 my-auto"
        @click="popWarningMessage(getOrderItems)"
        :disabled="this.getOrderItems.length === 0"
      >
        <v-icon> mdi-delete </v-icon>
        <span class="text-decoration-underline"> Delete selected items </span>
      </v-btn>
    </div>
    <v-divider></v-divider>
    <RelatedProduct />
    <Loader :showLoading="showDeleteDialog" :message="deleteMesage" />
    <Snackbar
      :showSnackbar="showSnackbar"
      :message="messageSnackbar"
      :timeoutSnackbar="2000"
    />

    <v-row justify="center">
      <v-dialog v-model="showMessageWarning" max-width="290">
        <v-card>
          <v-card-title class="headline"> Delete Items </v-card-title>
          <v-card-text>
            Are you sure you want to delete the selected items?
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="red darken-1"
              text
              @click.prevent="removeSelectedItems"
            >
              Delete
            </v-btn>

            <v-btn
              color="grey darken-1"
              text
              @click="showMessageWarning = false"
            >
              Cancel
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { axiosBase } from "@/api/axiosConfig";
import CartItem from "@/components/layout/order-summary/CartItem";
import Loader from "@/components/layout/utils/Loader";
import Snackbar from "@/components/layout/utils/Snackbar";
import RelatedProduct from "@/components/layout/RelatedProduct";
export default {
  name: "Cart-Items",
  data() {
    return {
      showMessageWarning: false,
      showDeleteDialog: false,
      deleteMesage: "",
      showSnackbar: false,
      messageSnackbar: "",
      timeoutSnackbar: 0,
      able_to_delete: true,
    };
  },
  props: {},
  components: {
    CartItem,
    Loader,
    Snackbar,
    RelatedProduct,
  },
  mounted() {
    this.getCartItems();
    // this.mountSelectStatus;
  },
  computed: {
    ...mapGetters(["isAuthenticated", "getOrderItems", "selectAll"]),
  },
  methods: {
    popWarningMessage(order_items) {
      if (order_items.some((order_item) => order_item.is_selected === true)) {
        this.showMessageWarning = true;
        console.log("able to delete");
      } else {
        console.log("not able to delete");
        this.snackbarPopup("Please select an item to delete.", 1000);
      }
    },
    removeSelectedItems() {
      axiosBase
        .post(
          "api/remove-selected-items/",
          {},
          {
            headers: {
              "Content-Type": "application/json",
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.snackbarPopup(res.data.success, 2000);
          this.getCartItems();
          this.showMessageWarning = false;
          this.$store.dispatch("fetchOrders");
        })
        .catch((err) => {
          console.log(err);
        })
        .finally(() => {});
    },
    snackbarPopup(message, timeout) {
      this.showSnackbar = true;
      this.messageSnackbar = message;
      setTimeout(() => {
        this.showSnackbar = false;
      }, timeout);
    },
    getCartItems() {
      this.$store.dispatch("fetchOrderItems");
    },
    autoInverter(payload) {
      console.log(!payload);
      this.$store.dispatch("invertOrderItemSet", !payload);
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