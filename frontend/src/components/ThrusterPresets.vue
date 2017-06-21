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
                    'Health Task': () => {
                        Object.assign(config.thrust_scales, {
                            velX: 20,
                            pitch: 25
                        })
                    },
                    'Invert': function() {
                        Object.assign(config.thrust_invert, {
                            velX: !config.thrust_invert.velX,
                            velY: !config.thrust_invert.velY,
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