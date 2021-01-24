<template>
  <div>
      <v-alert
          :value="display"
          border="left"
          dismissible
          elevation="11"
          :color="color"
          :type="toastType"
          transition="slide-x-reverse-transition"
          class="item__alert"
        >
        <h5 class="subtitle font-weight-bold pa-0 ma-0 mb-1">{{ title }}</h5>
          {{ message }}
        </v-alert>
  </div>
</template>

<script>
export default {
    data(){
        return {
            
        }
    },
    props: {
        display: Boolean,
        message: String,
        toastType: String,
        color: String,
        title: String,
    },
    computed: {
        // toast(){
        //     return toast_data
        // }
    },
    methods: {

    },
}
</script>

<style scoped>
.item__alert{
  position: fixed;
  height:auto;
  width:300px;
  top:0;
  right:0;
  /* background-color:white; */
  z-index: 20000;
  /* margin:0px 5px 20px 10px; */
  margin:80px 20px 10px 0px;
  font-size:16px;

}
</style>