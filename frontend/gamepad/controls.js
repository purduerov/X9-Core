var controls = {
    IMU: {
        x: 0,     //considered 'front or back'  (front & back, left joystick)
        y: 0,     //considered 'right or left'  (right & left, left joystick)
        z: 0,     //considered 'up or down'     (up or down, directional pad)
        pitch: 0, //nose up or down             (front & back, right joystick)
        roll: 0,  //roll to the left or right   (right & left, right joystick)
        yaw: 0    //left or right rotation      (left & right bumper)
    },
    // PRESSURE: {
        // pressure: 0,
        // temperature: 0
    // },
    Thrusters: {
        t0 : { power: "0"},
        t1 : { power: "0"},
        t2 : { power: "0"},
        t3 : { power: "0"},
        t4 : { power: "0"},
        t5 : { power: "0"},
        t6 : { power: "0"},
        t7 : { power: "0"}
    }
};