<template>
  <div style="z-index:10000">
    <v-app-bar color="#ffffff" fixed hide-on-scroll id="nav__header"> 
      <div class="brand-logo-container">
        <v-img src="@/assets/img/logo.png" class="brand-logo"></v-img>
      </div>
      <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->
      
      <v-toolbar-title class="headline">eMav test</v-toolbar-title>

      <v-spacer></v-spacer>

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
          <!-- <v-list rounded>
            <v-subheader>Hello, {{ getUsers.username }}</v-subheader>
            <v-list-item-group v-model="selectedItem" color="primary">
              <v-list-item v-for="(item, i) in items" :key="i" :to="item.href" class="no_underline">
                <v-list-item-icon>
                  <v-icon v-text="item.icon"></v-icon>
                </v-list-item-icon>
                <v-list-item-content>
                  <v-list-item-title v-text="item.text"></v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list-item-group>
          </v-list> -->
        </v-card>

        <!-- <v-list>
          <v-list-item>
          <v-list-item-title>
              <router-link :to="{ name: 'login' }" class="nav-link"
              >Profile</router-link>
            </v-list-item-title>
          </v-list-item>
          <v-list-item>
          <v-list-item-title>
              <router-link :to="{ name: 'login' }" class="nav-link"
              >Profile</router-link>
            </v-list-item-title>
          </v-list-item>
        </v-list> -->
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
</style>