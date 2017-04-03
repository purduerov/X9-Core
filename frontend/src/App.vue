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
                    <GpInfo :data="gpinfo"></GpInfo>
                </Card>
                <Card class="half-width half-height">
                    <Thruster :data="packet.Thrusters"></Thruster>
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
var gp = require("./gamepad/gp_library.js")
var controls = require("./controls.js")

export default {
    components: {
        Navbar,
        CameraView,
        IMU,
        Card,
        DataView,
        Press_Temp,
        GpInfo,
        Thruster
    },
    data: function() {
        return {
            packet: {
                IMU: {
                    x: 3, y: 4, z: 2, pitch: 6, roll: -4, yaw: .243
                },
                PRESSURE: {
                    pressure: 7, temperature: 4
                },
                Thrusters: {
                    t0 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    t1 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    t2 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    t3 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    t4 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    t5 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    t6 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    t7 : { active: 0, target: 0.0, current: 0.0, pwm_actual: 0}
                }
            },
            gpinfo: {
                buttons: { a: 0, b: 0, x: 0, y: 0 },
                axes: {
                    left: { x: 0, y: 0 },
                    right: { x: 0, y: 0 }
                }
            },
        };
    },
    mounted: function() {
        var vm = this;

        window.vue_app = vm;

        gp.set(undefined, function() {
            console.log("And done..")
            window.setInterval(function() {
                gp.get_current()
            }, 20)
        });

        var socket = io.connect('http://' + document.domain + ':' + location.port);

        var send = {};
        var app_refresh = setInterval(function() {
            if(gp.ready) {
                var send = JSON.stringify(controls);
                //console.log(send);
                socket.emit("dearflask", send);
            }
        }, 50);
        socket.on("dearclient", function(status) {
            data = JSON.parse(status);
            console.log(data);
            Object.keys(data).forEach(function(key, i) {
                vm.packet[key] = status[key];
            });
            //setTimeout(function() {
                //console.log(vm.packet);
            //}, 10);
        });
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
