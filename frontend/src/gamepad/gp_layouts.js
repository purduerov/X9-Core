/*
  Please include this file before gp_library.js. The layouts
  need to be defined before the controller library object can
  function.

  Any additions must follow the format of the xbox object
  (it was the first in this file)

  Please ask the Basestation team if you would like to add
  any controllers to the list, or if you're having issues
  using one that should be implimented.
*/

var layouts = {
  xbox: {
    id: "Xbox 360 Controller (XInput STANDARD GAMEPAD)",
    buttons: {
      a:      0,
      b:      1,
      x:      2,
      y:      3,
      lb:     4,
      rb:     5,
      lt:     6,
      rt:     7,
      slct:   8,
      strt:   9,
      lpress: 10,
      rpress: 11,
      up:     12,
      down:   13,
      left:   14,
      right:  15,
      length: 16
    },
    axes: {
      left: {
        x:    0,
        y:    1
      },
      right: {
        x:    2,
        y:    3
      },
      length: 4
    }
  },
  length: 1
}
