<template>
    <div id="Gamepad">
        <h5>Gamepad:</h5>
        <hr>
        <h6>Buttons:</h6>
        <ul v-for="(value, key) in data.buttons">
            <li>{{key}}: {{value}}</li>
        </ul>
        <hr>
        <h6>Left:</h6>
        <ul v-for="(value, key) in data.axes.left">
            <li>{{key}}: {{value}}</li>
        </ul>
        <hr>
        <h6>Right:</h6>
        <ul v-for="(value, key) in data.axes.right">
            <li>{{key}}: {{value}}</li>
        </ul>
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
</style>
