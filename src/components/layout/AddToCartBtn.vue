<template>
  <div>
    <v-btn
      class="primary white--text"
      outlined
      tile
      :loading="isLoading"
      dense
      @click.prevent="addToCart(prodItem)"
      v-if="!prodItem.is_free"
    >
      <v-icon>mdi-cart</v-icon>
      ADD TO CART</v-btn
    >

    <v-btn
      class="primary white--text"
      outlined
      :loading="isLoading"
      tile
      dense
      @click.prevent="downloadItem(prodItem)"
      v-else
      ><v-icon>mdi-download</v-icon> DOWNLOAD</v-btn
    >
    <Toast
      :display="alert"
      :message="toastMessage"
      :toastType="type"
      :color="color"
      :title="btnTitle"
    />
  </div>
</template>

<script>
import { axiosBase } from "@/api/axiosConfig";
import Toast from "@/components/layout/Toast";
export default {
  name: "Add-to-cart-btn",
  data: () => ({
    alert: false,
    toastMessage: "",
    type: "info",
    color: "blue",
    btnTitle: "",
    isLoading: false,
  }),
  props: {
    prodItem: Object,
  },
  components: {
    Toast,
  },
  mounted() {},
  computed: {},
  methods: {
    // add to cart method
    addToCart(prodItem) {
      this.isLoading = true;
      axiosBase
        .post(`api/add-to-cart/${prodItem.slug}/`, prodItem, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((res) => {
          console.log(res.data);
          this.$store.dispatch("fetchOrders");
          this.$store.dispatch("fetchOrderItems");
          this.$store.dispatch("invertItemDialog");
          this.isLoading = false;
          this.showToast(
            true,
            res.data.message,
            res.data.type,
            res.data.color,
            "Add to cart"
          );
        })
        .catch((err) => console.log(err));
    },
    //download item btn
    downloadItem(prodItem) {
      this.isLoading = true;
      axiosBase
        .get(`api/items/${prodItem.slug}/download/`, { responseType: "blob" })
        .then((response) => {
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement("a");
          link.href = url;
          link.setAttribute("download", `${prodItem.file.name}`);
          document.body.appendChild(link);
          link.click();
          this.$store.dispatch("invertItemDialog");
          this.isLoading = false;
          // alertToast, message, type, color
          this.showToast(
            true,
            `${prodItem.file.name} was downloaded successfully!`,
            "success",
            "green",
            "Download"
          );
          console.log("download success");
        })
        .catch((err) => {
          console.log(err);
          console.log(err.response);
        });
    },
    // show toast notification
    showToast(alertToast, message, type, color, title) {
      this.alert = alertToast;
      this.toastMessage = message;
      this.toastType = type;
      this.color = color;
      this.btnTitle = title;
      console.log("toast notif");
      console.log(this.alert);
      console.log(this.color);
      setTimeout(() => {
        this.alert = false;
      }, 2500);
    },
  },
};
</script>

<style>
</style>