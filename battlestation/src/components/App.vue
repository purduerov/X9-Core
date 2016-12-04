<template>
    <div id="app">
        <div id="navbar">
            <Navbar title="Purdue ROV | BattleStation"></Navbar>
        </div>
        <div id="main-container">
            <div id="camera-view">
                <CameraView></CameraView>
            </div>
            <IMU imuhead="ROV inertia status: "></IMU>
        </div>
    </div>
</template>

<script>
var Navbar = require("./Navbar.vue")
var CameraView = require("./CameraView.vue")
var IMU = require("./IMU.vue")
var Pressure = require("./Pressure.vue")
var Thrusters = require("./Thrusters.vue")


export default {
  components: {
    Navbar,
    CameraView,
    IMU,
    Pressure,
    Thrusters
  }
}
</script>

<style scoped>
#app {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    width: 100%;
    height: 100%;
}

#navbar {
    height: 50px;
}

#main-container {
    position: fixed;
    top: 70px;
    left: 6px;
    right: 6px;
    bottom: 6px;
    background-color: cadetblue;
    margin: 0;
}

#camera-view {
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 200px;
}

#IMU-orient {
  position: absolute;
  top: 0;
  right: 0;
  height: 400px;
  width: 150px;
}
</style>
