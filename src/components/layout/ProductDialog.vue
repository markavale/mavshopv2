<template>
  <v-row justify="center" id="quickViewDialog">
    <v-dialog
      v-model="itemDialogStatus"
      persistent
      max-width="90%"
      max-heigth="auto"
    >
      <v-card class="pa-3" height="auto">
        <!-- <v-row>
            <v-col cols="12">
              <div class="top-right-corner mr-3 mb-5">
                <v-btn color="error" @click="showQuickView=false" fab x-small>
                  <v-icon size="30">mdi-close</v-icon>
                </v-btn>
              </div>
            </v-col>
          </v-row> -->
        <v-row dense>
          <v-col class="mx-auto mt-4" cols="12" sm="12" md="6" lg="6" v-if="prodItem.item_type == 'Lightroom'">
            <!-- <div class="twenty-container"> -->
              <div class="thumbnail">
              <TwentyTwenty
                v-if="prodItem.new_img && prodItem.old_img"
                :after="prodItem.new_img"
                :before="prodItem.old_img"
                beforeLabel="Before"
                afterLabel="After"
                class=""
              />
              <v-row
                class="fill-height ma-0"
                align="center"
                justify="center"
                v-else
              >
                <v-progress-circular
                  indeterminate
                  color="#15314b"
                ></v-progress-circular>
              </v-row>
            </div>
          </v-col>
          <v-col
            cols="12"
            sm="12"
            md="6"
            lg="6"
            v-else
          >
            <v-img :src="prodItem.new_img" width="100%" height="auto">
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular
                    indeterminate
                    color="#15314b"
                  ></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-col>
          
          <v-col cols="12" md="6" sm="6">
            <!-- <div class="col-md-7 col-sm-7 col-xs-12"> -->
            <!-- <v-breadcrumbs class="pb-0" :items="breadcrums"></v-breadcrumbs> -->
            <v-card-actions class="px-6 py-0">
              <!-- <v-spacer></v-spacer> -->
              <v-rating
                :value="Number(prodItem.computed_review)"
                class=""
                background-color="warning lighten-3"
                color="warning"
                dense
                readonly
              ></v-rating>
              <span class="body-2 font-weight-normal">
                {{ prodItem.total_reviews }} REVIEWS</span
              >
              <v-spacer></v-spacer>
              <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                  <v-btn
                    color="error"
                    @click="closeItemDialog"
                    fab
                    x-small
                    v-bind="attrs"
                    v-on="on"
                  >
                    <v-icon size="30">mdi-close</v-icon>
                  </v-btn>
                </template>
                <span>Close</span>
              </v-tooltip>
            </v-card-actions>
            <div class="pl-6 mb-2">
              <p class="display-1 mb-0">{{ prodItem.title }}</p>
              <v-card-actions class="pa-0">
                <p
                  class="headline font-weight-bold py-3 pl-2 border__left"
                  style="color: #15314b"
                >
                  <span v-if="!prodItem.is_free && prodItem.discount_price"
                    >${{ prodItem.discount_price }}
                  </span>
                  <span v-if="prodItem.is_free">Free </span>
                  <del
                    v-if="!prodItem.is_free && prodItem.discount_price"
                    style=""
                    class="subtitle-1 font-weight-normal grey--text"
                    >${{ prodItem.price }}</del
                  >
                  <span v-if="!prodItem.is_free && !prodItem.discount_price"
                    >${{ prodItem.price }}
                  </span>
                </p>
              </v-card-actions>
              <p class="subtitle-1 font-weight-normal" color="">
                {{ prodItem.description }}
              </p>
              <p class="headline ma-0 pa-0">
                  Tags
                </p>
              <div class="text-left mb-3">
                <v-chip
                small
                  class="ma-2"
                  color="#15314b"
                  label
                  text-color="white"
                  default
                  v-for="tag in prodItem.tags"
                  :key="tag.id"
                >
                  {{ tag }}
                </v-chip>
              </div>
              <!-- <p class="title">SIZE</p>
                <v-radio-group v-model="row" row>
                  <v-radio label="XS" value="XS"></v-radio>
                  <v-radio label="S" value="s"></v-radio>
                  <v-radio label="M" value="m"></v-radio>
                  <v-radio label="L" value="l"></v-radio>
                  <v-radio label="XL" value="xl"></v-radio>
                </v-radio-group> -->
              <!-- <p class="title">File details</p>
                <v-text-field
                  outlined
                  style="width: 100px"
                  :value="1"
                  dense
                ></v-text-field> -->
              
              <div class="d-flex">
                <AddToCartBtn :prodItem="prodItem" />
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      class="ml-4"
                      outlined
                      tile
                      dense
                      v-bind="attrs"
                      v-on="on"
                      @click.prevent="wishList(prodItem)"
                    >
                      <v-icon medium :class="getWishStatus?'red--text':''">mdi-heart</v-icon>
                    </v-btn>
                  </template>
                  <span v-if="getWishStatus">Remove from wishlist</span>
                  <span v-else>Add to wishlist</span>
                </v-tooltip>
              </div>
            </div>
            <span class="pl-6">
              <router-link
                :to="{
                  name: 'item',
                  params: {
                    itemType: prodItem.item_type,
                    slug: prodItem.slug,
                  },
                }"
                class=""
                style="color: #15314b"
              >
                View full details >>
              </router-link>
            </span>
            <!-- <div class="tags text-left">
              <v-chip
                class="ma-2"
                color="#15314b"
                label
                text-color="white"
                default
                v-for="tag in prodItem.tags"
                :key="tag.id"
              >
                {{ tag }}
              </v-chip>
            </div> -->
          </v-col>
        </v-row>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import "vue-twentytwenty/dist/vue-twentytwenty.css";
import TwentyTwenty from "vue-twentytwenty";
import AddToCartBtn from "@/components/layout/AddToCartBtn"
// import { axiosBase } from "@/api/axiosConfig";
import { mapGetters } from "vuex";
export default {
  data: () => ({
    // prodItem: {},
    // showQuickView: false,
    closeDialog: true,
    itemDialog: false,
    isWish: false
  }),
  props: {
    itemInstance: Object,
    showDialog: Boolean,
  },
  computed: {
    ...mapGetters(['getWishStatus', "itemDialogStatus"]),
      prodItem(){
          return this.itemInstance
      },
      showQuickView(){
          return this.showDialog
      },
      
  },
  mounted(){
    // this.checkWishStatus();
  },
  components: {
      TwentyTwenty,
      AddToCartBtn
  },
  methods: {
    checkWishStatus(){
        this.$store.dispatch('checkWishStatus', this.prodItem.slug)
    },
    closeItemDialog(){
        this.$store.dispatch('invertItemDialog')
    },
    // downloadItem(prodItem) {
    //   axiosBase
    //     .get(`api/items/${prodItem.slug}/download/`, { responseType: "blob" })
    //     .then((response) => {
    //       const url = window.URL.createObjectURL(new Blob([response.data]));
    //       const link = document.createElement("a");
    //       link.href = url;
    //       link.setAttribute("download", `${prodItem.file.name}`);
    //       document.body.appendChild(link);
    //       link.click();
    //       this.$store.dispatch('invertItemDialog')
    //       this.$toast.success({
    //         title: `${prodItem.file.name}`,
    //         message: "Download Success!",
    //         position: "top right",
    //         closeButton: true,
    //         timeOut: 3500,
    //         showDuration: 500,
    //         hideDuration: 500,
    //         showMethod: "fadeIn",
    //         hideMethod: "fadeOut",
    //       });
    //       console.log("download success");
    //     })
    //     .catch((err) => console.log(err));
    // },
    // addToCart(prodItem) {
    //   axiosBase
    //     .post(`api/add-to-cart/${prodItem.slug}/`, prodItem, {
    //       headers: {
    //         "Content-Type": "application/x-www-form-urlencoded",
    //         Authorization: `Token ${localStorage.getItem("token")}`,
    //       },
    //     })
    //     .then((res) => {
    //       console.log("Success");
    //       console.log(prodItem.slug);
    //       console.log(res.data);
    //       this.$store.dispatch('invertItemDialog')
    //       this.$store.dispatch("fetchOrders");
    //       // var type = res.data.type
    //       // this.$toast.info = ''
    //       if (res.data.type == "success") {
    //         this.$toast.success({
    //           title: "Add to Cart",
    //           message: res.data.message,
    //           position: "top right",
    //           // type: res.data.type,
    //           closeButton: true,
    //           timeOut: 3500,
    //           showDuration: 500,
    //           hideDuration: 500,
    //           showMethod: "fadeIn",
    //           hideMethod: "fadeOut",
    //         });
    //       } else {
    //         this.$toast.info({
    //           title: "Add to Cart",
    //           message: res.data.message,
    //           position: "top right",
    //           closeButton: true,
    //           timeOut: 3500,
    //           showDuration: 500,
    //           hideDuration: 500,
    //           showMethod: "fadeIn",
    //           hideMethod: "fadeOut",
    //         });
    //       }

    //       console.log(res.data.type);
    //     })
    //     .catch((err) => console.log(err));
    // },
    wishList(payload){
      this.$store.dispatch('addRemoveWishList', payload.slug)
      console.log(payload)
      this.$store.dispatch('checkWishStatus', payload.slug)
      this.$store.dispatch('fetchWishLists')
      console.log("end of wish list listener")
    },
  },
  

};
</script>

<style scoped>
.img-responsive {
  height: auto;
  width: 100%;
}
.truncateText {
  white-space: nowrap;
  word-break: normal;
  overflow: hidden;
  text-overflow: ellipsis;
}
.thumbnail{
  min-width:100%;
  max-width:300px;
  min-height: auto;
  max-height:300px;
  object-fit:cover;
  object-position:50% 50%;
}
.twenty-container {
  width:100%;
  min-height: auto;
  max-height:300px;
  object-fit:cover;
  object-position:50% 50%;
  /* min-width: auto;
  max-width:500px; */
}
.border__left {
  border-left: 5px solid #1976d2;
  background-color: #f5f5f5;
  width: 100%;
  font-size: 3rem;
}
#quickViewDialog {
  z-index: 10002;
}
.categoryItem {
  padding-left: 3rem;
}
.categoryItem:hover {
  background-color: rgba(235, 235, 235, 0.5);
}
</style>