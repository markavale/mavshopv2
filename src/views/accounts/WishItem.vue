<template>
  <div>
    <v-list-item class="ma-0">
      <v-row 
      align="start"
      justify="center"
      >
        <v-col cols="12" xs="12" sm="12" md="4" lg="4" xl="4" class="ma-0 py-2">
          <!-- <v-list-item-avatar> -->
          <v-img
            max-height="auto"
            max-width="100%"
            contain
            aspect-ratio="1"
            :src="item.new_img"
            class="ma-0 pa-0"
          >
            <template v-slot:placeholder>
                <v-sheet>
                  <v-skeleton-loader type="image" />
                </v-sheet>
              </template>
          </v-img>
          <!-- </v-list-item-avatar> -->
        </v-col>
        <v-col cols="12" xs="12" sm="12" md="8" lg="8" xl="8">
          <v-list-item-content class="wish__content my-auto">
            <template v-slot:placeholder>
              <v-sheet>
                <v-skeleton-loader type="paragraph" />
              </v-sheet>
            </template>
            <router-link
              :to="{
                name: 'item',
                params: {
                  itemType: item.item_type,
                  slug: item.slug,
                },
              }"
            >
              <v-list-item-title class="pa-0 ma-0">{{
                item.title
              }}</v-list-item-title>
            </router-link>
            <v-card-actions class="pa-0 ma-0">
              <v-rating
                :value="Number(item.computed_review)"
                class=""
                background-color="warning lighten-3"
                color="warning"
                dense
                readonly
              ></v-rating>
              <span class="body-2 font-weight-thin text-muted"
                >({{ item.total_reviews }})</span
              >
            </v-card-actions>
            <v-list-item-subtitle
              class="headline font-weight-bold pa-0 ma-0"
              v-if="item.item_price == 0"
              >FREE</v-list-item-subtitle
            >
            <v-list-item-subtitle
              class="headline font-weight-bold pa-0 ma-0"
              v-else
              >₱{{ item.item_price }}</v-list-item-subtitle
            >
            <div
              class="d-flex flex-sm-row flex-md-row flex-lg-row flex-xs-column my-2"
            >
              <AddToCartBtn :prodItem="item" />
              <v-btn
                class="ml-4"
                outlined
                tile
                dense
                :loading="isLoading"
                :disabled="isLoading"
                @click.prevent="wishList(item)"
              >
                Remove from Wish List
              </v-btn>
            </div>
          </v-list-item-content>
        </v-col>
      </v-row>
    </v-list-item>
    <v-divider></v-divider>
  </div>
</template>

<script>
import AddToCartBtn from "@/components/layout/AddToCartBtn";
// import Toast from "@/components/layout/Toast";
import { axiosBase } from "@/api/axiosConfig";
// import { mapGetters } from "vuex";
export default {
  name: "Wish-Item",
  data: () => ({
    isLoading: false,
  }),
  props: {
    item: Object,
  },
  components: {
    AddToCartBtn,
  },
  mounted() {},
  computed: {},
  methods: {
    wishList(payload) {
      this.isLoading = true;
      axiosBase
        .post(
          `api/wish-list/${payload.slug}/`,
          {},
          {
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              Authorization: `Token ${localStorage.getItem("token")}`,
            },
          }
        )
        .then((res) => {
          console.log(res.data);
          this.wishLoading = false;
          this.$store.dispatch("fetchWishLists");
          console.log(this.getWishStatus);
        })
        .catch((err) => {
          console.log(err);
          console.log(err.response.data);
        });
    },
  },
};
</script>

<style>
.wish__img {
  height: 200px;
  width: 100%;
  padding: 12px;
}
.wish__img__responsive {
  min-height: auto;
  max-height: 180px;
  /* height:auto; */
  min-width: 100%;
  max-width: 100%;
}
.wish__item {
  height: auto;
}
.responsive {
  width: 100%;
  height: auto;
}
@media screen and (min-width: 300px) and (max-width: 767px) {
  /* .wish__img{
    height:auto;
    width:100%;
  }
  .wish__img__responsive{
    height:auto;
    width:100%;
  } */
}
</style>