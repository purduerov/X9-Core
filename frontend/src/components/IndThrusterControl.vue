<template>
    <div>
        <div class="half">
            <SliderControl v-for="i in [0,4,6,2]" :name="`Thruster ${i+1}`"
                :model.sync="data[i].power" :invert.sync="data[i].invert" min="0" max="100" />
        </div>
        <div class="half right">
            <SliderControl v-for="i in [1,5,7,3]" :name="`Thruster ${i+1}`"
                :model.sync="data[i].power" :invert.sync="data[i].invert" min="0" max="100" />
        </div>
    </div>
</template>

<script>
    var SliderControl = require('./SliderControl.vue')

    export default {
        components: {
            SliderControl
        },
        props: ['data']
    }
</script>

<style scoped> 
    .half {
        width: calc(50% - 10px);
        float: left;
        box-sizing: border-box;
    }

    .right {
        float: right;
    }
</style>