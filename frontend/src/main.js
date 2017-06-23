var gp = require("./gamepad")
var kb = require("./keyboard")

function main(packets, config) {

    //let socketHost = `http://${document.domain}:${location.port}`
    let socketHost = `ws://raspberrypi.local:5000`
    let socket = io.connect(socketHost, {transports: ['websocket']})
    let {shell, app, ipcRenderer} = window.require('electron');
    let cam2port = 8080;

    gp.set()

    function update() {

        if (gp.ready) {
            gp.get_current()

            let ts = config.thrust_scales
            let ti = config.thrust_invert

            packets.dearflask.thrusters.desired_thrust = [
                //VelX - forwards and backwards
                //gp.axes.left.y * (ts.master/100.0) * (ts.velX/100.0) * -1,
                gp.axes.right.x * (ts.master/100.0)  * (ts.yaw/100.0) * -1 * (ti.yaw ? -1 : 1),

                //VelY - strafe left and right
                gp.axes.left.x * (ts.master/100.0)  * (ts.velY/100.0) * -1 * (ti.velY ? -1 : 1),

                //VelZ - ascend and descend
                (gp.buttons.lb.val - gp.buttons.rb.val) * (ts.master/100.0)  * (ts.velZ/100.0) * -1 * (ti.velZ ? -1 : 1),

                //Roll
                (gp.buttons.slct.val - gp.buttons.strt.val) * (ts.master/100.0)  * (ts.roll/100.0) * (ti.roll ? -1 : 1),

                //Pitch
                gp.axes.right.y * (ts.master/100.0)  * (ts.pitch/100.0) * -1 * (ti.pitch ? -1 : 1),

                //Yaw
                //gp.axes.right.x * (ts.master/100.0)  * (ts.yaw/100.0)
                gp.axes.left.y * (ts.master/100.0) * (ts.velX/100.0) * (ti.velX ? -1 : 1)
            ]

            //Compute individual thruster scalings
            packets.dearflask.thrusters.thruster_scales = config.thruster_control.map(
                t => t.power/100.0 * (t.invert ? -1 : 1)
            )

            let tl = config.tool_scales

            packets.dearflask.valve_turner.power = (kb.isPressed('right') - kb.isPressed('left')) * (tl.valve_turner.power/100) * (tl.valve_turner.invert ? -1 : 1)
            packets.dearflask.fountain_tool.power = (gp.buttons.left.val - gp.buttons.right.val) * (tl.fountain_tool.power/100) * (tl.fountain_tool.invert ? -1 : 1)

            let claw = (gp.buttons.a.val - gp.buttons.b.val) * (tl.claw.master/100) * (tl.claw.invert ? -1 : 1)
            packets.dearflask.claw.power = claw * ((claw > 0 ? tl.claw.open : tl.claw.close)/100)

            packets.dearflask.cameras[cam2port] = "active";

            socket.emit("dearflask", packets.dearflask)
        }

        setTimeout(update, 10)
    }
    update()

    ipcRenderer.on('cam2port-include', function(port) {
        cam2port = port;
        console.log(port+" vs "+cam2port);
    });

    function updateDC(data) {
        packets.dearclient = data
    }

    socket.on("dearclient", updateDC)

    // request new data
    setInterval(() => {
        socket.emit("dearclient")
    }, 50)

    setInterval(() => {
        localStorage.setItem('configuration', JSON.stringify(config))
    }, 10*1000)
}

module.exports = main
