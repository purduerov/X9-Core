<template>
    <div id="app">
        <div id="navbar">
            <Navbar title="Purdue ROV - BattleStation"></Navbar>
        </div>
        <div id="main-container">
            <Card color="#FF9800" class="camera-width full-height">
                <CameraView></CameraView>
            </Card>
            <div style="width: calc(100% - 800px); height: 100%; float: left">
                <Card color="#FFC107" class="half-width half-height">
                    <IMU :data="data.imu"></IMU>
                </Card>
                <Card class="half-width half-height">
                    <DataView title="Pressure:" :data="data.pressure"></DataView>
                </Card>
                <Card color="#00BCD4" class="half-width half-height">
                    <IMU :data="data.imu"></IMU>
                </Card>
                <Card color="#E91E63" class="half-width half-height">
                    <IMU :data="data.imu"></IMU>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
var Navbar = require("./Navbar.vue")
var CameraView = require("./CameraView.vue")
var IMU = require("./IMU.vue")
var DataView = require("./DataView.vue")
var Card = require("./Card.vue")

export default {
    components: {
        Navbar,
        CameraView,
        IMU,
        Card,
        DataView
    },
    data: function() {
        return {
            data: {}
        }
    },

    mounted: function() {
        var vm = this

        var socket = io.connect('http://' + document.domain + ':' + location.port);

        socket.on('connect', function () {
            console.log("connected")
        });

        socket.on("dearflask", function(d) {
            vm.data = d
            setTimeout(function() {
                socket.emit("dearclient")
            }, 10);
        });
    }
}
</script>

<style scoped>
#app {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    width: 100%;
    height: 100%;
    background-color: #f5f5f5;
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
</style>
