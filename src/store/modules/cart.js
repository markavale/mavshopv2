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
    // selectAll: true,
    // itemSelected: false,
};

const getters = {
    isScrollingUp: (state) => state.scrollUp,
    getItems: (state) => state.items,
    getOrderItems: (state) => state.orderItems,
    getOrders: (state) => state.orders, 
    getWishLists: (state) => state.wishLists,
    getWishStatus: (state) => state.isWish,
    itemDialogStatus: (state) => state.showQuickView, 

    selectAll: (state) => !state.orderItems.some(order_item => order_item.is_selected === false),
    //coupon
    coupon_status: (state) => state.orders.some(order => order.use_coupon === true),
    // coupon_status: (state) => {
    //     const arrOrders = state.orders
    //     let coupon = arrOrders.reduce()
    //     arrOrders.forEach(order => {
    //         coupon = order.use_coupon
    //     });
    //     return coupon
    // },
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
                    // console.log(res.data);
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
                // console.log(res.data)
                context.commit('setWishList', res.data)
                resolve(true)
            })
            .catch(err => {
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
                    "Content-Type": "application/json",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                  },
                })
            .then(res => {
                console.log(res.data)
                context.commit('setWishList', res.data)
                resolve(true)
            })
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
    // order items
    invertOrderItemSet: ({dispatch}, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .patch('api/invert-selected-items/', {
                is_selected: payload
            }, {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                }
            })
            .then(res => {
                console.log(res.data)
                resolve(true)
                dispatch('fetchOrderItems')
                dispatch('fetchOrders')
            })
            .catch(err=>reject(err))
        })
    },
    // update select items
    invertSelectItem: ({dispatch}, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .patch(`api/order-items/${payload.id}/`, {
                is_selected: !payload.is_selected
            }, {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                }
            })
            .then(() => {
                resolve(true)
                dispatch('fetchOrderItems')
                dispatch('fetchOrders')
            })
            .catch(err=>{
                console.log(err.response.message)
                reject(err)
            })
        })
    },
    // coupon
    fetchCoupons: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .get('api/coupons',{
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                }
            })
            .then(res => {
                context.commit('newCoupons', res.data)
                resolve(true)
            })
            .catch(err => reject(err))
        })
    },
    applyCoupon: ({dispatch, context}, payload) => {
        return new Promise((resolve, reject) => {
            console.log(payload)
            axiosBase
            .post(`api/coupons/${payload.id}/apply/`,{}, {
                headers: {
                    "Content-Type": "application/json",
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
                    "Content-Type": "application/json",
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
    invertCouponStatus: ({dispatch}, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .patch(`api/orders/${payload.id}/`, {
                use_coupon: !payload.use_coupon
            }, {
                headers: {
                    "Content-Type": "application/json",
                    Authorization: `Token ${localStorage.getItem("token")}`,
                }
            })
            .then(() => {
                resolve(true)
                dispatch('fetchOrders')
            })
            .catch(err=>{
                console.log(err.response.message)
                reject(err)
            })
        })
    },
    invertUseCoupon: ({dispatch}, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .patch('api/invert-order-use-coupon/', {use_coupon: payload}, {
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Token ${localStorage.getItem('token')}`
                }
            })
            .then(res => {
                console.log(res.data)
                resolve(true)
                dispatch('fetchOrders')
            })
            .catch(err=>reject(err))
        })
    },
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