<template>
    <div id="Gamepad">
        <h1>Gamepad</h1>
        <hr>
        <div class="gamepad">
          <ul v-for="(value, key) in data.buttons">
              <li>{{key}}: {{value}}</li>
          </ul>
          <hr>
          <p>left:</p>
          <div class="gp_axis">
            <ul v-for="(value, key) in data.axes.left">
                <li>{{key}}: {{value}}</li>
            </ul>
          </div>
          <hr>
          <p>right:</p>
          <div class="gp_axis">
            <ul v-for="(value, key) in data.axes.right">
                <li>{{key}}: {{value}}</li>
            </ul>
          </div>
        </div>
    </div>
</template>

<script>
    export default {
        props: ['data']
    }
</script>

<style scoped>
h1 {
    font-weight: 400;
}

.gamepad {
  border: 2px solid grey;
}

.gp_axis {
  padding: 50px;
}
</style>