<template>
    <div v-show="active" id="container">
        <slot></slot>
    </div>
</template>

<script>
    export default {
        name: 'Tab',
        props: ['title'],
        data: function() {
            return {
                active: false
            }
        },
        mounted: function() {
            this.$parent.addTab(this)
        }
    }
</script>

<style scoped>
#container {
    width: 100%;
}
</style>