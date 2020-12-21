<template>
  <div>
    <Header />
    <v-container>
      <div class="row">
        <div class="col-md-3 col-sm-3 col-xs-12">
          <v-card outlined>
            <v-card-title>Filters</v-card-title>
            <v-divider></v-divider>
            <template>
              <v-treeview
                :items="items"
                :open="[1]"
                :active="[5]"
                :selected-color="'#fff'"
                activatable
                open-on-click
                dense
              ></v-treeview>
            </template>
            <v-divider></v-divider>
            <v-card-title>Price</v-card-title>
            <v-range-slider
              v-model="range"
              :max="max"
              :min="min"
              :height="10"
              class="align-center"
              dense
            ></v-range-slider>
            <v-row class="pa-2" dense>
              <v-col cols="12" sm="5">
                <v-text-field
                  :value="range[0]"
                  label="Min"
                  outlined
                  dense
                  @change="$set(range, 0, $event)"
                ></v-text-field>
              </v-col>
              <v-col cols="12" sm="2">
                <p class="pt-2 text-center">TO</p>
              </v-col>
              <v-col cols="12" sm="5">
                <v-text-field
                  :value="range[1]"
                  label="Max"
                  outlined
                  dense
                  @change="$set(range, 1, $event)"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-divider></v-divider>
            <v-card-title class="pb-0">Customer Rating</v-card-title>
            <v-container class="pt-0" fluid>
              <v-checkbox
                append-icon="mdi-star"
                label="4 & above"
                hide-details
                dense
              ></v-checkbox>
              <v-checkbox
                append-icon="mdi-star"
                label="3 & above"
                hide-details
                dense
              ></v-checkbox>
              <v-checkbox
                append-icon="mdi-star"
                label="2 & above"
                hide-details
                dense
              ></v-checkbox>
              <v-checkbox
                append-icon="mdi-star"
                label="1 & above"
                hide-details
                dense
              ></v-checkbox>
            </v-container>
            <!-- <v-divider></v-divider>
            <v-card-title class="pb-0">Size</v-card-title>
            <v-container class="pt-0" fluid>
              <v-checkbox label="XS" hide-details dense></v-checkbox>
              <v-checkbox label="S" hide-details dense></v-checkbox>
              <v-checkbox label="M" hide-details dense></v-checkbox>
              <v-checkbox label="L" hide-details dense></v-checkbox>
              <v-checkbox label="XL" hide-details dense></v-checkbox>
              <v-checkbox label="XXL" hide-details dense></v-checkbox>
              <v-checkbox label="XXXL" hide-details dense></v-checkbox>
            </v-container> -->
          </v-card>
        </div>
        <div class="col-md-9 col-sm-9 col-xs-12">
          <v-breadcrumbs class="pb-0" :items="breadcrums"></v-breadcrumbs>

          <v-row dense>
            <v-col cols="12" sm="8" class="pl-6 pt-6">
              <small>Showing 1-12 of 200 products</small>
            </v-col>
            <v-col cols="12" sm="4">
              <v-select
                class="pa-0"
                v-model="select"
                :items="options"
                style="margin-bottom: -20px"
                outlined
                dense
              ></v-select>
            </v-col>
          </v-row>

          <v-divider></v-divider>
          <div class="row text-left" v-if="pageLoading">
            <div
              class="col-md-3 col-sm-6 col-xs-12"
              v-for="item in 10"
              :key="item.id"
            >
              <v-sheet color="grey lighten-4" class="pa-3">
                <v-skeleton-loader
                  class="mx-auto"
                  max-width="300"
                  type="card"
                ></v-skeleton-loader>
              </v-sheet>
            </div>
          </div>

          <div class="row text-left" v-else>
            <div
              class="col-md-3 col-sm-6 col-xs-12"
              :key="item.id"
              v-for="item in getItems[0]"
            >
              <v-hover v-slot:default="{ hover }">
                <v-card class="mx-auto" color="grey lighten-4" max-width="600">
                  <v-img
                    class="white--text align-end"
                    :aspect-ratio="16 / 9"
                    height="200px"
                    width="100%"
                    :src="item.new_img"
                  >
                    <!-- <v-card-title>{{ item.item_type }} </v-card-title> -->
                    <v-expand-transition>
                      <div
                        v-if="hover"
                        class="d-flex transition-fast-in-fast-out transparent v-card--reveal display-3 white--text"
                        style="height: 70%"
                      >
                        <!-- <CartModal /> -->
                        <v-btn
                          v-if="hover"
                          @click="quickView(item)"
                          style="text-decoration: none"
                          >VIEW</v-btn
                        >
                      </div>
                    </v-expand-transition>
                    <template v-slot:placeholder>
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="#15314b"
                        ></v-progress-circular>
                      </v-row>
                    </template>
                  </v-img>
                  <v-card-text class="text--primary">
                    <div class="truncateText">
                      <router-link class="text-muted" 
                      :to="{
                          name: 'item',
                          params: {
                            itemType: item.item_type,
                            slug: item.slug,
                          },
                        }"
                      >{{ item.title }}</router-link>
                    </div>
                    <div
                      v-if="item.is_free"
                      class="title font-weight-bold"
                      style="color: #15314b"
                    >
                      FREE
                    </div>
                    <div
                      v-if="!item.is_free & !item.discount_price"
                      class="title font-weight-bold"
                      style="color: #15314b"
                    >
                      ${{ item.price }}
                    </div>
                    <div v-if="!item.is_free">
                      <span
                        class="title font-weight-bold"
                        style="color: #15314b"
                      >
                        ${{ item.discount_price }}
                      </span>

                      <span
                        class="grey--text text-decoration-line-through font-italic"
                        >${{ item.price }}</span
                      >
                    </div>
                  </v-card-text>
                </v-card>
              </v-hover>
            </div>
          </div>

          <div class="text-center mt-12">
            <v-pagination v-model="page" :length="6"></v-pagination>
          </div>
        </div>
      </div>
    </v-container>

    <v-row justify="center" id="quickViewDialog">
      <v-dialog
        v-model="showQuickView"
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
          <v-row>
            <v-col
              cols="12"
              sm="12"
              md="6"
              lg="6"
              v-if="prodItem.item_type == 'Photoshop'"
            >
              <v-img :src="prodItem.new_img" width="100%" height="auto">
                <template v-slot:placeholder>
                  <v-row
                    class="fill-height ma-0"
                    align="center"
                    justify="center"
                  >
                    <v-progress-circular
                      indeterminate
                      color="#15314b"
                    ></v-progress-circular>
                  </v-row>
                </template>
              </v-img>
            </v-col>
            <v-col cols="12" sm="12" md="6" lg="6" v-else>
              <div class="twenty-container">
                <TwentyTwenty
                  v-if="prodItem.new_img"
                  :before="prodItem.old_img"
                  :after="prodItem.new_img"
                  beforeLabel="Before"
                  afterLabel="After"
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
                <span class="body-2 font-weight-normal"> {{ prodItem.total_reviews }} REVIEWS</span>
                <v-spacer></v-spacer>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="error"
                      @click="showQuickView = false"
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
                <v-card-actions class="pa-0 ">
                  <p
                    class="headline font-weight-bold py-3 pl-2 border__left"
                    style="color: #15314b"
                  >
                    <span v-if="!prodItem.is_free && prodItem.discount_price">${{ prodItem.discount_price }} </span>
                    <span v-if="prodItem.is_free">Free </span>
                    <del
                      v-if="!prodItem.is_free && prodItem.discount_price"
                      style=""
                      class="subtitle-1 font-weight-normal grey--text"
                      >${{ prodItem.price }}</del
                    >
                    <span v-if="!prodItem.is_free && !prodItem.discount_price">${{ prodItem.price }} </span>
                  </p>
                </v-card-actions>
                <p class="subtitle-1 font-weight-normal" color="">
                  {{ prodItem.description }}
                </p>
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
                <v-btn class="primary white--text" outlined tile dense
                @click.prevent="addToCart(prodItem)"
                v-if="!prodItem.is_free"
                  ><v-icon>mdi-cart</v-icon> ADD TO CART</v-btn
                >
                <v-btn class="primary white--text" outlined tile dense
                @click.prevent="downloadItem(prodItem)"
                v-else
                  ><v-icon>mdi-download</v-icon> DOWNLOAD</v-btn
                >
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      class="ml-4"
                      outlined
                      tile
                      dense
                      v-bind="attrs"
                      v-on="on"
                    >
                      <v-icon>mdi-heart</v-icon>
                    </v-btn>
                  </template>
                  <span>Add to wishlist</span>
                </v-tooltip>
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
                  style="color:#15314b"
                >
                View full details >>
                </router-link>
              </span>
              <!-- </div> -->
            </v-col>
          </v-row>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>
<script>
// import CartModal from "@/components/cart/CartModal";
import "vue-twentytwenty/dist/vue-twentytwenty.css";
import TwentyTwenty from "vue-twentytwenty";
import Header from "@/components/Header";
import { axiosBase } from "@/api/axiosConfig";
import { mapGetters } from "vuex";
export default {
  data: () => ({
    prodItem: {},
    showQuickView: false,
    dialog: false,
    range: [0, 10000],
    select: "Popularity",
    options: [
      "Default",
      "Popularity",
      "Relevance",
      "Price: Low to High",
      "Price: High to Low",
    ],
    page: 1,
    breadcrums: [
      {
        text: "Home",
        disabled: false,
        href: "breadcrumbs_home",
      },
      {
        text: "Clothing",
        disabled: false,
        href: "breadcrumbs_clothing",
      },
      {
        text: "T-Shirts",
        disabled: true,
        href: "breadcrumbs_shirts",
      },
    ],
    min: 0,
    max: 10000,
    items: [
      {
        id: 2,
        name: "Photoshop",
        children: [
          { id: 2, name: "All" },
          { id: 3, name: "Logo" },
          { id: 4, name: "Certificate" },
          { id: 5, name: "Shirt" },
        ],
      },
      {
        id: 1,
        name: "Lightroom",
        children: [
          { id: 5, name: "All" },
          { id: 6, name: "Moody Dark" },
          { id: 7, name: "Cinematic" },
          { id: 8, name: "Color Pop" },
          { id: 9, name: "Dark" },
        ],
      },
    ],
    pageLoading: false,
  }),
  mounted() {
    this.getAllItems();
    this.loadPage();
  },

  computed: {
    ...mapGetters(["getItems"]),
    
  },

  created() {},

  components: {
    Header,
    TwentyTwenty,
    // CartModal,
  },
  methods: {
    loadPage() {
      this.pageLoading = true;
      setTimeout(() => {
        this.pageLoading = false;
      }, 1500);
    },
    quickView(item) {
      this.showQuickView = true;
      console.log(this.showQuickView);
      axiosBase
        .get(`api/items/${item.slug}/`)
        .then((res) => {
          this.prodItem = res.data;
          console.log(this.prodItem.new_img);
        })
        .catch((err) => console.log(err));
    },
    // incrementView(item){
    //   axiosBase
    //   .post(`api/items/${item.slug}/`,item)
    // },
    downloadItem(prodItem){
      axiosBase
        .get(`api/items/${prodItem.slug}/download/`, {responseType: 'blob'})
        .then((response)=>{
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `${prodItem.file.name}`);
          document.body.appendChild(link);
          link.click();
          this.$toast.success({
            title: `${prodItem.file.name}`,
            message: "Download Success!",
            position: "top right",
            closeButton: true,
            timeOut: 3500,
            showDuration: 500,
            hideDuration: 500,
            showMethod: "fadeIn",
            hideMethod: "fadeOut",
          });
          console.log("download success")
        })
        .catch(err=>console.log(err));
    },
    addToCart(prodItem) {
      axiosBase
        .post(`api/add-to-cart/${prodItem.slug}/`, prodItem, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((res) => {
          console.log("Success");
          console.log(prodItem.slug);
          console.log(res.data);
          this.showQuickView = false;
          this.$store.dispatch("fetchOrders");
          // var type = res.data.type
          // this.$toast.info = ''
          if(res.data.type == 'success'){
             this.$toast.success({
            title: "Add to Cart",
            message: res.data.message,
            position: "top right",
            // type: res.data.type,
            closeButton: true,
            timeOut: 3500,
            showDuration: 500,
            hideDuration: 500,
            showMethod: "fadeIn",
            hideMethod: "fadeOut",
          });
          }
          else{
            this.$toast.info({
            title: "Add to Cart",
            message: res.data.message,
            position: "top right",
            closeButton: true,
            timeOut: 3500,
            showDuration: 500,
            hideDuration: 500,
            showMethod: "fadeIn",
            hideMethod: "fadeOut",
          });
          }
         
          console.log(res.data.type)
        })
        .catch((err) => console.log(err));
    },
    getAllItems() {
      this.$store.dispatch("fetchItems");
    },
  },
};
</script>
<style>
.v-card--reveal {
  align-items: center;
  bottom: 0;
  justify-content: center;
  opacity: 0.8;
  position: absolute;
  width: 100%;
}
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
.twenty-container {
  height: auto;
  width: 100%;
}
.border__left{
  border-left:5px solid #1976d2;
  background-color:#f5f5f5;
  width:100%;
  font-size:3rem;
}
#quickViewDialog{
  z-index:10002;
}
</style>