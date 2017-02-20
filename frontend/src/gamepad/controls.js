var controls = {
    force: {
        x: 0,     //considered 'front or back'  (front & back, left joystick)
        y: 0,     //considered 'right or left'  (right & left, left joystick)
        z: 0,     //considered 'up or down'     (up or down, directional pad)
        pitch: 0, //nose up or down             (front & back, right joystick)
        roll: 0,  //roll to the left or right   (right & left, right joystick)
        yaw: 0    //left or right rotation      (left & right bumper)
    },
    buttons: gp.buttons,
    axes: gp.axes
};
