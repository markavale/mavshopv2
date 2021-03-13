<template>
  <div>
    <Header />
    <v-container fluid>
      <div class="row">
        <div class="col-md-3 col-sm-3 col-xs-12">
          <v-card outlined>
            <v-card-title>Filters</v-card-title>
            <v-divider></v-divider>
            <v-list>
              <v-list-group>
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Lightroom</v-list-item-title>
                  </v-list-item-content>
                </template>
                <div>
                  <v-list-item
                    v-for="category in lightroomCategories"
                    :key="category.id"
                    class="categoryItem"
                    active-class="primary"
                  >
                    <!-- <v-btn> -->
                    <v-list-item-content
                      @click.prevent="categoryName(category.id)"
                    >
                      <v-list-item-title>{{
                        category.category_name
                      }}</v-list-item-title>
                    </v-list-item-content>
                    <!-- </v-btn> -->
                  </v-list-item>
                </div>
              </v-list-group>

              <v-list-group>
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>Photoshop</v-list-item-title>
                  </v-list-item-content>
                </template>
                <div>
                  <v-list-item
                    v-for="category in photoshopCategories"
                    :key="category.id"
                    class="categoryItem"
                  >
                    <v-list-item-content
                      @click.prevent="categoryName(category.id)"
                    >
                      <v-list-item-title>{{
                        category.category_name
                      }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </div>
              </v-list-group>
            </v-list>
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
              v-for="item in getItems"
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
                      <router-link
                        class="text-muted"
                        :to="{
                          name: 'item',
                          params: {
                            itemType: item.item_type,
                            slug: item.slug,
                          },
                        }"
                        >{{ item.title }}</router-link
                      >
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
    <ProductDialog :itemInstance="prodItem" :showDialog="showQuickView" />
  </div>
</template>
<script>
import Header from "@/components/Header";
import ProductDialog from "@/components/layout/ProductDialog";
// import ProductList from "@/components/layout/ProductDialog";
import { axiosBase } from "@/api/axiosConfig";
import { mapGetters } from "vuex";
export default {
  data: () => ({
    shop_items: [],
    // prodItem: {},
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
        action: "mdi-ticket",
        items: [{ title: "List Item" }],
        title: "Attractions",
      },
      {
        action: "mdi-silverware-fork-knife",
        active: true,
        items: [
          { title: "Breakfast & brunch" },
          { title: "New American" },
          { title: "Sushi" },
        ],
        title: "Dining",
      },
      {
        action: "mdi-school",
        items: [{ title: "List Item" }],
        title: "Education",
      },
      {
        action: "mdi-run",
        items: [{ title: "List Item" }],
        title: "Family",
      },
      {
        action: "mdi-bottle-tonic-plus",
        items: [{ title: "List Item" }],
        title: "Health",
      },
      {
        action: "mdi-content-cut",
        items: [{ title: "List Item" }],
        title: "Office",
      },
      {
        action: "mdi-tag",
        items: [{ title: "List Item" }],
        title: "Promotions",
      },
    ],
    pageLoading: false,
    categories: [],
    lightroom_category: [],
    photoshop_category: [],
  }),
  mounted() {
    this.getAllItems();
    this.loadPage();
    this.getCategories();
  },
  computed: {
    ...mapGetters(["getItems", "getWishLists", "prodItem"]),
    itemCategories() {
      return this.categories;
    },
    photoshopCategories() {
      return this.photoshop_category;
    },
    lightroomCategories() {
      return this.lightroom_category;
    },
  },

  created() {},

  components: {
    Header,
    // ProductList,
    // TwentyTwenty,
    ProductDialog,
    // CartModal,
  },
  methods: {
    loadPage() {
      this.pageLoading = true;
      setTimeout(() => {
        this.pageLoading = false;
      }, 1500);
    },

    // downloadItem(prodItem){
    //   axiosBase
    //     .get(`api/items/${prodItem.slug}/download/`, {responseType: 'blob'})
    //     .then((response)=>{
    //       const url = window.URL.createObjectURL(new Blob([response.data]));
    //       const link = document.createElement('a');
    //       link.href = url;
    //       link.setAttribute('download', `${prodItem.file.name}`);
    //       document.body.appendChild(link);
    //       link.click();
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
    //       console.log("download success")
    //     })
    //     .catch(err=>console.log(err));
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
    //       this.showQuickView = false;
    //       this.$store.dispatch("fetchOrders");
    //       // var type = res.data.type
    //       // this.$toast.info = ''
    //       if(res.data.type == 'success'){
    //          this.$toast.success({
    //         title: "Add to Cart",
    //         message: res.data.message,
    //         position: "top right",
    //         // type: res.data.type,
    //         closeButton: true,
    //         timeOut: 3500,
    //         showDuration: 500,
    //         hideDuration: 500,
    //         showMethod: "fadeIn",
    //         hideMethod: "fadeOut",
    //       });
    //       }
    //       else{
    //         this.$toast.info({
    //         title: "Add to Cart",
    //         message: res.data.message,
    //         position: "top right",
    //         closeButton: true,
    //         timeOut: 3500,
    //         showDuration: 500,
    //         hideDuration: 500,
    //         showMethod: "fadeIn",
    //         hideMethod: "fadeOut",
    //       });
    //       }

    //       console.log(res.data.type)
    //     })
    //     .catch((err) => console.log(err));
    // },
    categoryName(category) {
      console.log(category);
      this.$store.dispatch("filterItems", category);
      console.log("Dispatchingg.....");
      console.log(this.getItems);
      console.log("-------------------");
      // this.loadPage();
    },
    getCategories() {
      axiosBase
        .get("api/items/categories/")
        .then((res) => {
          this.categories = res.data;
          this.getPhotoshop();
          this.getLightroom();
          console.log(res.data);
        })
        .catch((err) => console.log(err));
    },
    getPhotoshop() {
      axiosBase
        .get("api/items/categories/?category_type=Photoshop")
        .then((res) => {
          this.photoshop_category = res.data;
          console.log(this.photoshop_category);
        })
        .catch((err) => console.log(err));
    },
    getLightroom() {
      axiosBase
        .get("api/items/categories/?category_type=Lightroom")
        .then((res) => {
          this.lightroom_category = res.data;
          console.log(this.lightroom_category);
        })
        .catch((err) => console.log(err));
    },
    quickView(item) {
      this.showQuickView = true;
      console.log(this.showQuickView);
      this.$store.dispatch("invertItemDialog");
      this.$store.dispatch("checkWishStatus", item.slug);
      this.$store.dispatch("retrieveItem", item.slug);
    },
    getAllItems() {
      this.$store.dispatch("fetchItems");
    },
    wishList(payload) {
      this.$store.dispatch("addRemoveWishList", payload);
      this.$store.dispatch("checkWishStatus", payload.slug);
      this.$store.dispatch("fetchWishLists");
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
.border__left {
  border-left: 5px solid #1976d2;
  background-color: #f5f5f5;
  width: 100%;
  font-size: 3rem;
}
#quickViewDialog {
  z-index: 10002;
}
/* .tags{
  margin:0 0 30px 0;
  padding: 8px;
  background-color:#fff;
} */
.categoryItem {
  padding-left: 3rem;
}
.categoryItem:hover {
  background-color: rgba(235, 235, 235, 0.5);
}
.activeCategory {
  background-color: blue !important;
}
.thumbnail {
  width: 100%;
  min-height: auto;
  max-height: 550px;
}
</style>