import time
import wiringpi

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)

wiringpi.pwmSetRange(200)

delay_period = 0.01

while True:
	for pulse in range(50, 250, 1):
		wiringpi.pwmWrite(18,pulse)
		time.sleep(delay_period)
	for pulse in range(250, 50, -1):
		wiringpi.pwmWrite(18, pulse)
		time.sleep(delay_period)

