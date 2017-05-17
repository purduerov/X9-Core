/*
**************************************************************************************************
  This file creates a gp object -- the 'gamepad' -- and provides
  the library necessrily to fill it.

  Please include gp_layouts.js before gp_library.js in the html script tags.

--------------------------------------------------------------------------------------------------
  To set the gamepad/gp, use:
    gp.set();
    --note, you can pass an html 'message' element into this function to write
      its instructional messages to.

--------------------------------------------------------------------------------------------------
  To map the identified gp, use:
    gp.map();

    --The gp.map() function is called by gp.set(), although
      you are able to call it if you want to re-map gp.

--------------------------------------------------------------------------------------------------
  To get the status of the gp, once identified and mapped, use:
    gp.get_current();

    --for best performance, I recommend this should be used inside of the master loop so
      there are no issues with asynchronous behavior.

--------------------------------------------------------------------------------------------------
  To use the statuses of a button or a joystick, after using gp.get_current();,
  type references to the gamepad like so:
    A: gp.buttons.a.val            <- a 1/0 value for whether it's pressed or not
       gp.buttons.a.pressed        <- a 1/0 value for if the button was just pressed or not
       gp.buttons.a.released       <- a 1/0 value for if the button was just released or not

    left stick: gp.axes.left.x     <- the position of the left joystick, x axis
                gp.axes.left.y     <- the position of the left joystick, y axis
                gp.axes.left.r     <- the radius, or hypotenus of the triangle x and y make.
                gp.axes.left.theta <- the angle of the hypotenus from the y-axis (NOT x-axis)
                    --this functions the same as if you'd flipped the unit circle around the line y=x on the xy-plane

    --to see what button lables are available, you can either look at gp_layouts.js, or 'inspect' your
      webpage and just type 'gp' in the command prompt there--it should show you the gp object, which you
      can click through to see its structure.
**************************************************************************************************
*/

let layouts = require('./layouts.json');
let bind = require('./bind_functions.js');

class Gamepad {

    static getGamepads() {
        return navigator.getGamepads()
    }

    getGamepad() {
        return this.gp_index >= 0 ? Gamepad.getGamepads()[this.gp_index] : undefined;
    }

    static checkCompatibility(id) {
        return Gamepad.findLayout(id) !== undefined;
    }

    static findLayout(match_id) {
        return layouts.find(n => n['id'].includes(match_id))
    }

    // Select and set a gamepad if it matches a layout we know about, and a
    // buttons is pressed
    static findGamepad(callback) {
        console.log('Scanning for gamepads with a button pressed...')

        // Poll for new gamepads
        let monitor = window.setInterval(() => {
            let gamepads = Gamepad.getGamepads()

            // Check each gamepad for a gamepad with a pressed button. When one
            // is found, map the gamepad and clear this monitor interval
            for (let i = 0; i < gamepads.length; i++) {
                let g = gamepads[i]
                // 1) make sure g and its buttons are not undefined
                if (!g || !g.buttons) continue

                // 2) see if any buttons are pressed
                if (!g.buttons.find(b => b.pressed)) continue

                // 3) attempt to match the ID to our list of layouts
                if (!Gamepad.checkCompatibility(g.id)) continue

                // This gamepad is good if it passes through above checks

                // Cancel the interval
                window.clearInterval(monitor)

                let gp
                try {
                    gp = new Gamepad(i)
                } catch (e) {
                    console.error(e)
                    continue
                }

                // call callback if provided
                if (callback) callback(gp)

                break
            }
        }, 100);
    }


    constructor(gp_index) {
        this.id = "";

        // saved gamepad.index. It should be unique between disconnects
        this.index = -1
        // index of the gamepad accessible through navigator.getGamepads()
        this.gp_index = gp_index

        this.layout = {}
        this.gamepad = undefined

        this.buttons = {}
        this.buttons_last = {}

        this.axes = {}
        this.axes_offset = {}

        this.deadZone = 0.2

        /* Set up Nav Gamepad */

        // Assure that the gamepad is valid
        this.gamepad = Gamepad.getGamepads()[gp_index]
        if (this.gamepad === undefined) {
            throw new Error(`Index: ${gp_index} is an undefined gamepad`)
        }

        this.id = this.gamepad.id
        this.index = this.gamepad.index

        /* Set up Layout */

        this.layout = Gamepad.findLayout(this.gamepad.id)

        if (this.layout === undefined) {
            throw new Error(`No layout was able to be matched for "${this.gamepad.id}".`)
        }

        /* Initialize Buttons */

        for (const btn in this.layout.buttons) {
            this.buttons[btn] = false
            this.buttons_last[btn] = false
        }

        /* Initialize Axes */

        for (const axis in this.layout.axes) {
            this.axes_offset[axis] = this.axisFromGamepad(axis)
            this.axes[axis] = this.axis(axis)
        }

        // Do an update to refresh everything and update buttons
        this.update()

        // We have matched an ID
        console.log(`Gamepad "${this.gamepad.id}" was matched to "${this.layout.description}".`)
    }

    buttonState(btn) {
        if (this.buttons[btn] === undefined) {
            return false
        }
        return this.buttons[btn]
    }

    buttonPressed(btn) {
        if (this.buttons[btn] === undefined) {
            return false
        }
        return this.buttons[btn] && !this.buttons_last[btn]
    }

    buttonReleased(btn) {
        if (this.buttons[btn] === undefined) {
            return false
        }
        return !this.buttons[btn] && this.buttons_last[btn]
    }

    buttonFromGamepad(btn) {
        if (this.layout['buttons'][btn] === undefined) {
            return false
        }

        const {index, match, where} = this.layout.buttons[btn]

        if (index >= this.gamepad[where].length || index < 0) {
            return false
        }

        return this.gamepad[where][index].value === match
    }

    axis(axis) {
        if (this.layout['axes'][axis] === undefined) {
            return 0.0
        }

        let value = this.axisFromGamepad(axis) - this.axes_offset[axis]

        value = Math.min(1.0, value)
        value = Math.max(-1.0, value)

        if (value > 0 && value <  this.deadZone) value = 0.0
        if (value < 0 && value > -this.deadZone) value = 0.0

        return value
    }

    axisFromGamepad(axis) {
        if (this.layout['axes'][axis] === undefined) {
            return 0.0
        }

        const {index, where} = this.layout['axes'][axis]

        return this.gamepad[where][index]
    }

    resetAxisOffset(axis) {
        for (const axis in this.axes_offset) {
            this.axes_offset[axis] = this.axisFromGamepad(axis)
        }
    }

    update() {
        this.gamepad = this.getGamepad()

        if (this.gamepad === undefined || !this.gamepad.connected) {
            console.warn("Lost connection to controller")
            this.connected = false
            return false
        }

        for (const btn in this.layout.buttons) {
            this.buttons_last[btn] = this.buttons[btn]
            this.buttons[btn] = this.buttonFromGamepad(btn)
        }

        for (const axis in this.layout.axes) {
            this.axes[axis] = this.axis(axis)
        }

        return true
    }
}

module.exports = Gamepad
