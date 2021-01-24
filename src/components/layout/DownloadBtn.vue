<template>
    <div>
        
    </div>
</template>

<script>
export default {
    name: '',
    data(){
        return {}
    },
    props: {},
    mounted(){},
    computed: {},
    methods: {
        downloadItem(prodItem) {
            axiosBase
                .get(`api/items/${prodItem.slug}/download/`, { responseType: "blob" })
                .then((response) => {
                const url = window.URL.createObjectURL(new Blob([response.data]));
                const link = document.createElement("a");
                link.href = url;
                link.setAttribute("download", `${prodItem.file.name}`);
                document.body.appendChild(link);
                link.click();
                this.$store.dispatch('invertItemDialog')
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
                console.log("download success");
                })
                .catch((err) => console.log(err));
            },
    },
}
</script>

<style>

</style>