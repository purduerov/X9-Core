var controls = {
    force: {
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
    tools: {
      claw: 0,
      valve: 0
    },
    thrusters: {
        t0 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0},
        t1 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0},
        t2 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0},
        t3 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0},
        t4 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0},
        t5 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0},
        t6 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0},
        t7 : { active: 1, target: 0.0, current: 0.0, pwm_actual: 0}
    },
    buttons: gp.buttons,
    axes: gp.axes
};
