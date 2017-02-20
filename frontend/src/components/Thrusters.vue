<template>
    <div>
        <h5>Thrusters:</h5>
        <hr>
        <div v-for="(t,i) in data">
            <ul>
                <li>Thruster: {{i+1}}</li>
                <li>Val: {{t}}</li>
                <!--<li>Active: {{t.active}}</li>-->
                <!--<li>Target: {{t.target}}</li>-->
                <!--<li>Current: {{t.current}}</li>-->
                <!--<li>PWM: {{t.pwm_actual}}</li>-->
            </ul>
            <hr>
        </div>
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
