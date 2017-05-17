<template>
    <div>
        <h1>Tools:</h1>
        <hr>
        <div class="trst">
            <div class="info">
                <ul>
                    <li>Claw: {{Math.round(data.claw.power * 100)}}% <hr /></li>
                    <li>Fountain Tool: {{Math.round(data.fountain_tool.power * 100)}}% <hr /></li>
                    <li>Valve Turner: {{Math.round(data.valve_turner.power * 100)}}% <hr /></li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'tool-info',
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
