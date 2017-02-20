<template>
    <div id="app">
        <div id="navbar">
            <Navbar title="Purdue ROV - BattleStation"></Navbar>
        </div>
        <div id="main-container">
            <Card class="camera-width full-height">
                <CameraView></CameraView>
            </Card>
            <div class="information-components">
                <Card class="half-width half-height">
                    <IMU :data="rov.imu"></IMU>
                </Card>
                <Card class="half-width half-height">
                    <DataView title="Pressure:" :data="rov.pressure"></DataView>
                </Card>
                <Card class="half-width half-height">
                    <GpInfo :data="gamepad"></GpInfo>
                </Card>
                <Card class="half-width half-height">
                    <Thruster :data="rov.thrusters"></Thruster>
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
var GpInfo = require("./GpInfo.vue")
var Thruster = require("./Thrusters.vue")

export default {
    components: {
        Navbar,
        CameraView,
        IMU,
        Card,
        DataView,
        GpInfo,
        Thruster
    },
    data: function() {
        return {
            packet: {
                imu: {
                    x: 3,
                    y: 4,
                    z: 2,
                    pitch: 6,
                    roll: -4,
                    yaw: .243
                },
                pressure: {
                    pressure: 7,
                    temperature: 4
                },
                thrusters: [
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0},
                    { active: 0, target: 0.0, current: 0.0, pwm_actual: 0}
                ]
            },
            rov: {},
            gamepad: {
                buttons: {
                    a: 0,
                    b: 0,
                    x: 0,
                    y: 0
                },
                axes: {
                    left: {
                        x: 0,
                        y: 0
                    },
                    right: {
                        x: 0,
                        y: 0
                    }
                }
            },
        };
    },
    mounted: function() {
        var vm = this;

        vue_app = vm;

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
        }, 5);

        var socket = io.connect(`http://${document.domain}:${location.port}`, {transports: ['websocket']});
        //var socket = io.connect('http://10.10.1.125:5000', {transports: ['websocket']});


        setInterval(function() {
            socket.emit("control-data", {
                gamepad: controls,
                thrusters: [
                    true,true,true,true,
                    true,true,true,true
                ]
            });
        }, 50);


        setInterval(function() {
            socket.emit("ask-rov-data");
        }, 60);

        socket.on("rov-data", function(data) {
            vm.rov = data
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
.information-components {
    width: calc(100% - 800px); /* 100% - camera-width */
    height: 100%;
    float: left;
}
</style>
