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
    buttons: [
      {where: "buttons", name: "a", index: 0, match: 1},
      {where: "buttons", name: "b", index: 1, match: 1},
      {where: "buttons", name: "x", index: 2, match: 1},
      {where: "buttons", name: "y", index: 3, match: 1},
      {where: "buttons", name: "lb", index: 4, match: 1},
      {where: "buttons", name: "rb", index: 5, match: 1},
      {where: "buttons", name: "lt", index: 6, match: 1},
      {where: "buttons", name: "rt", index: 7, match: 1},
      {where: "buttons", name: "slct", index: 8, match: 1},
      {where: "buttons", name: "strt", index: 9, match: 1},
      {where: "buttons", name: "lpress", index: 10, match: 1},
      {where: "buttons", name: "rpress", index: 11, match: 1},
      {where: "buttons", name: "up", index: 12, match: 1},
      {where: "buttons", name: "down", index: 13, match: 1},
      {where: "buttons", name: "left", index: 14, match: 1},
      {where: "buttons", name: "right", index: 15, match: 1},
    ],
    axes: [
      {where: "axes", which: "left", name: "x", index: 0},
      {where: "axes", which: "left", name: "y", index: 1},
      {where: "axes", which: "right", name: "x", index: 2},
      {where: "axes", which: "right", name: "y", index: 3},
    ]
  },
  linbox: {
      id: "Microsoft Controller (Vendor: 045e Product: 02d1)",
    buttons: [
      {where: "buttons", name: "a", index: 0, match: 1},
      {where: "buttons", name: "b", index: 1, match: 1},
      {where: "buttons", name: "x", index: 2, match: 1},
      {where: "buttons", name: "y", index: 3, match: 1},
      {where: "buttons", name: "lb", index: 4, match: 1},
      {where: "buttons", name: "rb", index: 5, match: 1},
      {where: "buttons", name: "home", index: 8, match: 1},
      {where: "axes", name: "lt", index: 2, match: 1},
      {where: "axes", name: "rt", index: 5, match: 1},
      {where: "buttons", name: "slct", index: 6, match: 1},
      {where: "buttons", name: "strt", index: 7, match: 1},
      {where: "buttons", name: "lpress", index: 9, match: 1},
      {where: "buttons", name: "rpress", index: 10, match: 1},
      {where: "axes", name: "up", index: 7, match: -1},
      {where: "axes", name: "down", index: 7, match: 1},
      {where: "axes", name: "left", index: 6, match: -1},
      {where: "axes", name: "right", index: 6, match: 1},
    ],
    axes: [
      {where: "axes", which: "left", name: "x", index: 0},
      {where: "axes", which: "left", name: "y", index: 1},
      {where: "axes", which: "right", name: "x", index: 3},
      {where: "axes", which: "right", name: "y", index: 4},
    ]
  },
  rockgp: {
      id: "Performance Designed Products Rock Candy Gamepad for Xbox 360 (Vendor: 0e6f Product: 011f)",
    buttons: [
      {where: "buttons", name: "a", index: 0, match: 1},
      {where: "buttons", name: "b", index: 1, match: 1},
      {where: "buttons", name: "x", index: 2, match: 1},
      {where: "buttons", name: "y", index: 3, match: 1},
      {where: "buttons", name: "lb", index: 4, match: 1},
      {where: "buttons", name: "rb", index: 5, match: 1},
      {where: "buttons", name: "home", index: 8, match: 1},
      {where: "axes", name: "lt", index: 2, match: 1},
      {where: "axes", name: "rt", index: 5, match: 1},
      {where: "buttons", name: "slct", index: 6, match: 1},
      {where: "buttons", name: "strt", index: 7, match: 1},
      {where: "buttons", name: "lpress", index: 9, match: 1},
      {where: "buttons", name: "rpress", index: 10, match: 1},
      {where: "axes", name: "up", index: 7, match: -1},
      {where: "axes", name: "down", index: 7, match: 1},
      {where: "axes", name: "left", index: 6, match: -1},
      {where: "axes", name: "right", index: 6, match: 1},
    ],
    axes: [
      {where: "axes", which: "left", name: "x", index: 0},
      {where: "axes", which: "left", name: "y", index: 1},
      {where: "axes", which: "right", name: "x", index: 3},
      {where: "axes", which: "right", name: "y", index: 4},
    ]
  },
      
  length: 3
}
