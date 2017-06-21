<template>
    <div>
        <div class="container">
            <div class="horizontal">
                <ThrusterCircle class="top-left" :value="Math.round(data[0] * 100)"/>
                <ThrusterCircle class="top-right" :value="Math.round(data[1] * 100)"/>
                <ThrusterCircle class="bottom-left" :value="Math.round(data[2] * 100)"/>
                <ThrusterCircle class="bottom-right" :value="Math.round(data[3] * 100)"/>
            </div>
            <div class="vertical">
                <ThrusterCircle class="top-left" :value="Math.round(data[4] * 100)"/>
                <ThrusterCircle class="top-right" :value="Math.round(data[5] * 100)"/>
                <ThrusterCircle class="bottom-left" :value="Math.round(data[6] * 100)"/>
                <ThrusterCircle class="bottom-right" :value="Math.round(data[7] * 100)"/>
            </div>
        </div>
    </div>
</template>

<script>
    var ThrusterCircle = require("./ThrusterCircle.vue")

    export default {
        name: 'thrusters',
        components: {
            ThrusterCircle
        },
        props: ['data'],
    }
</script>

<style scoped>
.container {
    position: relative;
    width: 100%;
    height: 240px;
}

.horizontal {
    position: relative;
    width: 240px;
    height: 240px;
    margin: 0 auto;
}

.vertical {
    position: relative;
    width: 140px;
    height: 140px;
    margin: 0 auto;
    transform: translateY(-190px);
}

.top-left {
    position: absolute;
    top: 0;
    left: 0;
}

.top-right {
    position: absolute;
    top: 0;
    right: 0;
}

.bottom-left {
    position: absolute;
    bottom: 0;
    left: 0;
}

.bottom-right {
    position: absolute;
    bottom: 0;
    right: 0;
}
</style>