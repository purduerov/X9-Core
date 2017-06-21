# Test Scripts for the ROV!

## Digital Pin Test
```bash
usage: digital_pin.py [-h] pin value

Digital Pin Test

positional arguments:
  pin         Raspberry Pi Pin (BCM Pin)
  value       On or Off

optional arguments:
  -h, --help  show this help message and exit
```
Note: You need sudo to change gpio pins

## Motor Movement Test
```bash
usage: motor_move.py [-h] pin power time

Motor Movement Test

positional arguments:
  pin         PWM Chip Pin [0, 15]
  power       Power level [-1.0, 1.0]
  time        How long to turn on motor (seconds)

optional arguments:
  -h, --help  show this help message and exit
```
Note: Ctrl-C will stop the movement

## Thruster Test
Automated thruster test. Turns on thrusters for 1 second forward, 1 second back.
Helps to make sure all thrusters have their correct pin and are working properly.

## Camera Test
Starts up all cameras with mjpg streamer, and check which streams are working.
