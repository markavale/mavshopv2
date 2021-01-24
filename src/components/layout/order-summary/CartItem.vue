<template>
  <div>
    <!-- v-for="orderItem in getOrderItems"
      :key="orderItem.id" -->
    <v-row class="ma-0" align="start" align-content="start">
      <v-col cols="1">
        <v-checkbox
          v-model="cartItemStatus"
          color="primary"
          :value="orderItem"
          hide-details
          class="my-2 ml-3"
        ></v-checkbox>
      </v-col>

      <v-col cols="5">
        <v-row no-gutters dense>
          <v-col cols="6">
            <v-list class="pa-0 ma-0">
              <v-list-item>
                <v-list-item-content class="pa-0">
                  <v-img class="responsive1" :src="orderItem.item.new_img">
                    <template v-slot:placeholder>
                      <v-sheet>
                        <v-skeleton-loader type="image" />
                      </v-sheet>
                    </template>
                  </v-img>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-col>
          <v-col cols="6">
            <p class="grey--text body-2 truncateText">
              {{ orderItem.item.title }}
            </p>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="3"> ₱{{ orderItem.item.item_price }} </v-col>
      <v-col cols="3">
        <span class="font-weight-bold">₱{{ orderItem.item.item_price }}</span>
      </v-col>
      <v-col class="ma-0 pa-0" cols="12">
        <v-divider></v-divider>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Cart-Item",
  data() {
    return {};
  },
  props: {
    orderItem: Object,
    isSelected: {
      type: Boolean,
      default: true,
    },
  },
  mounted() {},
  computed: {
    cartItemStatus: {
      get() {
        return this.isSelected;
      },
      set(newValue){
        this.isSelected = newValue
      }
    },
  },
  methods: {},
};
</script>

<style>
</style>
