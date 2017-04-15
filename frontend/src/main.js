var gp = require("./gamepad")


function main(packets) {
    //let socketHost = `http://${document.domain}:${location.port}`
    let socketHost = `ws://raspberrypi.local:5000`
    let socket = io.connect(socketHost, {transports: ['websocket']});

    gp.set()

    function update() {
        if (gp.ready) {
            gp.get_current();

            packets.dearflask.thrusters.desired_thrust = [
                //VelX - forwards and backwards
                gp.axes.left.y,

                //VelY - strafe left and right
                (gp.buttons.rb.val - gp.buttons.lb.val) * 0.4,

                //VelZ - ascend and descend
                gp.buttons.rt.val - gp.buttons.lt.val,

                //Roll
                gp.axes.right.x,

                //Pitch
                gp.axes.right.y,

                //Yaw
                gp.axes.left.x
            ]

            packets.dearflask.valve_turner.power = (gp.buttons.b.val - gp.buttons.y.val) * 0.1
            packets.dearflask.fountain_tool.power = (gp.buttons.left.val - gp.buttons.right.val) * 0.1
            packets.dearflask.claw.power = (gp.buttons.a.val - gp.buttons.x.val) * 0.1

            socket.emit("dearflask", packets.dearflask);
        }

        setTimeout(update, 10)
    }
    update()

    function updateDC(data) {
        packets.dearclient = data
    }

    socket.on("dearclient", updateDC)

    // request new data
    setInterval(() => {
        socket.emit("dearclient")
    }, 50)
}

module.exports = main
