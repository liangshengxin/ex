<template>
<div>
    <i class="cubeic-more" style="color:#4493F7"></i>
</div>
</template>

<script>
export default {
    name:'category',
    created() {
        const toast = this.$createToast({
            txt: '这些还没想好怎么弄！',
            type: 'txt',
            time:2000,
            maskClosable:true,
            onTimeout: () => {
                this.$router.back()
            }
        })
        toast.show()
    },
}
</script>
