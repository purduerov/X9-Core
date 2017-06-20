<template>
    <div>
        <h1>Thruster Scaling:</h1>
        <hr>
        <SliderControl name="Master" 
            :model.sync="scales.master" min="0" max="70" />
        <SliderControl name="Forward/Back"
            :model.sync="scales.velX" :invert.sync="invert.velX" min="0" max="100" />
        <SliderControl name="Strafe"
            :model.sync="scales.velY" :invert.sync="invert.velY" min="0" max="100" />
        <SliderControl name="Ascend/Descend"
            :model.sync="scales.velZ" :invert.sync="invert.velZ" min="0" max="100" />
        <SliderControl name="Pitch"
            :model.sync="scales.pitch" :invert.sync="invert.pitch" min="0" max="100" />
        <SliderControl name="Roll"
            :model.sync="scales.roll" :invert.sync="invert.roll" min="0" max="100" />
        <SliderControl name="Yaw"
            :model.sync="scales.yaw" :invert.sync="invert.yaw" min="0" max="100" />
        </div>
    </div>
</template>

<script>
    var SliderControl = require('./SliderControl.vue')

    export default {
        name: 'ThrusterControl',
        components: {
            SliderControl
        },
        props: ['scales', 'invert']
    }
</script>