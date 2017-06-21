<template>
    <div>
        <div>Claw: {{Math.round(data.claw.power * 100)}}%</div>
        <hr />
        <div>Fountain Tool (Positive Close): {{Math.round(data.fountain_tool.power * 100)}}%</div>
        <hr />
        <div>Valve Turner: {{Math.round(data.valve_turner.power * 100)}}%</div>
    </div>
</template>

<script>
    export default {
        name: 'tool-info',
        props: ['data']
    }
</script>