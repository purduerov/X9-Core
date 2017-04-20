module.exports = {
    dearflask: {
        thrusters: {
            desired_thrust: [
                0, // x:     forwards and backwards
                0, // y:     strafe left or right
                0, // z:     ascend / descend
                0, // roll:  roll to the left or right
                0, // pitch: nose up or down
                0 // yaw:   left or right rotation
            ],
            disabled_thrusters: [],
            thruster_scales: [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        },
        valve_turner: {
            power: 0.0
        },
        claw: {
            power: 0.0
        },
        fountain_tool: {
            power: 0.0
        },
        cameras: {
            { port: 8080, status: 1 }
        }
    },
    dearclient: {
        IMU: {
            x: 3, y: 4, z: 2,
            pitch: 6, roll: -4, yaw: 0.243
        },
        pressure: {
            pressure: 7,
            temperature: 4
        },
        thrusters: [0, 0, 0, 0, 0, 0, 0, 0],
        cameras: {}
    }
};
