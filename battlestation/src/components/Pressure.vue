<template>
    <div id="Pressure-orient">
        <p>{{ pressurehead }}</p>
        <ul id="pressure-stats">
            <li v-for="item in moving">
                {{ item.head+item.val }}
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'pressure-orient',
        props: ['pressurehead'],
        data: function() {
            return {
                moving: [
                    { head: "Pressure: ", val: 0 + " bars" },
                    { head: "Temperature: ", val: 0 + " Celcius" }
                ]
            }
        },
        methods: {
            update: function(info) {
                console.log('update')
                var titles = ["pressure", "temperature"];
                this.moving[0].val = info[titles[0]];
                this.moving[1].val = info[titles[1]];
            }
        },
        mounted: function() {
            setInterval(this.update, 500)
        }
    }
</script>