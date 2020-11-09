<template>
  <v-app>
    <v-main>
      <router-view />
    </v-main>
    <v-btn
            v-scroll="onScroll"
            v-show="fab"
            fab
            dark
            fixed
            bottom
            right
            color="primary"
            @click="toTop"
          >
            <v-icon>keyboard_arrow_up</v-icon>
          </v-btn>
  </v-app>
</template>

<script>
import 'cxlt-vue2-toastr/dist/css/cxlt-vue2-toastr.css'
import { axiosBase } from '@/api/axiosConfig'

export default {
  name: "App",
  components: {
    
  },
  mounted(){
    this.pageVisits();
  },

  data: () => ({
    fab: false,
    counter: 1,
  }),
  methods: {
    pageVisits(){
      axiosBase.post('api/count-visit/', {
        counter: this.counter,
      })
      .then()
      .catch(err=>console.log(err));
    },
    onScroll (e) {
      if (typeof window === 'undefined') return
      const top = window.pageYOffset ||   e.target.scrollTop || 0
      this.fab = top > 20
    },
    toTop () {
      this.$vuetify.goTo(0)
    }
  }
};
</script>


<style lang="scss">
html{
  scroll-behavior: smooth;
  box-sizing: border-box;
}
#app {
  font-family: 'Montserrat';
  background-color: #f5f5f5;
  
}
.lead{
  font-size:20px;
  font-weight: 500;
  color:#15314b;
  // color:#2c3e50;
}
.line-mf {
  width: 40px;
  height: 5px;
  background-color: #0078ff;
  margin: 0 auto 15px auto;
}
.container_box{
  padding: 3rem 2rem;
  background-color: #fff;
  margin: 50px 0;
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.06), 0 2px 5px 0 rgba(0, 0, 0, 0.2);
}
.black-overlay{
  background-color: rgba(0, 0, 0, 0.6);
  position: absolute;
  top: 0;
  left: 0px;
  padding: 0;
  height: 100vh;
  width: 100%;
  opacity: .9;
}

</style>
