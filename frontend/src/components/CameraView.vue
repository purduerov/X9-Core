<template>
    <div id="camera-view">
        <iframe src="http://raspberrypi.local:8081/?action=stream"></iframe>
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
    -webkit-transform: rotate(180deg) transform(180deg);
}
</style>
