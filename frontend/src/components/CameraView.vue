<template>
    <div id="camera-view">
        <img src="http://10.10.1.125:8080/?action=stream">
    </div>
</template>

<script>
export default {
    name: 'camera-view',
}
</script>

<style scoped>
img {
  max-height: 100%;
  max-width: 100%;
  margin: 0 auto;
}

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
