import { axiosBase } from "@/api/axiosConfig";


const state = {
    product: {},
    wish_item: {},
    // wish_list: [],
}

const getters = {
    prodItem: (state) => state.product,
}

const actions = {
    // fetching product item
    retrieveItem: (context, payload) =>{
        return new Promise((resolve, reject) => {
            axiosBase
            .get(`api/items/${payload}/`)
            .then(res => {
                context.commit('retrievedItem', res.data)
                console.log(res.data)
                resolve(true)
            })
            .catch(err => reject(err))
        })
    },
    // fetch wish items
    fetchWishLists: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .get('api/wish-list/', {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                  },
              })
            .then(res => {
                console.log(res.data)
                context.commit('setWishList', res.data)
                resolve(true)
            })
            .catch(err => {
                console.log("errror")
                console.log(err.data)
                reject(err)
                
            })
        })
    },
    // add wish item
    CreateDestroyWishItem: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .post(`api/wish-list/${payload.slug}`, {}, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                  },
              })
              .then(res => {
                  context.commit('setWishList', res.data)
                  console.log(res.data)
                  resolve(true)
              })
              .catch(err => reject(err))
        })
    },
}
const mutations = {
    retrievedItem: (state, payload) => state.product = payload,
    setWishList: (state, payload) => state.wish_item = payload,
    // newRating: (state, newRating) => state.rating.unshift(newRating),
}


export default {
    state,
    getters,
    actions,
    mutations,
}