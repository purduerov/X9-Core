<template>
    <div id="camera-view">
        <div class="image">
            <img :src="source" :style="transform(flipped[port])">
        </div>
        <button id="flip" @click="flip">Flip</button>
        <div class="buttons">
            <button v-for="(cam,name) in data" 
                :key="name" 
                @click="changePort(cam.port)" 
                :class="cam.status">
                    {{name}}
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'camera-view',
    props: ['data', 'status'],
    data: function() {
        return {
            port: 8080,
            flipped: {}
        }
    },
    methods: {
        changePort: function(newPort) {
            this.port = newPort

            let newStatus = {}
            for (let [name, cam] of Object.entries(this.data)) {
                // temporarily lets keep all cameras active. Suspending and restarting
                // needs to be a little better handled on the rov side.
                // newStatus[cam.port] = this.port == cam.port ? 'active' : 'suspended'

                newStatus[cam.port] = 'active'
            }
            this.$emit('update:status', newStatus)
        },
        flip: function() {
            if (this.port in this.flipped) {
                this.flipped[this.port] = (this.flipped[this.port] + 1) % 4
            } else {
                this.flipped[this.port] = 1
            }
        },
        transform: function(num) {
            num = num || 0
            return {'transform': `rotate(${num*90}deg)`}
        }
    },
    computed: {
        source: function() {
            return `http://raspberrypi.local:${this.port}/?action=stream`
        }
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

button.killed {
    background-color: red;
}

button.active {
    background-color: green;
}

button.suspended {
    background-color: orange;
}

#camera-view {
    position: relative;
    height: 100%;
    width: 100%;
}

#flip {
    position: absolute;
    right: 0;
    top: 0;
    width: 100px;
    z-index: 999;
}

.flipped {
    transform: rotate(180deg);
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