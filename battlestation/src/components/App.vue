<template>
    <div id="app">
        <Navbar title="Purdue ROV | BattleStation"></Navbar>
        <div id="main-container">
            <div id="camera-view">
                <CameraView><CameraView>
            </div>
        </div>
    </div>
</template>

<script>
var Navbar = require("./Navbar.vue")
var CameraView = require("./CameraView.vue")

export default {
  components: {
    Navbar,
    CameraView
  }
}
</script>

<style scoped>
#app {
    font-family: 'Roboto', Helvetica, Arial, sans-serif;
    width: 100%;
    height: 100%;
}

navbar {
    height: 100px;
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
    width: 1200px;
}
</style>
