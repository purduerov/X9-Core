<template>
  <div id="IMU-orient">
    <p>{{ imuhead }}</p>
    <ul id="imu-stats">
      <li v-for="item in moving">
        {{ item.head+item.val }}
      </li>
    </ul>
  </div>
</template>

<script>
    export default {
        name: 'imu-orient',
        props: ['imuhead'],
        data: function() {
            return {
                moving: [
                    { head: "Forward: ", val: 0 },
                    { head: "Right: ", val: 0 },
                    { head: "Up: ", val: 0 },
                    { head: "Rotating ", val: "up: "+0 },
                    { head: "Roll ", val: "right: "+0 },
                    { head: "Turning ", val: "right: "+0 }
                ]
            }
        },
        methods: {
            update: function(info) {
                console.log('update')
                var titles = ["x", "y", "z", "pitch", "roll", "yaw"];
                var i = 0;
                for (i; i < 3; i++) {
                    orient.moving[i].val = info[titles[i]];
                }
                if (info[titles[i]] >= 0) {
                    orient.moving[i].val = "up: "+info[titles[i]];
                } else {
                    orient.moving[i].val = "down: "+(-info[titles[i]]);
                }
                i++;

                for (i; i < 6; i++) {
                    if (info[titles[i]] >= 0) {
                        orient.moving[i].val = "right: "+info[titles[i]];
                    } else {
                        orient.moving[i].val = "left: "+(-info[titles[i]]);
                    }
                }
            }
        },
        mounted: function() {
            setInterval(this.update, 500)
        }
    }
</script>
