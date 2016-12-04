<template>
    <div id="Thrusters-orient">
        <p>{{ thrustershead }}</p>
        <ul id="thrusters-stats">
            <li v-for="item in moving">
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
        methods: {
            update: function(info) {
                console.log('update')
                var titles = ["t0", "t1", "t2", "t3", "t4", "t5", "t6", "t7"];
                for (var i = 0; i < 8; i++) {
                    this.moving[i].val = info[titles[i]];
                    if (info[titles[i]] >= 0) {
                    this.moving[i].val = "Increasing "+info[titles[i]];
                } else {
                    this.moving[i].val = "Decreasing "+(-info[titles[i]]);
                }
                }

            }
        },
        mounted: function() {
            setInterval(this.update, 500)
        }
    }
</script>