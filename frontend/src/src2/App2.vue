<template>
    <div id="app2">
        <div id="navbar">
            <Navbar title="Purdue ROV - BattleStation"></Navbar>
        </div>
        <div id="main-container">
            <div class="full-width full-height">
                <Card class="full-height full-width">
                    <CameraView :data="packets.dearclient.cameras" :packet="packets.dearflask"></CameraView>
                </Card>
            </div>
        </div>
    </div>
</template>

<script>
var Navbar = require("../components/Navbar.vue")
var CameraView = require("../components/CameraView2.vue")
var Card = require("../components/Card.vue")

var packets = require("../packets.js")

export default {
    components: {
        Navbar,
        CameraView,
        Card,
    },
    data: function() {
        return {
            packets: packets,
        }
    },
    mounted: function() {
        window.vue2 = this;
    }
}
</script>

<style scoped>
#app2 {
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

.full-height {
    height: 100% !important;
    float: left;
}

.full-width {
    width: 100% !important;
    float: left;
}
</style>
