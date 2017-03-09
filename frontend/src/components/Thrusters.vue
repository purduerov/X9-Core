<template>
    <div>
        <h1>Thrusters:</h1>
        <hr>
        <div class="trst">
            <div  class="left">
                <ul v-for="n in 4">
                    <li>t{{n}}: </br>
                        <p class="thruster_data">
                            Active: {{data["t"+(n-1)].active}}</br>
                            Current: {{data["t"+(n-1)].current}}
                        </p>
                    </li>
                    <hr>
                </ul>
            </div>
            <div  class="right">
                <ul v-for="n in 4">
                    <li>t{{n+4}}: </br>
                        <p class="thruster_data">
                            Active: {{data["t"+(n+3)].active}}</br>
                            Current: {{data["t"+(n+3)].current}}
                        </p>
                    </li>
                    <hr>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['data'],
        mounted: function() {
            console.log(Object.keys(this.data));
        }
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