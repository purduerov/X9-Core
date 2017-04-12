<template>
    <div id="camera-view2">
        <iframe src="http://10.42.0.204:8081/?action=stream"></iframe>
    </div>
</template>

<script>
export default {
    name: 'camera-view2',
}
</script>

<style scoped>
iframe{
  height: 100%;
  width: 100%;
}

#camera-view2 {
    z-index: 2;
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
}

#camera-view2 > img {
    max-height: 100%;
    max-width: 100%;
}
</style>
