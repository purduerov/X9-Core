<template>
    <div>
        <h1>Thruster Scaling:</h1>
        <hr>
        <div class="trst">
	  <div class="info">
                <div>
                    <span>Master: {{data.master}}%</span>
                    <input type="range" min="0" max="70" v-model="data.master">
		</div>
                <div>
                    <span>Forward/Backward: {{data.velX}}%</span>
                    <input type="range" min="0" max="100" v-model="data.velX">
                </div>
                <div>
                    <span>Strafe: {{data.velY}}%</span>
                    <input type="range" min="0" max="100" v-model="data.velY">
                </div>
                <div>
                    <span>Ascend/Descend: {{data.velZ}}%</span>
                    <input type="range" min="0" max="100" v-model="data.velZ">
                </div>
                <div>
                    <span>Pitch/Roll: {{data.pitchRoll}}%</span>
                    <input type="range" min="0" max="100" v-model="data.pitchRoll">
                </div>
                <div>
                    <span>Yaw: {{data.yaw}}%</span>
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
