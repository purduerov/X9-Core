<template>
    <div id="Press_Temp">
        <div class="press_temp_box">
            <p>Pressure: {{data.pressure}}</p>
        </div>
        <hr>
        <div class="press_temp_box">
            <p>Temperature: {{data.temperature}}</p>
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
.press_temp_box {
  border: 1px black solid;
  padding: 4px;
}
</style>