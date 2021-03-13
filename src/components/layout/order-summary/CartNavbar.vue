<template>
  <div style="z-index: 10000">
    <v-app-bar color="#ffffff" id="nav__header">
      <router-link style="text-decoration:none;" class="d-flex" :to="{ name: 'index' }">
        <div class="brand-logo-container">
          <v-img src="@/assets/img/logo.png" class="brand-logo"></v-img>
        </div>
        <v-toolbar-title class="headline my-auto">Get Design</v-toolbar-title>
      </router-link>
      <span style="font-weight:400;color:grey" class="mx-2"> | </span>
      <router-link style="text-decoration:none;" class="my-auto" :to="{ name: 'shop' }">
        <h5 class=" my-auto" style="font-size:0.9rem; color:grey;">Continue shopping</h5>
      </router-link>
      <v-spacer></v-spacer>
      <div class="green--text nav-link">
        <v-icon color="green">mdi-shield-check</v-icon>
        Secure Checkout
      </div>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "",
  data() {
    return {};
  },
  props: {},
  mounted() {},
  computed: {},
  methods: {},
};
</script>

<style>
.brand-logo {
  height: 70px;
  width: 70px;
  margin: 5px;
  padding: 0;
  -webkit-transition: -webkit-transform 1s;
}
.brand-logo:hover {
  -webkit-transform: rotate(360deg) translateZ(0);
}
</style>