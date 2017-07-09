<template>
    <div id="container">
        <button v-for="(func, task) in presets" @click="func">{{task}}</button>
    </div>
</template>

<script>
    // thrust_scales: {
    //     master: 50, velX: 60, velY: 50,
    //     velZ: 60, pitch: 35,
    //     roll: 35, yaw: 25,
    // },
    // thrust_invert: {
    //     master: false, velX: false, velY: false,
    //     velZ: false, pitch: false,
    //     roll: false, yaw: false,
    // },

    export default {
        props: ['config'],
        data: function() {
            let config = this.config
            return {
                presets: {
                    'Default': () => {
                        Object.assign(config.thrust_scales, {
                            master: 50, velX: 60, velY: 50,
                            velZ: 60, pitch: 35,
                            roll: 35, yaw: 25,
                        })
                        Object.assign(config.thrust_invert, {
                            master: false, velX: false, velY: false,
                            velZ: false, pitch: false,
                            roll: false, yaw: false,
                        })
                    },
                    'Slow': () => {
                        Object.assign(config.thrust_scales, {
                            master: 20
                        })
                    },
                    'Medium': () => {
                        Object.assign(config.thrust_scales, {
                            master: 40
                        })
                    },
                    'Fast': () => {
                        Object.assign(config.thrust_scales, {
                            master: 60
                        })
                    },
                    'Invert': function() {
                        Object.assign(config.thrust_invert, {
                            velX: !config.thrust_invert.velX,
                            velY: !config.thrust_invert.velY,
                            pitch: !config.thrust_invert.pitch,
                            roll: !config.thrust_invert.roll,
                            yaw: !config.thrust_invert.yaw
                        })
                    },
                    'Half': function() {
                        Object.assign(config.thrust_scales, {
                            master: Math.round(config.thrust_scales.master/2),
                        })
                    },
                    'Double': function() {
                        Object.assign(config.thrust_scales, {
                            master: Math.min(config.thrust_scales.master*2, 70),
                        })
                    },
                    'Fountain': function() {
                        Object.assign(config.thrust_scales, {
                            velX: 35,
                            velY: 35,
                            yaw: 15
                        })
                    },
                }
            }
        }
    }
</script>

<style scoped>
#container {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}
</style>
