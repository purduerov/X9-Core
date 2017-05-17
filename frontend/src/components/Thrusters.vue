<template>
    <div>
        <h1>Thrusters:</h1>
        <hr>
        <div class="trst">
            <div class="left">
                <ul>
                    <li>t1: {{Math.round(data[0] * 100)}}% <hr /></li>
                    <li>t5: {{Math.round(data[4] * 100)}}% <hr /></li>
                    <li>t7: {{Math.round(data[6] * 100)}}% <hr /></li>
                    <li>t3: {{Math.round(data[2] * 100)}}% <hr /></li>
                </ul>
            </div>
            <div class="right">
                <ul>
                    <li>t2: {{Math.round(data[1] * 100)}}% <hr /></li>
                    <li>t6: {{Math.round(data[5] * 100)}}% <hr /></li>
                    <li>t8: {{Math.round(data[7] * 100)}}% <hr /></li>
                    <li>t4: {{Math.round(data[3] * 100)}}% <hr /></li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'thrusters',
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

.left {
    display: flex;
    width: 50%;
    height: 100%;
    flex-direction: column;
}

.right {
    display: flex;
    width: 50%;
    height: 100%;
    flex-direction: column;
}

.trst {
    display: flex;
    flex-direction: row;
}
</style>
