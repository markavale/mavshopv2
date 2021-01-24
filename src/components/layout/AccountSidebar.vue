<template>
  <v-card height="400" width="100%" class="mr-1">
    <!-- <v-navigation-drawer permanent> -->
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="title mt-0 pa-0">
          My Account
        </v-list-item-title>
      </v-list-item-content>
    </v-list-item>

    <v-divider></v-divider>

    <v-list dense nav>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="subtitle font-weight-bold mt-0 pa-0">
            My Orders
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        v-for="item in orders"
        :key="item.title"
        link
        :to="{ name: item.link }"
        active-class="btnActiveStatus"
        class="sidebarMenu"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>


      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="subtitle font-weight-bold mt-0 pa-0">
            Account information
          </v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item
        v-for="item in account_info"
        :key="item.title"
        link
        :to="{ name: item.link }"
        active-class="btnActiveStatus"
        class="sidebarMenu"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>
    <!-- </v-navigation-drawer> -->
  </v-card>
</template>

<script>
export default {
  data() {
    return {
      account_info: [
        { title: "Personal Info", icon: "mdi-account", link: "shop" },
        { title: "My Wish List", icon: "mdi-heart", link: "wish-list" },
        { title: "About", icon: "mdi-help-box", link: "shop" },
      ],
      orders: [
        { title: "All", icon: "mdi-clipboard", link: "shop" },
        { title: "Refund", icon: "mdi-heart", link: "shop" },
        { title: "Closed", icon: "mdi-help-box", link: "shop" },
      ],
      right: null,
    };
  },
};
</script>

<style>
.btnActiveStatus {
  /* color: red; */
  background: #E1F5FE !important;
}
.sidebarMenu:hover {
  text-decoration: none;
}
.sidebarMenu {
  color: #1976d2 !important;
}
</style>