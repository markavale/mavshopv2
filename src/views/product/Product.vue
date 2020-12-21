<template>
  <div style="background-color:#ffffff;">
    <Header />
    <div style="height: 60px"></div>
    <v-container >
      <div class="row" v-if="prodItem">
        <div class="col-md-6 col-sm-6 col-xs-12" v-if="prodItem.item_type == 'Photoshop'">
          <v-img :src="prodItem.new_img" width="100%" height="auto" >
                <template v-slot:placeholder>
                  <v-row
                    class="fill-height ma-0"
                    align="center"
                    justify="center"
                  >
                    <v-progress-circular
                      indeterminate
                      color="#15314b"
                    ></v-progress-circular>
                  </v-row>
                </template>
              </v-img>
        </div>
        <div class="col-md-6 col-sm-6 col-xs-12" v-else>
          <div class="twenty-container">
                <TwentyTwenty
                  v-if="prodItem.new_img"
                  :before="prodItem.old_img"
                  :after="prodItem.new_img"
                  beforeLabel="Before"
                  afterLabel="After"
                />
                <v-row
                  class="fill-height ma-0"
                  align="center"
                  justify="center"
                  v-else
                >
                  <v-progress-circular
                    indeterminate
                    color="#15314b"
                  ></v-progress-circular>
                </v-row>
              </div>
        </div>
        <div class="col-md-6 col-sm-6 col-xs-12" >
          <v-breadcrumbs >
              <v-breadcrumbs-item
                :href="breadcrums[0].home.href.name"
                :disabled="breadcrums[0].home.disabled"
                class="mr-2"
              >
                {{ breadcrums[0].home.text.toUpperCase() }}
              </v-breadcrumbs-item>
              &nbsp;/&nbsp;
              <v-breadcrumbs-item
                :href="breadcrums[1].type.href.name"
                :disabled="breadcrums[1].type.disabled"
                class=""
              >
                 &nbsp;{{ breadcrums[1].type.text.toUpperCase() }}
              </v-breadcrumbs-item>
              &nbsp;/&nbsp;
              <v-breadcrumbs-item
                :href="{name: 'breadcrums[2].instance.href.name'}"
                :disabled="breadcrums[2].instance.disabled"
                class="ml-2"
              >
                 &nbsp;{{ breadcrums[2].instance.text.toUpperCase() }}
              </v-breadcrumbs-item>
          </v-breadcrumbs>
          <div class="pl-6">
            <v-card-actions class="pa-0">
              <v-rating
                :value="Number(prodItem.computed_review)"
                class=""
                background-color="warning lighten-3"
                color="warning"
                dense
                readonly
              ></v-rating>
              <span class="body-2 font-weight-thin"> {{ prodItem.total_reviews }} REVIEWS</span>
            </v-card-actions>
            <p class="display-1 mb-0">{{ prodItem.title }}</p>
            <v-card-actions class="pa-0">
              <p
                class="headline font-weight-bold py-3 pl-2 border__left"
                style="color: #15314b"
              >
                <span v-if="!prodItem.is_free && prodItem.discount_price"
                  >${{ prodItem.discount_price }}
                </span>
                <span v-if="prodItem.is_free">Free </span>
                <del
                  v-if="!prodItem.is_free && prodItem.discount_price"
                  style=""
                  class="subtitle-1 font-weight-normal grey--text"
                  >${{ prodItem.price }}</del
                >
                <span v-if="!prodItem.is_free && !prodItem.discount_price"
                  >${{ prodItem.price }}
                </span>
              </p>
            </v-card-actions>
            <p class="subtitle-1 font-weight-normal">
              {{ prodItem.description }}
            </p>
            <p class="title">File Details</p>
            <p class="subtitle">
               {{ prodItem.file.name }}( {{ prodItem.file.size }} )
            </p>
            <!-- <v-radio-group v-model="row" row>
              <v-radio label="XS" value="XS"></v-radio>
              <v-radio label="S" value="s"></v-radio>
              <v-radio label="M" value="m"></v-radio>
              <v-radio label="L" value="l"></v-radio>
              <v-radio label="XL" value="xl"></v-radio>
            </v-radio-group> -->
            <!-- <p class="title">ITEMS</p>
            <v-text-field
              outlined
              style="width: 100px"
              :value="1"
              dense
            ></v-text-field> -->
            <v-btn class="primary white--text" outlined tile dense
                @click.prevent="addToCart(prodItem)"
                v-if="!prodItem.is_free"
                  ><v-icon>mdi-cart</v-icon> ADD TO CART</v-btn
                >
                <v-btn class="primary white--text" outlined tile dense
                @click.prevent="downloadItem(prodItem)"
                v-else
                  ><v-icon>mdi-download</v-icon> DOWNLOAD</v-btn
                >
            <v-tooltip bottom>
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  class="ml-4"
                  outlined
                  tile
                  dense
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-heart</v-icon>
                </v-btn>
              </template>
              <span>Add to wishlist</span>
            </v-tooltip>
          </div>
        </div>
      </div>
      <!-- </div> -->
      <div class="row">
        <div class="col-sm-12 col-xs-12 col-md-12">
            <v-card flat>
                <p class="display-1 text-left pt-3">Customer Reviews ( {{ prodItem.total_reviews }} )</p>
                 <v-container>
                   <div class="computed__rating">
                   <div class="d-flex justify-center ma-0 pa-0" style="height:auto;">
                      <p class="warning--text display-1">{{ prodItem.computed_review }}</p> 
                      <p class="subtitle-1 grey--text mt-3 ml-2">/ 5.0</p>
                   </div>
                   <v-rating
                    :value="Number(prodItem.computed_review)"
                    class="mt-0 text-center"
                    background-color="warning lighten-3"
                    color="warning"
                    dense
                    readonly
                  ></v-rating>
                
                 </div>
                 </v-container>
                
                <v-list >
                <div  v-if="prodItem.total_reviews !== 0">
                  <v-list-item-group  color="primary" >
                  <v-divider></v-divider>
                  <div v-for="item in prodItem.reviews"
                    :key="item.id">
                    <v-list-item>
                      <v-list-item-avatar>
                        <v-img :src="item.user.image"></v-img>
                      </v-list-item-avatar>
                      <v-list-item-content>
                        <v-list-item-title >{{ item.user.username }}</v-list-item-title
                        ><v-rating
                          :value="Number(item.rate)"
                          class=""
                          background-color="warning lighten-3"
                          color="warning"
                          dense
                        ></v-rating>
                        <v-list-item-subtitle>{{ item.message }}</v-list-item-subtitle>
                      </v-list-item-content>
                  </v-list-item>
                  <v-divider></v-divider>
                  </div>
                </v-list-item-group>
                </div>
                <div v-else>
                  <p style="color:black;" class="text--center">no reviews!!</p>
                </div>
              </v-list>

          <v-card-text class="pa-0 pt-4" tile outlined>
            <p class="subtitle-1 font-weight-light pt-3 text-center">
              YOU MIGHT ALSO LIKE
            </p>
            <v-divider></v-divider>
            <div class="row text-center">
              <div class="col-md-2 col-sm-4 col-xs-12 text-center">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card :elevation="hover ? 16 : 2">
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      src="@/assets/img/home/deal4.jpg"
                    >
                      <v-card-title>Bags & Purses </v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 60% + Extra 10%</div>
                      <div>Baggit, Zara, Fossil</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn class="ma-2" outlined color="info">
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
              <div class="col-md-2 col-sm-4 col-xs-12 text-center">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card :elevation="hover ? 16 : 2">
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      src="@/assets/img/home/deal4.jpg"
                    >
                      <v-card-title>T-Shirt </v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 50%</div>
                      <div>Zara, Selected, Celio</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn class="ma-2" outlined color="info">
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
              <div class="col-md-2 col-sm-4 col-xs-12 text-center">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card :elevation="hover ? 16 : 2">
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      src="@/assets/img/home/deal4.jpg"
                    >
                      <v-card-title>Jeans </v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 60% + Extra 10%</div>
                      <div>Jack & Jones, Levis</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn class="ma-2" outlined color="info">
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
              <div class="col-md-2 col-sm-4 col-xs-12 text-center">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card :elevation="hover ? 16 : 2">
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      src="@/assets/img/shop/5.jpg"
                    >
                      <v-card-title>Shirts </v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 60% + Extra 10%</div>
                      <div>Nike, Adidas, Puma</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn class="ma-2" outlined color="info">
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
              <div class="col-md-2 col-sm-4 col-xs-12 text-center">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card :elevation="hover ? 16 : 2">
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      src="@/assets/img/home/deal4.jpg"
                    >
                      <v-card-title>Shoes </v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 60% + Extra 10%</div>
                      <div>Nike, Adidas, Puma</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn class="ma-2" outlined color="info">
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
              <div class="col-md-2 col-sm-4 col-xs-12 text-center">
                <v-hover v-slot:default="{ hover }" open-delay="200">
                  <v-card :elevation="hover ? 16 : 2">
                    <v-img
                      class="white--text align-end"
                      height="200px"
                      src="@/assets/img/home/deal4.jpg"
                    >
                      <v-card-title>Jackets </v-card-title>
                    </v-img>

                    <v-card-text class="text--primary text-center">
                      <div>Upto 60% + Extra 10%</div>
                      <div>Nike, Adidas, Puma</div>
                    </v-card-text>

                    <div class="text-center">
                      <v-btn class="ma-2" outlined color="info">
                        Explore
                      </v-btn>
                    </div>
                  </v-card>
                </v-hover>
              </div>
            </div>
          </v-card-text>
            </v-card>
        </div>
      </div>
    </v-container>
    <!-- <v-card class="accent">
      <v-container>
        <v-row no-gutters>
          <v-col  class="col-12 col-md-4 col-sm-12">
            <v-row>
              <v-col class="col-12 col-sm-3 pr-4 hidden-sm-only" align="right">
                <v-icon class="display-2">mdi-truck</v-icon>
              </v-col>
              <v-col class="col-12 col-sm-9 pr-4">
                <h3 class="font-weight-light">FREE SHIPPING & RETURN</h3>
                <p class="font-weight-thin">Free Shipping over $300</p>
              </v-col>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-4 col-sm-12">
            <v-row>
              <v-col class="col-12 col-sm-3 pr-4" align="right">
                <v-icon class="display-2">mdi-cash-usd</v-icon>
              </v-col>
              <v-col class="col-12 col-sm-9 pr-4">
                <h3 class="font-weight-light">MONEY BACK GUARANTEE</h3>
                <p class="font-weight-thin">30 Days Money Back Guarantee</p>
              </v-col>
            </v-row>
          </v-col>
          <v-col class="col-12 col-md-4 col-sm-12">
            <v-row>
              <v-col class="col-12 col-sm-3 pr-4" align="right">
                <v-icon class="display-2">mdi-headset</v-icon>
              </v-col>
              <v-col class="col-12 col-sm-9 pr-4">
                <h3 class="font-weight-light">020-800-456-747</h3>
                <p class="font-weight-thin">24/7 Available Support</p>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-card> -->
  </div>
</template>
<script>
import { axiosBase } from "@/api/axiosConfig";
import Header from "@/components/Header";
import "vue-twentytwenty/dist/vue-twentytwenty.css";
import TwentyTwenty from "vue-twentytwenty";
export default {
  data: () => ({
    rating: 4.5,
    product: {},
    breadcrums: {
      // home:{
      //   text: "Home",
      //   disabled: false,
      //   href: { name: "home" },
      // },
      // type:{
      //   text: "" || null,
      //   disabled: false,
      //   href: { name: "shop" },
      // },
      // instance:{
      //   text: "" || null,
      //   disabled: true,
      //   href: "#test",
      // },
    },
    item: 5,
    errors: [],

  }),
  mounted() {
    this.getItem();
  },
  computed: {
    // breadCrumbs() {
    //   let pathArray = this.$route.path.split("/");
    //   pathArray.shift();
    //   const breadCrumbs = [];
    //   // needed to handle the intermediary entries for nested vue routes
    //   let breadcrumb = "";
    //   let lastIndexFound = 0;
    //   for (let i = 0; i < pathArray.length; ++i) {
    //     breadcrumb = `${breadcrumb}${"/"}${pathArray[i]}`;
    //     if (
    //       this.$route.matched[i] &&
    //       Object.hasOwnProperty.call(this.$route.matched[i], "meta") &&
    //       Object.hasOwnProperty.call(this.$route.matched[i].meta, "breadCrumb")
    //     ) {
    //       breadCrumbs.push({
    //         href:
    //           i !== 0 && pathArray[i - (i - lastIndexFound)]
    //             ? "/" + pathArray[i - (i - lastIndexFound)] + breadcrumb
    //             : breadcrumb,
    //         disabled: i + 1 === pathArray.length,
    //         text: this.$route.matched[i].meta.breadCrumb || pathArray[i],
    //       });
    //       lastIndexFound = i;
    //       breadcrumb = "";
    //     }
    //   }
    //   return breadCrumbs;
    // },
    prodItem() {
      return this.product;
    },
  },
  components: {
    Header,
    TwentyTwenty
  },
  methods: {
    getItem() {
      if(this.$route.params.slug){
        axiosBase
        .get(`api/items/${this.$route.params.slug}/`)
        .then((res) => {
          this.product = res.data;
          const pathLinks = [
            {
              home:{
              text: "Home",
              disabled: false,
              href: { name: "home" },
              },
            },
            {
              type:{
              text: res.data.item_type,
              disabled: false,
              href: { name: "shop" },
              },
            },
            {
              instance:{
              text: res.data.slug,
              disabled: true,
              href: "#test",
              },
            }
          ]
          this.breadcrums = pathLinks
          console.log(this.breadcrums)
          console.log(this.breadcrums[1].type)
          console.log(this.breadcrums[1].type.href)
          console.log(this.breadcrums[1].type.text)
          // this.breadcrums.type.text = res.data.item_type
          // this.breadcrums.instance.text = res.data.slug
          console.log(res.data);
        })
        .catch((err) => {
          this.errors = [];
          console.log(err);
          console.log(err.response.data);
          this.errorMessage = err.response.data;
          let error_data = err.response.data;
          console.log(error_data);
          for (const field_error in error_data) {
            this.errors.push(error_data[field_error]);
          }
          console.log(this.errors)
        });
      }
      else{
        console.log("ERRRRRRRRR!!!!")
      }
      
    },

    downloadItem(prodItem){
      axiosBase
        .get(`api/items/${prodItem.slug}/download/`, {responseType: 'blob'})
        .then((response)=>{
          const url = window.URL.createObjectURL(new Blob([response.data]));
          const link = document.createElement('a');
          link.href = url;
          link.setAttribute('download', `${prodItem.file.name}`);
          document.body.appendChild(link);
          link.click();
          this.$toast.success({
            title: `${prodItem.file.name}`,
            message: "Download Success!",
            position: "top right",
            closeButton: true,
            timeOut: 3500,
            showDuration: 500,
            hideDuration: 500,
            showMethod: "fadeIn",
            hideMethod: "fadeOut",
          });
          console.log("download success")
        })
        .catch(err=>console.log(err));
    },

    addToCart(prodItem) {
      axiosBase
        .post(`api/add-to-cart/${prodItem.slug}/`, prodItem, {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            Authorization: `Token ${localStorage.getItem("token")}`,
          },
        })
        .then((res) => {
          console.log("Success");
          console.log(prodItem.slug);
          console.log(res.data);
          this.showQuickView = false;
          this.$store.dispatch("fetchOrders");
          // var type = res.data.type
          // this.$toast.info = ''
          if(res.data.type == 'success'){
             this.$toast.success({
            title: "Add to Cart",
            message: res.data.message,
            position: "top right",
            // type: res.data.type,
            closeButton: true,
            timeOut: 3500,
            showDuration: 500,
            hideDuration: 500,
            showMethod: "fadeIn",
            hideMethod: "fadeOut",
          });
          }
          else{
            this.$toast.info({
            title: "Add to Cart",
            message: res.data.message,
            position: "top right",
            closeButton: true,
            timeOut: 3500,
            showDuration: 500,
            hideDuration: 500,
            showMethod: "fadeIn",
            hideMethod: "fadeOut",
          });
          }
         
          console.log(res.data.type)
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>
<style>
.border__left{
  border-left:5px solid #1976d2;
  background-color:rgba(25, 118, 210,0.2);
  width:100%;
  font-size:3rem;
}
.computed__rating{
  /* background-color:rgba(25, 118, 210,0.2); */
  background-color:#f5f5f5;
}
</style>
