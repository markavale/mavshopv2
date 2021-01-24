<template>
  <div>
    <!-- slide-x-reverse-transition -->
    <Header />
    <!-- <div style="height: 60px"></div> -->
    <v-container fluid>
      <!-- <v-breadcrumbs class="product__breadcrumbs">
              <v-breadcrumbs-item
                :href="breadcrums[0].home.href.name"
                :disabled="breadcrums[0].home.disabled"
                class="mr-2 product__breadcrumbs"
              >
                {{ breadcrums[0].home.text.toUpperCase() }}
              </v-breadcrumbs-item>
              &nbsp;/&nbsp;
              <v-breadcrumbs-item
                :href="breadcrums[1].type.href.name"
                :disabled="breadcrums[1].type.disabled"
                class="product__breadcrumbs"
              >
                 &nbsp;{{ breadcrums[1].type.text.toUpperCase() }}
              </v-breadcrumbs-item>
              &nbsp;/&nbsp;
              <v-breadcrumbs-item
                :href="{name: 'breadcrums[2].instance.href.name'}"
                :disabled="breadcrums[2].instance.disabled"
                class="ml-2 product__breadcrumbs"
              >
                 &nbsp;{{ breadcrums[2].instance.text.toUpperCase() }}
              </v-breadcrumbs-item>
          </v-breadcrumbs> -->
      <v-row justify="space-around" align="start">
        <v-col class="account__list" cols="12" xs="12" sm="12" md="3" lg="3">
          <AccountSidebar />
        </v-col>
        <v-col cols="12" xs="12" sm="12" md="9" lg="9">
          <v-list v-if="pageLoading">
            <v-list-item class="wish__item">
              <div class="row">
                <div class="col-12 col-md-12" v-for="item in 10" :key="item.id">
                  <div class="d-flex">
                    <div class="wish__img">
                      <div class="wish__img__responsive">
                        <v-sheet>
                          <v-skeleton-loader type="image" height="180px" />
                        </v-sheet>
                      </div>
                    </div>
                    <v-list-item-content class="wish__content">
                      <v-sheet color="lighten-4" class="pa-3">
                        <v-skeleton-loader
                          class="mx-auto"
                          max-width="100%"
                          height="120px"
                          type="sentences, sentences, sentences"
                        ></v-skeleton-loader>
                      </v-sheet>
                    </v-list-item-content>
                  </div>
                  <v-divider></v-divider>
                </div>
              </div>
              <v-divider></v-divider>
            </v-list-item>
          </v-list>
          <v-list height="auto" width="100%" v-else>
            <span class="headline px-2 ma-0">My wish lists</span>
            <div v-for="wishLists in getWishLists" :key="wishLists.id">
              
              <div v-if="getWishLists.total_items !== 0">
                <v-divider></v-divider>
                <WishItem
                  :item="item"
                  v-for="item in wishLists.items"
                  :key="item.id"
                />
              </div>
              <div v-else>
                <h1 class="text--center red--text">no wish list</h1>
              </div>
            </div>
          </v-list>
        </v-col>
      </v-row>
    </v-container>

    <Toast
      :display="alert"
      :message="toastMessage"
      :toastType="type"
      :color="color"
    />
  </div>
</template>

<script>
import Header from "@/components/Header";
import AccountSidebar from "@/components/layout/AccountSidebar";
// import AddToCartBtn from "@/components/layout/AddToCartBtn";
import WishItem from "@/views/accounts/WishItem";
import Toast from "@/components/layout/Toast";
// import { axiosBase } from "@/api/axiosConfig"
import { mapGetters } from "vuex";
export default {
  name: "Wish-List",
  data() {
    return {
      alert: false,
      toastMessage: "testsetset",
      type: "info",
      color: "blue",
      wishLoading: false,
      pageLoading: false,
    };
  },
  mounted() {
    this.fetchAllWishLists();
    this.pageLoad();
  },
  components: {
    Header,
    AccountSidebar,
    Toast,
    // AddToCartBtn,
    WishItem,
  },
  computed: {
    ...mapGetters(["getWishLists"]),
  },
  methods: {
    pageLoad() {
      this.pageLoading = true;
      setTimeout(() => {
        this.pageLoading = false;
      }, 1000);
    },
    fetchAllWishLists() {
      this.$store.dispatch("fetchWishLists");
    },
  },
};
</script>

<style>
.wish__content {
  height: auto;
  padding: 0 0 40px 0;
}
.wish__container {
  width: 100%;
}
.account__list {
  position: -webkit-sticky;
  position: sticky;
  top: 0;
}

</style>