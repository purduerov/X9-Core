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
        {{ axes.name+": "+axes.val }}
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
      update: function() {
            console.log(Object.getOwnPropertyNames(this));
          Object.keys(gp.buttons).forEach(function(key_b, i) {
            console.log(key_b);
            this.buttons[i] = { name: key_b, val: gp.buttons[key_b].val };
          });
          Object.keys(gp.axes).forEach(function(key_a, i) {
            console.log(key_a);
            this.axes[i] = { name: key_a, val: gp.buttons[key_a].val };
          });
      }
    },
    mounted: function() {
      setInterval(this.update, 500);
    }
  }
</script>