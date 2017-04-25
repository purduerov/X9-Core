<template>
    <div>
        <h1>Thruster Scaling:</h1>
        <hr>
        <div class="trst">
            <div class="info">
                <div>
                    <span>Master</span>
                    <input type="range" min="-1" max="100" v-model="data.master">
                </div>
                <div>
                    <span>Forward / Backward</span>
                    <input type="range" min="-1" max="100" v-model="data.velX">
                </div>
                <div>
                    <span>Strafe</span>
                    <input type="range" min="0" max="100" v-model="data.velY">
                </div>
                <div>
                    <span>Ascend/Descend</span>
                    <input type="range" min="0" max="100" v-model="data.velZ">
                </div>
                <div>
                    <span>Pitch / Roll</span>
                    <input type="range" min="0" max="100" v-model="data.pitchRoll">
                </div>
                <div>
                    <span>Yaw</span>
                    <input type="range" min="0" max="100" v-model="data.yaw">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'ThrusterControl',
        props: ['data']
    }
</script>

<style scoped>
h1 {
    font-weight: 400;
}

.thruster_data {
    padding-left: 8px;
}

.info {
    width: 100%;
    height: 100%;
}

.trst {
    display: flex;
    flex-direction: row;
}
</style>
