<template>
  <div style="z-index:10000">
    <v-app-bar color="#ffffff" fixed hide-on-scroll id="nav__header"
    > 
    <!-- prominent
    height="115px;" -->
      <div class="brand-logo-container">
        <v-img src="@/assets/img/logo.png" class="brand-logo"></v-img>
      </div>   
      <v-toolbar-title class="headline">eMav</v-toolbar-title>
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
      <v-btn 
      icon
      class="icon-link"
      >
        <v-icon>mdi-heart</v-icon>
      </v-btn>
     
      <v-menu left bottom>
        <template v-slot:activator="{ on, attrs }">
          <v-btn icon v-bind="attrs" v-on="on">
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>

        <v-card class="mx-auto" max-width="300" tile>
          <v-list rounded>
            <v-subheader>Hello, {{ requestUser.username }}</v-subheader>
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

              <router-link :to="{ name: 'login' }" class="nav-link" v-if="!isAuthenticated">
                <v-list-item>
                <v-list-item-icon>
                  <v-icon>mdi-login</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title>Login</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              </router-link>

              <router-link :to="{ name: 'logout' }" class="nav-link" v-if="isAuthenticated">
                <v-list-item>
                <v-list-item-icon>
                  <v-icon>mdi-logout</v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title>Logout</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              </router-link>
            </v-list-item-group>
          </v-list>
        </v-card>
      </v-menu>
       <CartItems />
      
    </v-app-bar>
    
  </div>
</template>
        


<script>
import { mapGetters } from "vuex";
import CartItems from "@/components/cart/CartItems"
export default {
  data: () => ({
      selectedItem: 1,
      items: [
        { text: 'Settings', icon: 'mdi-settings', href:{name:"login"} },
        { text: 'Account', icon: 'mdi-account', href:{name:"login"}  },
        { text: 'Login', icon: 'mdi-login', href:{name:"login"}  },
      ],
    }),
    components:{
      CartItems,
    },
    computed:{
      ...mapGetters(['requestUser', 'isAuthenticated'])
    },
    mounted(){
      this.getCurrUser()
    },
    methods: {
      getCurrUser(){
        this.$store.dispatch("fetchCurrentUser")
      }
    },
}
</script>

<style>
.brand-logo{
  height:50px;
  width:50px;
  margin:5px;
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
.no_underline{
  text-decoration: None;
}
.icon-link{
  color:#1976d2;
}
#nav__header{
  z-index:10001;
}
.brand__name{
  padding-top:12px;
  font-size:1.8rem;
  font-weight: 500;
}
.shop__links{
  text-align:center;
  font-size:14px;
  color:black;
  font-weight: 350;
  margin:0 8px;
  padding:0;
}
</style>