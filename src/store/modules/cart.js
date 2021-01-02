import { axiosBase } from "@/api/axiosConfig";
// import index from '@/store/index';
import router from "@/router";
// import axios from 'axios';
const state = {
    items: [],
    orderItems: [],
    orders: [],
    wishLists: [],
    
};

const getters = {
    getItems: (state) => state.items,
    getOrderItems: (state) => state.orderItems,
    getOrders: (state) => state.orders,
    getWishLists: (state) => state.wishLists,
};

const actions = {
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
                    context.commit("setOrders", res.data);
                    resolve(true);
                })
                .catch((err) => reject(err));
        });
    },
    fetchWishLists: (context) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .get('api/wish-list/')
            .then(res => {
                console.log(res.data)
                context.commit('setWishList', res.data)
                resolve(true)
            })
            .catch(err => reject(err))
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
    addRemoveWishList: (context, payload) => {
        return new Promise((resolve, reject) => {
            axiosBase
            .post(`api/wish-list/${payload.slug}/`)
            .then(res => {
                console.log(res.data)
                context.commit('setWishList', payload)
                resolve(true)
            })
            .catch(err => {
                console.log(err.data)
                reject(err)
            })
        })
    },
};

const mutations = {
    setItems: (state, newItems) => state.items.unshift(newItems),
    setOrderItems: (state, newOrderItems) => state.orderItems.unshift(newOrderItems),
    setOrders: (state, newOrders) => state.orders.unshift(newOrders),
    setWishList: (state, newWishList) => state.orders.unshift(newWishList),
    //updateItems: (state, filteredItem) => state.items = filteredItem,
};

export default {
    state,
    getters,
    actions,
    mutations,
};