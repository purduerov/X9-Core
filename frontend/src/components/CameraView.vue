<template>
    <div id="camera-view">
        <div class="image">
            <img :src="source">
        </div>
        <div class="buttons">
            <button @click="port = 8080">Camera 1</button>
            <button @click="port = 8081">Camera 2</button>
            <button @click="port = 8082">Camera 3</button>
            <button @click="port = 8083">Camera 4</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'camera-view',
    data: function() {
        return {
            port: 8080
        }
    },
    computed: {
        source: function() {
            return `http://10.42.0.164:${this.port}/?action=stream`
        }
    }
}
</script>

<style scoped>

.buttons{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 50px;
    display: flex;
    justify-content: space-between;
}

button {
    width: 20%;
    font-size: 30px;
    flex: 1;
    background-color: #555555;
}

#camera-view {
    position: relative;
    height: 100%;
    width: 100%;
}

.image {
    height: calc(100% - 50px);
    width: 100%;
    display: flex;
    align-items: center;
}

.image > img {
    max-height: 100%;
    max-width: 100%;
    width: 100%;
}
</style>
