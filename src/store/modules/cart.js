import { axiosBase } from "@/api/axiosConfig";
// import index from '@/store/index';
import router from "@/router";
// import axios from 'axios';
const state = {
    items: [],
    orderItems: [],
    orders: [],
    
};

const getters = {
    getItems: (state) => state.items,
    getOrderItems: (state) => state.orderItems,
    getOrders: (state) => state.orders,
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
};

const mutations = {
    setItems: (state, newItems) => state.items.unshift(newItems),
    setOrderItems: (state, newOrderItems) => state.orderItems.unshift(newOrderItems),
    setOrders: (state, newOrders) => state.orders.unshift(newOrders),
};

export default {
    state,
    getters,
    actions,
    mutations,
};