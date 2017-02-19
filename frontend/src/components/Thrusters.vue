<template>
    <div>
        <h5>Thrusters:</h5>
        <hr>
        <ul v-for="(value, key) in data">
            <li>{{key}}: </br>
                <p class="thruster_data">
                   Active: {{value.active}}</br>
                   Target: {{value.target}}</br>
                   Current: {{value.current}}</br>
                   PWM: {{value.pwm_actual}}</p>
            </li>
            <hr>
        </ul>
    </div>
</template>

<script>
    export default {
        props: ['data']
    }
</script>

<style scoped>
.thruster_data {
  padding-left: 8px;
}

h1 {
    font-weight: 400;
}
</style>
