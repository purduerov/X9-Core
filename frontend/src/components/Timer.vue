<template>
<div>
    <h1>Timer</h1>
    <hr>
    <h1 id="timer" :class="{orangeText: minutes >= 13, redText: minutes >= 15}">
        <span>{{minutes}}</span>:<span>{{seconds}}</span>
    </h1>
    <br>
    <div class="buttons">
        <button v-if="!running"     @click="start()">Start</button>
        <button v-if="running"      @click="pause()">Pause</button>
        <button :disabled="running" @click="reset()">Reset</button>
    </div>
</div>
</template>

<script>
export default {
    data: function() {
        return {
            timer_interval: -1,
            start_time: 0,
            delta: 0,
            running: false,
            paused_at: 0
        }
    },
    methods: {
        start: function() {
            this.start_time = Date.now() - this.paused_at
            this.delta = this.paused_at
            this.timer_interval = setInterval(this.update.bind(this), 0.1)
            this.running = true
        },
        pause: function() {
            this.paused_at = this.delta
            this.running = false

            clearInterval(this.timer_interval)
        },
        reset: function() {
            this.paused_at = 0
            this.delta = 0
            this.running = false

            clearInterval(this.timer_interval)
        },
        update: function() {
            this.delta = Date.now() - this.start_time
        }
    },
    computed: {
        minutes: function() {
            let minutes = Math.floor(this.delta / 1000 / 60)
            return (minutes < 10) ? "0" + minutes : minutes
        },
        seconds: function() {
            let seconds = Math.floor(this.delta / 1000 % 60)
            return (seconds < 10) ? "0" + seconds : seconds
        }
    }
}
</script>

<style scoped>
#timer {
    font-family: monospace;
    width: 100%;
    text-align: center;
    font-size: 70px;
    font-weight: bold;
}

.orangeText {
    color: orange;
}

.redText {
    color: red;
}

.buttons {
    text-align: center;
    width: 100%;
}

.buttons > button {
    width: 150px;
    background-color: grey;
    height: 30px;
}

.buttons > button:disabled {
    background-color: darkgrey;
    color: grey;
}

</style>