<template>
  <div class="text-center">
    <v-menu
      v-model="menu"
      bot
      :nudge-width="200"
      offset-y
      :close-on-content-click="false"
      open-on-hover
    >
      <template v-slot:activator="{ on, attrs }">
        <v-btn v-bind="attrs" v-on="on" icon :color="menu ? 'primary' : ''"
         v-if="getOrders  == 0 || getOrders[0].items == 0">
            <v-icon>mdi-cart</v-icon>
          </v-btn>
        <v-btn v-bind="attrs" icon v-on="on" :color="menu ? 'primary' : ''" v-else>
            <div v-for="order in getOrders[0]" :key="order.id">
              <v-badge :content="order.total_items" color="error" v-if="order.total_items != 0">
            <v-icon>mdi-cart</v-icon>
             </v-badge>
             <v-icon v-else>mdi-cart</v-icon>
            </div>
        </v-btn>
      </template>
      <v-card class="pa-5" v-if="getOrders[0] == 0">
        <v-img
          src="@/assets/img/emptyCart.png"
          min-height="auto"
          max-height="300px"
          width="300px"
        >
        </v-img>
      </v-card>
      <div v-for="cart in getOrders[0]" :key="cart.id" v-else>
        <v-card class="pa-5" v-if="cart.total_items == 0">
          <v-img
            src="@/assets/img/emptyCart.png"
            min-height="auto"
            max-height="300px"
            width="300px"
          >
          </v-img>
        </v-card>

        <v-card width="350px" v-if="cart.total_items != 0">
          <v-list v-for="order in getOrders[0]" :key="order.id">
            <v-list-item
              v-for="orderItem in order.items"
              :key="orderItem.id"
              class="cart-item"
            >
              <v-img
                :src="orderItem.item.new_img"
                max-height="auto"
                max-width="100"
                contain
                aspect-ratio="1"
                class="grey lighten-3 mr-3"
              >
                <template v-slot:placeholder>
                  <v-row
                    class="fill-height pa-0"
                    align="center"
                    justify="center"
                  >
                    <v-progress-circular
                      indeterminate
                      color="grey lighten-5"
                    ></v-progress-circular>
                  </v-row>
                </template>
              </v-img>
              <v-list-item-content>
                <v-list-item-subtitle class="top-center text-muted mb-5">{{
                  orderItem.item.title
                }}</v-list-item-subtitle>
                <v-list-item-title class="mt-5">{{
                  orderItem.item.item_type
                }}</v-list-item-title>
                <h1
                  class="headline font-weight-bold"
                  v-if="orderItem.item.discount_price"
                >
                  P{{ orderItem.item.discount_price }}
                </h1>
                <h1
                  class="headline font-weight-bold"
                  v-if="!orderItem.item.discount_price"
                >
                  P{{ orderItem.item.price }}
                </h1>
              </v-list-item-content>
              <div class="top-right-corner">
                <v-tooltip bottom class="delete__icon">
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      :class="fav ? 'red--text' : ''"
                      icon
                      @click.prevent="removeFromCart(orderItem.item.slug)"
                      top
                    >
                      <v-icon
                        size="20"
                        color="error"
                        dark
                        v-bind="attrs"
                        v-on="on"
                      >
                        mdi-delete
                      </v-icon>
                    </v-btn>
                  </template>
                  <span>Remove</span>
                </v-tooltip>
              </div>
            </v-list-item>

            <v-divider></v-divider>
            <v-list-item>
              <v-list-item-action> </v-list-item-action>
              <v-list-item-title class="text--right">{{
                order.total
              }}</v-list-item-title>
            </v-list-item>
          </v-list>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn width="100%" class="primary white--text" outlined tile dense
              >VIEW CART / CHECK OUT</v-btn
            >
          </v-card-actions>
        </v-card>
      </div>
    </v-menu>

    <!-- <v-hover v-slot="{ hover }">
      <div>
        <v-btn icon :color="hover ? 'primary' : ''">
        <v-icon>mdi-cart</v-icon>
      </v-btn>
      

      </div>
    </v-hover> -->
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { axiosBase } from "@/api/axiosConfig";
export default {
  name: "CartItems",
  data: () => ({
    fav: true,
    menu: false,
    message: false,
    hints: true,
    cartMessage: "",
    totalItems: 0,
  }),

  computed: {
    ...mapGetters(["getOrders"]),
  },
  watch: {
    watchMenu() {
      console.log(this.menu);
    },
  },
  mounted() {
    this.getUserOrders();
  },
  methods: {
    getUserOrders() {
      this.$store.dispatch("fetchOrders");
    },
    removeFromCart(slug) {
      axiosBase
        .post(`api/remove-from-cart/${slug}/`, slug, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((res) => {
          this.menu = true;
          console.log(res.data);
          this.getUserOrders();
          this.cartMessage = res.data.message;
          console.log(this.cartMessage);
        })
        .catch((error) => {
          this.menu = true;
          console.log(error.response.data);
          console.log(error.request);
          if (error.response) {
            console.log(error.response.data);
          } else {
            console.log("Error", error.message);
          }
          console.log(error.config);
        });
    },
  },
};
</script>

<style>
.primary-color {
  color: #1976d2;
}
.top-right-corner {
  position: absolute;
  top: 0;
  right: 0;
}
.top-left-corner {
  position: absolute;
  top: 0;
  left: 0;
}
.top-center {
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -50px;
  margin-left: -50px;
}
.top-right-corner{
  display:none;
}
.cart-item:hover .top-right-corner{
  display:block;
}
.cart-item:hover {
  background-color: #f5f5f5;
}
.showCartItems {
  display: block;
}
.unShowCartItems {
  display: block;
}
</style>