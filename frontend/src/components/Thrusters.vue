<template>
    <div id="Thrusters-orient">
        <p>{{ thrustershead }}</p>
        <ul id="thrusters-stats">
            <li v-for="thruster power changing">
                {{ item.head+item.val }}
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'thrusters-orient',
        props: ['thrustershead'],
        data: function() {
            return {
                moving: [
                    { head: "t0 ", val: "Power: " + 0},
                    { head: "t1: ", val: "Power: " + 0},
                    { head: "t2: ", val: "Power: " + 0 },
                    { head: "t3: ", val: "Power: " + 0 },
                    { head: "t4: ", val: "Power: " + 0 },
                    { head: "t5: ", val:  "Power: " + 0 },
                    { head: "t6: ", val: "Power: " + 0 },
                    { head: "t7: ", val: "Power: " + 0 }
                ]
            }
        },
        mounted: function() {
            setInterval(this.update, 500)
        }
    }
</script>