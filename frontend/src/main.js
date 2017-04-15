var gp = require("./gamepad")


function main(dearflask, dearclient) {
    //let socketHost = `http://${document.domain}:${location.port}`
    let socketHost = `http://raspberrypi.local:5000`
    let socket = io.connect(socketHost, {transports: ['websocket']});

    function update() {
        if (gp.ready) {
            dearflask.thrusters.desired_thrust = [
                gp.axes.left.y,
                gp.axes.left.x,
                0,
                0,
                0,
                0
            ]

            socket.emit("dearflask", dearflask);
        }

        setTimeout(update, 10)
    }

    socket.on("dearclient", (data) => {
        dearflask = data
    })


    update()
}

module.exports = main
