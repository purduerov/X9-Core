<template>
    <div id="camera-view">
        <iframe src="http://10.42.0.204:8080/?action=stream"></iframe>
    </div>
</template>

<script>
export default {
    name: 'camera-view',
}
</script>

<style scoped>
iframe{
  height: 100%;
  width: 100%;
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
