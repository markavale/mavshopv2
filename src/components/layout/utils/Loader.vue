<template>
  <div class="text-center">
    <v-dialog v-model="showLoading" hide-overlay persistent width="300">
      <v-card color="primary" dark>
        <v-card-text>
          {{ message }}
          <v-progress-linear
            indeterminate
            color="white"
            class="mb-0"
          ></v-progress-linear>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "Loading",
  data() {
    return {};
  },
  props: {
    showLoading: {
      default: false,
      type: Boolean,
    },
    message: String,
  },
  //   watch: {
  //     showLoading(val) {
  //       if (!val) return;
  //       setTimeout(() => (this.dialog = false), 4000);
  //     },
  //   },
  // mounted(){},
  // computed: {},
  // methods: {},
};
</script>

<style>
</style>