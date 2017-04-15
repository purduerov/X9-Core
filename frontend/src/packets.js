module.exports = {
    dearflask: {
        thrusters: {
            desired_thrust: [
                0, // x:     forwards and backwards
                0, // y:     strafe left or right
                0, // z:     ascend / descend
                0, // pitch: nose up or down
                0, // roll:  roll to the left or right
                0 // yaw:   left or right rotation
            ],
            disabled_thrusters: []
        }
    },
    dearclient: {
        IMU: {
            x: 3,
            y: 4,
            z: 2,
            pitch: 6,
            roll: -4,
            yaw: 0.243
        },
        pressure: {
            pressure: 7,
            temperature: 4
        },
        thrusters: {
            t0: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 },
            t1: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 },
            t2: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 },
            t3: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 },
            t4: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 },
            t5: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 },
            t6: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 },
            t7: { active: 0, target: 0.0, current: 0.0, pwm_actual: 0 }
        }
    }
};
