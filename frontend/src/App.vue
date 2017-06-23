<template>
    <div id="app">
        <div id="navbar">
            <Navbar title="Purdue ROV - BattleStation"></Navbar>
        </div>
        <div id="main-container">
            <div class="camera-width full-height">
                <Card class="full-height">
                    <CameraView :data="packets.dearclient.cameras" :packet="packets.dearflask"></CameraView>
                </Card>
            </div>
            <div class="data-width full-height">
                <div class="data-column">
                    <Card title="Thruster Info">
                        <Thruster :data="packets.dearclient.thrusters"></Thruster>
                    </Card>
                    <Card title="Tool Info">
                        <ToolInfo :data="packets.dearflask"></ToolInfo>
                    </Card>
                    <Card title="Camera Info">
                        <CameraInfo :data="packets.dearclient.cameras"></CameraInfo>
                    </Card>
                    <Card title="Presets">
                        <ThrusterPresets :config="config"></ThrusterPresets>
                    </Card>
                </div>
                <div class="data-column">
                    <CardTabs title="Thruster Control" fixedHeight="450px">
                        <Tab title="General">
                            <ThrusterControl :scales="config.thrust_scales" :invert="config.thrust_invert"></ThrusterControl>
                        </Tab>
                        <Tab title="Individual">
                            <IndThrusterControl :data="config.thruster_control"></IndThrusterControl>
                        </Tab>
                    </CardTabs>
                    <Card title="Tool Control">
                        <ToolControl :data="config.tool_scales" :packleds="packets.dearflask.leds"></ToolControl>
                    </Card>
                </div>
                <div class="data-column">
                    <Card title="Timer">
                        <Timer></Timer>
                    </Card>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
var Navbar = require("./components/Navbar.vue")
var CameraView = require("./components/CameraView.vue")
var CameraInfo = require("./components/CameraInfo.vue")
var Card = require("./components/Card.vue")
var CardTabs = require("./components/CardTabs.vue")
var Tab = require("./components/Tab.vue")
var Thruster = require("./components/Thrusters.vue")
var ThrusterControl = require("./components/ThrusterControl.vue")
var ThrusterPresets = require("./components/ThrusterPresets.vue")
var IndThrusterControl = require("./components/IndThrusterControl.vue")
var ToolControl = require("./components/ToolControl.vue")
var ToolInfo = require("./components/ToolInfo.vue")
var Timer = require("./components/Timer.vue")

var packets = require("./packets.js")
var main = require("./main.js")

export default {
    components: {
        Navbar,
        CameraView,
        CameraInfo,
        Card,
        CardTabs,
        Tab,
        Thruster,
        ThrusterControl,
        ThrusterPresets,
        IndThrusterControl,
        ToolControl,
        ToolInfo,
        Timer
    },
    data: function() {
        let config = {
            version: 1.0, //INCREMENT IF YOU CHANGE THIS DATA STRUCTURE!
            thrust_scales: {
                master: 50, velX: 60, velY: 50,
                velZ: 60, pitch: 35,
                roll: 35, yaw: 25,
            },
            thrust_invert: {
                master: false, velX: false, velY: false,
                velZ: false, pitch: false,
                roll: false, yaw: false,
            },
            thruster_control: [
                {power: 100, invert: false}, {power: 100, invert: false},
                {power: 100, invert: false}, {power: 100, invert: false},
                {power: 100, invert: false}, {power: 100, invert: false},
                {power: 100, invert: false}, {power: 100, invert: false}
            ],
            tool_scales: {
                claw: {
                    master: 50,
                    open: 50,
                    close: 50,
                    invert: false
                },
                valve_turner: {
                    power: 30,
                    invert: false
                },
                fountain_tool: {
                    power: 30,
                    invert: false
                }
            }
        }
        let savedConfig = {}
        try {
            savedConfig = JSON.parse(localStorage.getItem('configuration') || {})
            if (savedConfig && savedConfig.version && savedConfig.version == config.version) {
                config = savedConfig
            }
        } catch (e) {}

        return {
            packets: packets,
            config: config
        }
    },
    mounted: function() {
        window.vue = this
        main(this.packets, this.config);
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

.data-column {
    width: 33.333333%;
    height: 100%;
    float: left;
}

.half-height {
    height: 50% !important;
    float: left;
}

.full-height {
    height: 100% !important;
    float: left;
}

.camera-width {
    width: 1200px;
}
.data-width {
    width: calc(100% - 1200px)
}
</style>
