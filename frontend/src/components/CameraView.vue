<template>
    <div id="camera-view">
        <div class="image">
            <img :src="source">
        </div>
        <div class="buttons">
            <button @click="port = 8083" v-on:click="temp_reset_rotate()">Main Camera</button>
            <button @click="port = 8080" v-on:click="temp_rotate()">PCT Camera</button>
            <button @click="port = 8081" v-on:click="temp_reset_rotate()">Fount Camera</button>
            <!--<button @click="port = 8085">Camera 4</button>-->
            <!--<button @click="port = 8081">Camera 5</button>-->
            <!--<button @click="port = 8083">Camera 6</button>-->
        </div>
    </div>
</template>

<script>
export default {
    name: 'camera-view',
    data: function() {
        return {
            port: 8082
        }
    },
    computed: {
        source: function() {
            return `http://10.42.0.130:${this.port}/?action=stream`
        }
    },

    temp_rotate: function() {
        getElementsByClass("image")[0].style.transform = "rotate(270deg)";
        //getElementsByClass("image")[0].style.webkit-transform = "rotate(270deg)";
    },

    temp_reset_rotate: function() {
        getElementsByClass("image")[0].style.transform = "rotate(0deg)";
        //getElementsByClass("image")[0].style.transform = "rotate(0deg)";
    }
}
</script>

<style scoped>

.buttons {
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
