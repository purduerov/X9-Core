<template>
    <div id="camera-view">
        <div class="image">
            <img :src="source" :style="transform">
        </div>
        <div class="buttons">
            <button v-for="(cam,name) in data" :key="name" v-show="cam.status !== 'killed'"
              @click="changePort(cam.port)" :class="cam.status">{{name}}</button>
        </div>
        <div class="control-buttons">
            <button @click="flip" class="control-button" id="flip">⤽</button>
            <button @click="refresh" class="control-button" :disabled="refreshing">⟳</button>
        </div>
    </div>
</template>

<script>
let {shell, app, ipcRenderer} = window.require('electron');

export default {
    name: 'camera-view',
    props: ['data'],
    data: function() {
        return {
            port: 8080,
            last: 8080,
            transform: {},
            flipped: {},
            refreshing: false,
        }
    },
    methods: {
        changePort: function(newPort) {
            this.last = this.port
            this.port = newPort;

            ipcRenderer.send('cam2port-send', {"port": this.port, "last": this.last});

            let num = this.flipped[this.port] || 0
            this.transform = {'transform': `rotate(${num*90}deg)`}
        },
        window: function() {
            const {BrowserWindow} = window.require('electron').remote

            let win = new BrowserWindow({width: 1000, height: 800})
            win.on('closed', () => {
                win = null
            })
            win.loadURL(`file:///home/bmaxfie/ROV/X9-Core/frontend/src/line_draw/line_length.html`)
        },
        flip: function() {
            if (this.port in this.flipped) {
                this.flipped[this.port] = (this.flipped[this.port] + 1) % 4
            } else {
                this.flipped[this.port] = 1
            }

            let num = this.flipped[this.port] || 0
            this.transform = {'transform': `rotate(${num*90}deg)`}
        },
        refresh: function() {
            this.refreshing = true
            let prev_port = this.port
            this.port = 0

            setTimeout(() => {
                this.port = prev_port
                this.refreshing = false
            }, 300)
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
    width: calc(100% - 120px);
    height: 50px;
    display: flex;
    //justify-content: space-between;
}

.buttons > button {
    width: 20%;
    font-size: 30px;
    flex: 1;
}

.buttons > button.killed {
    background-color: red;
}

.buttons > button.active {
     /* background-color: green; */
}

.buttons > button.suspended {
    background-color: orange;
}

#camera-view {
    position: relative;
    height: 100%;
    width: 100%;
}

.control-buttons {
    position: absolute;
    bottom: 0;
    right: 0;
    height: 50px;
    width: 120px;
    display: flex;
    justify-content: space-between;
}
.control-button {
    width: 100%;
    flex: 1;
    font-size: 40px;
}

.flipped {
    transform: rotate(180deg);
}

#flip {
    transform: scaleX(-1);
}

.image {
    height: calc(100% - 50px);
    width: 100%;
    display: flex;
    align-items: center;
    overflow: hidden;
}

.image > img {
    max-height: 100%;
    max-width: 100%;
    height: 100%;
}
</style>
