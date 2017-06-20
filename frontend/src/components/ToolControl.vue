<template>
    <div>
        <h1>Tool Control Scaling:</h1>
        <hr>
        <SliderControl name="Claw Master" :model.sync="data.claw.master" :invert.sync="data.claw.invert" min="0" max="100" />
        <SliderControl name="Claw Open" :model.sync="data.claw.open" min="0" max="100" />
        <SliderControl name="Claw Close" :model.sync="data.claw.close" min="0" max="100" />
        <hr />

        <SliderControl name="Valve Turner" :model.sync="data.valve_turner.power" :invert.sync="data.valve_turner.invert" min="0" max="65" />
        <hr />

        <SliderControl name="Fountain Tool" :model.sync="data.fountain_tool.power" :invert.sync="data.fountain_tool.invert" min="0" max="50" />
        </div>
    </div>
</template>

<script>
    var SliderControl = require('./SliderControl.vue')

    export default {
        name: 'ToolControl',
        components: {
            SliderControl
        },
        props: ['data']
    }
</script>