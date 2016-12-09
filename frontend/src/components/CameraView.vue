<template>
    <div id="camera-view">
        <img src="assets/image.jpg">
    </div>
</template>

<script>
export default {
    name: 'camera-view',
}
</script>

<style scoped>
#camera-view {
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
}

#camera-view > img {
    max-height: 100%;
    max-width: 100%;
}
</style>
