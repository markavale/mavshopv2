<template>
  <div class="text-center">
    <v-snackbar
      v-model="showSnackbar"
      :timeout="timeout"
      left
    >
      {{ message }}

      <template v-slot:action="{ attrs }">
        <v-btn
          color="blue"
          text
          v-bind="attrs"
          @click="snackbar = false"
        >
          Close
        </v-btn>
      </template>
    </v-snackbar>
  </div>
</template>

<script>
export default {
    name: '',
    data(){
        return {}
    },
    props: {
        showSnackbar: Boolean,
        message: String,
        timeout: Number,
    },
    mounted(){},
    computed: {},
    methods: {},
}
</script>

<style>

</style>