import { axiosBase } from "@/api/axiosConfig";
// import index from '@/store/index';
import router from "@/router";
// import axios from 'axios';
const state = {
    items: [],
    orderItems: [],
    orders: [],
    wishLists: [],
    showQuickView: false,
    isWish: false,
    scrollUp: true,

    coupons: [],
    selectedItems: [],
    activeCoupon: [],
};

const getters = {
    isScrollingUp: (state) => state.scrollUp,
    getItems: (state) => state.items,
    getOrderItems: (state) => state.orderItems,
    getOrders: (state) => state.orders, 
    getWishLists: (state) => state.wishLists,
    getWishStatus: (state) => state.isWish,
    itemDialogStatus: (state) => state.showQuickView, 
    //coupon
    getCoupons: (state) => state.coupons,
    getActiveCoupon: (state) => state.activeCoupon,
};

const actions = {
    //navbar status menu showing
    checkScrollStatus: (context, payload) => {
        return new Promise((resolve, reject) => {
            try {
                context.commit('scrollStatus', payload)
                resolve(true)
            } catch (error) {
                reject(error)
            }
        })
    },
    invertScrollStatus: (context, payload) => {
        return new Promise((resolve, reject) => {
            try {
                context.commit('invertedScrollStatus', payload)
                // console.log(payload)
                resolve(true)
            } catch (error) {
                reject(error)
            }
        })
    },
    fetchItems: ({ commit }) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .get("api/items/")
                .then((res) => {
                    console.log(res.data);
                    commit("setItems", res.data);
                    resolve(true);
                })
                .catch((err) => {
                    router.push("/login");
                    reject(err);
                });
        });
    },
    fetchOrderItems: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .get("api/order-items/", {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        Authorization: `Token ${localStorage.getItem("token")}`,
                    },
                })
                .then((res) => {
                    console.log(res.data);
                    context.commit("setOrderItems", res.data);
                    resolve(true);
                })
                .catch((err) => reject(err));
        });
    },
    fetchOrders: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .get("api/orders/", {
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded",
                        Authorization: `Token ${localStorage.getItem("token")}`,
                    },
                })
                .then((res) => {
                    console.log(res.data);
                    console.log("--------------")
                    console.log(res.data[0].coupon)
                    context.commit("setOrders", res.data);
                    context.commit('setActiveCoupon', res.data[0].coupon)
                    
                    resolve(true);
                })
                .catch((err) => reject(err));
        });
    },
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
    filterItems: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
                .get(`api/items/?item_type=&is_free=&category=${payload}`)
                .then(res => {
                    console.log(payload)
                    console.log(res.data)
                    context.commit("setItems", res.data)
                    resolve(true)
                })
                .catch(err => {
                    console.log(err.data)
                    reject(err)
                })
        })
    },
    // adding new datas
    addRemoveWishList: ( context, payload) => {
        return new Promise((resolve, reject) => {
            console.log(payload)
            axiosBase
            .post(`api/wish-list/${payload}/`, {}, {
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
            // .then(res => {
            //     dispatch('checkWishStatus', res.data)
            // })
            .catch(err => {
                console.log(err.data)
                reject(err)
            })
        })
    },
    // Add to cart
    checkWishStatus: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .get(`api/wish-list/${payload}`, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                  },
              })
            .then(res => {
                console.log(res.data.isWish)
                context.commit('setWishStatus', res.data.isWish)
                resolve(true)
            })
            .catch(err => {
                console.log(err.response)
                reject(err)
            })
        })
    },
    invertItemDialog: (context) => {
        context.commit('updateItemDialogStatus')
    },
    // coupon
    fetchCoupons: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .get('api/coupons',{
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                }
            })
            .then(res => {
                context.commit('newCoupons', res.data)
                console.log(res.data)
                resolve(true)
            })
            .catch(err => reject(err))
        })
    },
    // fetchActiveCoupon: (context) => {
    //     return new Promise((resolve, reject) => {
    //         axiosBase
    //         .get('')
    //     })
    // },
    applyCoupon: ({dispatch, context}, payload) => {
        return new Promise((resolve, reject) => {
            console.log(payload)
            axiosBase
            .post(`api/coupons/${payload.id}/apply/`,{}, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                }
            })
            .then(res => {
                console.log(res.data)
                resolve(true)
                dispatch('fetchOrders')
                context.commit('setActiveCoupon', res.data)
            })
            .catch(err => reject(err))
        })
    },
    removeCoupon: ({dispatch}) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .post(`api/coupons/remove/`,{}, {
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                }
            })
            .then(res => {
                console.log(res.data)
                resolve(true)
                dispatch('fetchOrders')
            })
            .catch(err => {
                console.log(err.response.data)
                reject(err)
            })
        })
    },
    // selectingItems: (context) => {
    //     return new Promise((resolve, reject) => {
    //         axio
    //     })
    // },

};

const mutations = {
    setItems: (state, newItems) => state.items = newItems,
    setOrderItems: (state, newOrderItems) => state.orderItems = newOrderItems,
    setOrders: (state, newOrders) => state.orders = newOrders,
    setWishList: (state, newWishList) => state.wishLists = newWishList,
    setWishStatus: (state, newWishStatus) => state.isWish = newWishStatus,
    updateItemDialogStatus: (state) => state.showQuickView = !state.showQuickView,
    invertedScrollStatus: (state, newStatus) => state.isScrollingUp = newStatus,
    scrollStatus: (state, boolStatus) => state.isScrollingUp = boolStatus,

    //coupons
    newCoupons: (state, coupons) => state.coupons = coupons,
    setActiveCoupon: (state, newCoupon) => state.activeCoupon = newCoupon,
};

export default {
    state,
    getters,
    actions,
    mutations,
};