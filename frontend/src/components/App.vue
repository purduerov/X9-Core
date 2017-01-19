<template>
    <div id="app">
        <div id="navbar">
            <Navbar title="Purdue ROV - BattleStation"></Navbar>
        </div>
        <div id="main-container">
            <Card class="camera-width full-height">
                <CameraView></CameraView>
            </Card>
            <div style="width: calc(100% - 800px); height: 100%; float: left">
                <Card class="half-width half-height">
                    <IMU :data="packet.IMU"></IMU>
                </Card>
                <Card class="half-width half-height">
                    <DataView title="Pressure:" :data="packet.pressure"></DataView>
                </Card>
                <Card class="half-width half-height">
                    <IMU :data="packet.IMU"></IMU>
                </Card>
                <Card class="half-width half-height">
                    <IMU :data="packet.IMU"></IMU>
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
            packet: {
            IMU: {
              x: 0,
              y: 0,
              z: 0,
              pitch: 0,
              roll: 0,
              yaw: 0
            },
            PRESSURE: {
              pressure: 0,
              temperature: 0
            },
            Thrusters: {
              t0 : { power: "0"},
              t1 : { power: "0"},
              t2 : { power: "0"},
              t3 : { power: "0"},
              t4 : { power: "0"},
              t5 : { power: "0"},
              t6 : { power: "0"},
              t7 : { power: "0"}
            }
          }
        };
    },
    mounted: function() {
        var vm = this

        var socket = io.connect('http://' + document.domain + ':' + location.port);

        socket.on('connect', function () {
            console.log("connected")
        });

        socket.on("dearflask", function(d) {
            vm.packet = d
            setTimeout(function() {
                socket.emit("dearclient")
            }, 10);
        });
        
        console.log(vm.packet);
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
</style>
