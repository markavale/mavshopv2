<template>
  <div>
    <div class="row text-left" v-if="pageLoading">
      <div class="col-md-3 col-sm-6 col-xs-12">
        <!-- v-for="item in 10"
        :key="item.id" -->
        <v-sheet color="grey lighten-4" class="pa-3">
          <v-skeleton-loader
            class="mx-auto"
            max-width="300"
            type="card"
          ></v-skeleton-loader>
        </v-sheet>
      </div>
    </div>
    <v-container fluid v-else>
      <vueper-slides
      class="no-shadow mt-5 px-5 mx-2"
      :visible-slides="3"
      slide-multiple
      :gap="3"
      :dragging-distance="200"
      :breakpoints="breakpoints"
    >
      <vueper-slide
        :key="item.id"
        v-for="item in getItems"
        class=""
      >
        <template v-slot:content>
          <!-- <div class="vueperslide__content-wrapper" style="flex-direction: row"> -->
            <!-- <div class="px-3"> -->
            <v-hover v-slot:default="{ hover }">
              <v-card class="mx-auto" color="grey lighten-4" max-width="600">
                <v-img
                  class="white--text align-end"
                  :aspect-ratio="16 / 9"
                  height="auto"
                  width="100%"
                  :src="item.new_img"
                >
                <!-- height="200px" -->
                  <v-expand-transition>
                    <div
                      v-if="hover"
                      class="d-flex transition-fast-in-fast-out transparent v-card--reveal display-3 white--text"
                      style="height: 70%"
                    >
                      <v-btn
                        v-if="hover"
                        @click="quickView(item)"
                        style="text-decoration: none; margin: 20px auto"
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
                    <span class="title font-weight-bold" style="color: #15314b">
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
            <!-- </div> -->
          <!-- </div> -->
        </template>
      </vueper-slide>
    </vueper-slides>
    </v-container>

    <ProductDialog :itemInstance="prodItem" :showDialog="showQuickView" />
  </div>
</template>

<script>
import ProductDialog from "@/components/layout/ProductDialog";
import { mapGetters } from "vuex";
import { VueperSlides, VueperSlide } from "vueperslides";
import "vueperslides/dist/vueperslides.css";
export default {
  name: "",
  data() {
    return {
      showQuickView: false,
      pageLoading: false,
      breakpoints: {
    1200: {
      slideRatio: 1 / 5
    },
    900: {
      slideRatio: 1 / 3
    },
    600: {
      slideRatio: 1 / 2,
      arrows: false,
      bulletsOutside: true
    },
    // The order you list breakpoints does not matter, Vueper Slides will sort them for you.
    1100: {
      slideRatio: 1 / 4
    }
  },
    };
  },
  props: {},
  mounted() {
    this.getAllItems();
    // this.loadPage();
    // this.getCategories();
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
  components: {
    ProductDialog,
    VueperSlides,
    VueperSlide,
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

<style scoped>
.vueperslides__arrow {
  color: yellow;
}
.truncateText {
  white-space: nowrap;
  word-break: normal;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>