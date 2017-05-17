<template>
    <div>
        <h1>Tool Control Scaling:</h1>
        <hr>
        <div class="trst">
            <div class="info">
                <span>Claw</span>
                <div>
                    <span>Master: {{data.claw.master}}%</span>
                    <input type="range" min="0" max="100" v-model="data.claw.master">
                </div>
                <hr/>
                <div class="tool_sub">
                    <div>
                        <span>Open: {{data.claw.open}}%</span>
                        <input type="range" min="0" max="100" v-model="data.claw.open">
                    </div>
                    <div>
                        <span>Close: {{data.claw.close}}%</span>
                        <input type="range" min="0" max="100" v-model="data.claw.close">
                    </div>
                </div>
                <div>
                    <span>Valve Turner: {{data.vlv_turn.main}}%</span>
                    <input type="range" min="0" max="65" v-model="data.vlv_turn.main">
                </div>
                <div>
                    <span>Fountain Tool: {{data.fountain.main}}%</span>
                    <input type="range" min="0" max="50" v-model="data.fountain.main">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'ToolControl',
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

.tool_sub {
    padding: 50px;
}
</style>
