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
                    <Press_Temp :data="packet.PRESSURE"></Press_Temp>
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
var Press_Temp = require("./Pressure.vue")

export default {
    components: {
        Navbar,
        CameraView,
        IMU,
        Card,
        DataView,
        Press_Temp
    },
    data: function() {
        return {
            packet: {
            IMU: {
              x: 3,
              y: 4,
              z: 2,
              pitch: 6,
              roll: -4,
              yaw: .243
            },
            PRESSURE: {
              pressure: 7,
              temperature: 4
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
        var vm = this;
        
        gp.vue = vm;
        
        var go1 = -1;
        var go2 = -1;
        var send = {};
        gp.set();
        go1 = window.setInterval(function() {
            if(gp.ready) {
                window.clearInterval(go1);
                go1 = -1;
                bind.activate();
                go2 = window.setInterval(function() {
                  gp.get_current();
                });
            }
        });

        var socket = io.connect('http://' + document.domain + ':' + location.port);

        var app_refresh = setInterval(function() {
            socket.emit("dearflask", JSON.stringify({buttons: gp.buttons, axes: gp.axes}));
        }, 50);
        socket.on("dearclient", function(status) {
            Object.keys(status).forEach(function(key, i) {
                vm.packet[key] = status[key];
            });
            //setTimeout(function() {
                //console.log(vm.packet);
            //}, 10);
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
