<template>
    <div id="app">
        <div id="navbar">
            <Navbar title="Purdue ROV - BattleStation"></Navbar>
        </div>
        <div id="main-container">
            <Card class="camera-width full-height">
                <CameraView></CameraView>
            </Card>
            <div class="data-width full-height">
                <!-- 
                <Card class="half-width half-height">
                    <IMU :data="packets.dearclient.IMU"></IMU>
                </Card>
                <Card class="half-width half-height">
                    <Press_Temp :data="packets.dearclient.pressure"></Press_Temp>
                </Card>
                <Card class="half-width half-height">
                    <GpInfo :data="gpinfo"></GpInfo>
                </Card> -->
                <Card class="half-width half-height">
                    <Thruster :data="packets.dearclient.thrusters"></Thruster>
                </Card>
                <Card class="half-width half-height">
                    <ToolInfo :data="packets.dearflask"></ToolInfo>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
var Navbar = require("./components/Navbar.vue")
var CameraView = require("./components/CameraView.vue")
var IMU = require("./components/IMU.vue")
var DataView = require("./components/DataView.vue")
var Card = require("./components/Card.vue")
var Press_Temp = require("./components/Pressure.vue")
var GpInfo = require("./components/GpInfo.vue")
var Thruster = require("./components/Thrusters.vue")
var ToolInfo = require("./components/ToolInfo.vue")

var packets = require("./packets.js")
var main = require("./main.js")

export default {
    components: {
        Navbar,
        CameraView,
        IMU,
        Card,
        DataView,
        Press_Temp,
        GpInfo,
        Thruster,
        ToolInfo
    },
    data: function() {
        return {
            packets: packets
        }
    },
    mounted: function() {
        main(this.packets)
    }
}
</script>

<style scoped>
#app {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    width: 100%;
    height: 100%;
    background-color: #1a1a1a;
    font-weight: 100;
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
    margin: 0;
}

.half-width {
    width: 50%;
    float: left;
}

.half-height {
    height: 50%;
    float: left;
}

.full-height {
    height: 100%;
    float: left;
}

.camera-width {
    width: 800px;
}
.data-width {
    width: calc(100% - 800px)
}
</style>
