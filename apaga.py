import Rpio.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.out)

GPIO.output(18, 0)