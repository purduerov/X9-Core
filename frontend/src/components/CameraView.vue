<template>
    <div id="camera-view">
        <!--<iframe height="764px" width="1024px" src="http://10.42.0.204:8080/?action=stream"></iframe>-->
        <img src="src/assets/image.jpg"/>
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
    z-index: 0;
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
}

#camera-view > img {
    //max-height: 100%;
    //max-width: 100%;
}
</style>
