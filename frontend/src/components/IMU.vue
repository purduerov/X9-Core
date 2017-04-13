<template>
    <div>
        <h1>Sensors:</h1>
        <hr>
        <p>IMU:</p>
        <ul v-for="(value, key) in data.IMU">
            <li>{{key}}: {{value}}</li>
        </ul>
        <hr>
        <p>Pressure: {{ data.PRESSURE.pressure }}</p>
        <hr>
        <p>Temperature: {{ data.PRESSURE.temperature }}</p>
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
li {
    padding: 4px 0px
}
</style>
