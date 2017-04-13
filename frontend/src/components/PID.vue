<template>
    <div>
        <h1>PID Controllers:</h1>
        <hr>
        <input type="checkbox" id="x_lock" value="false" v-model="data.x_lock">
        <label for="x_lock">Lock X-Axis</label>
        </br>
        <input type="checkbox" id="y_lock" value="false" v-model="data.y_lock">
        <label for="y_lock">Lock Y-Axis</label>
        </br>
        <input type="checkbox" id="z_lock" value="false" v-model="data.z_lock">
        <label for="z_lock">Lock Z-Axis</label>
        </br>
        <input type="checkbox" id="roll_lock" value="false" v-model="data.roll_lock">
        <label for="roll_lock">Lock Roll-Axis</label>
        </br>
        <input type="checkbox" id="pitch_lock" value="false" v-model="data.pitch_lock">
        <label for="pitch_lock">Lock Pitch-Axis</label>
        </br>
        <input type="checkbox" id="yaw_lock" value="false" v-model="data.yaw_lock">
        <label for="yaw_lock">Lock Yaw-Axis</label>
    </div>
</template>

<script>
    export default {
        props: ['data']
    }
</script>

<style scoped>
h1 {
    font-weight: 400;
}

input[type="checkbox"] {
    width: 30px;
    height: 30px;
}

label {
    margin: 10px 0px;
}
</style>
