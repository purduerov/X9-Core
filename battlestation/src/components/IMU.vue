<template>
  <div id="IMU-orient">
    <p>{{ imuhead }}</p>
    <ul id="imu-stats">
      <status-item v-for="item in moving" v-bind:status="item"></status-item>
    </ul>
  </div>
</template>

<script>
  window.onload = function() {
    Vue.component("status-item", {
      props: ["status"],
      template: "<li>{{ status.head+status.val }}</li>"
    });
    var status = new Vue({
      el: "#imu-stats",
      data: {
        moving: [
          { head: "Forward: ", val: 0 },
          { head: "Right: ", val: 0 },
          { head: "Up: ", val: 0 },
          { head: "Rotating ", val: "up: "+0 },
          { head: "Roll ", val: "right: "+0 },
          { head: "Turning ", val: "right: "+0 }
        ]
      },
      methods: {
        update: function(info) {
          var titles = ["x", "y", "z", "pitch", "roll", "yaw"];
          var i = 0;
          for(i; i < 3; i++) {
            orient.moving[i].val = info[titles[i]];
          }
          if(info[titles[i]] >= 0) {
            orient.moving[i].val = "up: "+info[titles[i]];
          } else {
            orient.moving[i].val = "down: "+(-info[titles[i]]);
          }
          i++;
          
          for(i; i < 6; i++) {
            if(info[titles[i]] >= 0) {
              orient.moving[i].val = "right: "+info[titles[i]];
            } else {
              orient.moving[i].val = "left: "+(-info[titles[i]]);
            }
          }
        }
      }
    });
  }
 
  export default {
    name: 'imu-orient',
    props: ['imuhead']
  }
</script>