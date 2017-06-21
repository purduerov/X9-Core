<template>
    <div id="container"> 
        <div>
            <span>{{name}}: {{model}}%</span>
            <span v-if="invert !== undefined" style="float: right">
                <input type="checkbox" :checked="invert" @click="$emit('update:invert', !invert)">
                <label>Invert</label>
            </span>
        </div>
        <input type="range" :min="min" :max="max" :value="model" @input="$emit('update:model', $event.target.value)">
    </div>
</template>

<script>
    export default {
        name: 'SliderControl',
        props: ['name', 'model', 'invert', 'min', 'max']
    }
</script>

<style scoped>
#container {
    padding: 5px;
}
</style>