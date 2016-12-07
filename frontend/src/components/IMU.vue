<template>
  <div id="IMU-orient">
    <p>Hello~</p>
    <ul v-for="(value, key) in data">
        <li>{{key}}: {{Math.round(value*1000)/1000.0}}</li>
    </ul>
  </div>
</template>

<script>
    export default {
        name: 'imu-orient',
        props: ['data']
    }
</script>
