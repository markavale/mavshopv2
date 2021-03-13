<template>
  <div style="z-index: 10000">
    <v-app-bar color="#ffffff" fixed hide-on-scroll id="nav__header">
      <!-- prominent
    height="115px;" -->
      <router-link style="text-decoration:none;" class="d-flex brand__link" :to="{ name: 'index' }">
        <div class="brand-logo-container">
          <v-img src="@/assets/img/logo.png" class="brand-logo"></v-img>
        </div>
        <v-toolbar-title class="headline m-auto">
          <span class="brand__title">Get Design</span>
        </v-toolbar-title>
      </router-link>
      <!-- <h1 class="brand__name">eMav Shop</h1>
      <v-toolbar-title class="shop__links" style="font-size:20px;">Photoshop</v-toolbar-title>
      <v-toolbar-title class="shop__links" style="font-size:20px;">Lightroom</v-toolbar-title>       -->
      <v-spacer></v-spacer>
      <!-- <template v-slot:extension >
        <v-tabs align-with-title>
          <v-tab>Tab 1</v-tab>
          <v-tab>Tab 2</v-tab>
          <v-tab>Tab 3</v-tab>
        </v-tabs>
      </template> -->
      <router-link style="text-decoration:none" :to="{ name: 'wish-list' }">
        <v-btn icon class="" color="danger" v-if="getWishLists.length !== 0">
          <div v-for="wish in getWishLists" :key="wish.id">
            <v-badge
              :content="wish.total_items"
              color="error"
              v-if="wish.total_items != 0"
            >
              <v-icon>mdi-heart</v-icon>
            </v-badge>
            <v-icon v-else>mdi-heart</v-icon>
          </div>
        </v-btn>

        <v-btn icon color="danger" v-else>
          <v-icon>mdi-heart</v-icon>
        </v-btn>
      </router-link>

      <v-menu
        v-model="accoutTab"
        bot
        :nudge-width="200"
        offset-y
        :close-on-content-click="false"
        open-on-hover
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn
            icon
            v-bind="attrs"
            v-on="on"
            :color="accoutTab ? 'primary' : ''"
          >
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>

        <v-card class="mx-auto" max-width="300" tile>
          <v-list rounded>
            <v-subheader v-if="requestUser"
              >Hello, {{ requestUser.username }}</v-subheader
            >
            <v-subheader v-else>...</v-subheader>
            <v-divider></v-divider>
            <v-list-item-group color="primary">
              <router-link :to="{ name: 'login' }" class="nav-link">
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>mdi-settings</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>Settings</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </router-link>

              <router-link :to="{ name: 'login' }" class="nav-link">
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>mdi-account</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>Account</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </router-link>

              <router-link
                :to="{ name: 'login' }"
                class="nav-link"
                v-if="!isAuthenticated"
              >
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon>mdi-login</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title>Login</v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </router-link>

              <router-link
                :to="{ name: 'logout' }"
                class="nav-link"
                v-if="isAuthenticated"
              >
                <v-list-item>
                  <v-list-item-icon>
                    <v-icon class="red--text">mdi-logout</v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title class="red--text"
                      >Logout</v-list-item-title
                    >
                  </v-list-item-content>
                </v-list-item>
              </router-link>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-menu>
      <CartItems />
    </v-app-bar>
    <div style="height: 60px"></div>
  </div>
</template>
    
<script>
import { mapGetters, mapMutations } from "vuex";
import CartItems from "@/components/cart/CartItems";
export default {
  data: () => ({
    scrollPosition: null,
    status: true,
    accoutTab: false,
    selectedItem: 1,
    items: [
      { text: "Settings", icon: "mdi-settings", href: { name: "login" } },
      { text: "Account", icon: "mdi-account", href: { name: "login" } },
      { text: "Login", icon: "mdi-login", href: { name: "login" } },
    ],
  }),
  components: {
    CartItems,
  },
  computed: {
    ...mapGetters([
      "requestUser",
      "isAuthenticated",
      "getWishLists",
      "isScrollingUp",
    ]),
  },
  mounted() {
    this.dispatchAction();
    this.checkStat();
  },
  methods: {
    handleScroll() {
      var currentScrollPosition = window.scrollY || window.scrollTop;
      if (currentScrollPosition > this.scrollPosition) {
        // console.log("Scrolling down");
        this.status = false;
        this.$store.dispatch("invertScrollStatus", this.status);
        mapMutations(["scrollStatus", this.status]);
      } else {
        this.status = true;
        // console.log("Scrolling up");
        this.$store.dispatch("invertScrollStatus", this.status);
        mapMutations(["scrollStatus", this.status]);
        // console.log(this.scrollPosition)
      }
      this.checkStat();

      // console.log("isScrollingUp");
      // console.log(this.isScrollingUp);
      this.scrollPosition = currentScrollPosition;
    },
    checkStat() {
      this.$store.dispatch("checkScrollStatus", this.status);
    },
    dispatchAction() {
      this.$store.dispatch("fetchCurrentUser");
      this.$store.dispatch("fetchWishLists");
      console.log(this.getWishLists)
    },
    // getCurrUser(){

    // },
    // fetchWishList(){

    // },
  },
  created() {
    window.addEventListener("scroll", this.handleScroll);
  },
  destroyed() {
    window.removeEventListener("scroll", this.handleScroll);
  },
};
</script>

<style>
.brand-logo {
  /* height: 50px;
  width: 50px; */
  height: 70px;
  width: 70px;
  margin: 5px;
  padding: 0;
  -webkit-transition: -webkit-transform 1s;
}
.brand-logo:hover {
  -webkit-transform: rotate(360deg) translateZ(0);
}
.fixed-bar {
  position: sticky;
  position: -webkit-sticky; /* for Safari */
  top: 6em;
  z-index: 2;
}
.containarize {
  padding: 0 30px;
}
.no_underline {
  text-decoration: None;
}
.icon-link:hover {
  color: #1976d2;
}
#nav__header {
  z-index: 10001;
}
.brand__name {
  padding-top: 12px;
  font-size: 1.8rem;
  font-weight: 500;
}
.shop__links {
  text-align: center;
  font-size: 14px;
  color: black;
  font-weight: 350;
  margin: 0 8px;
  padding: 0;
}
.brand__link {
  text-decoration: none;
}
.brand__title {
  text-decoration: none;
}
</style>