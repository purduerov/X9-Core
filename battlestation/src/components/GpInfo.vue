<template>
  <div id="gp-describe">
    <p>{{ gphead }}</p>
    <ul id="btn-status">
      <li v-for="item in buttons">
        {{ buttons.name+": "+buttons.val }}
      </li>
    </ul>
    <ul id="axes-status">
      <li v-for="item in axes">
        <p>{{ axes.name+":" }}</p>
        <p class="gp_ax_sub">{{ axes.left.x }}</p>
        <p class="gp_ax_sub">{{ axes.left.y }}</p>
        <p class="gp_ax_sub">{{ axes.left.r }}</p>
        <p class="gp_ax_sub">{{ axes.left.theta }}</p>
      </li>
    </ul>
  </div>
</template>


<script>
  export default {
    name: 'gp-describe',
    props: ['gphead'],
    data: function() {
      return {
        buttons: [],
        axes: []
        }
      },
    methods: {
      update_gp: function() {
          var that = this;
          console.log(this.buttons);
          console.log(this.axes);
          Object.keys(gp.buttons).forEach(function(key_b, i) {
            that.buttons[i] = { name: key_b, val: gp.buttons[key_b].val };
          });
          Object.keys(gp.axes).forEach(function(key_a, i) { //updates the axes 
            that.axes[i] = {name: key_a, stats: {} };
            Object.keys(gp.axes[key_a]).forEach(function(key_s, j) {
              that.axes[i].stats[key_s] = gp.axes[key_a][key_s];
            });
          });
      }
    },
    mounted: function() {
      setInterval(this.update_gp, 500);
    }
  }
</script>