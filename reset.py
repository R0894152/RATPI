import RPi.GPIO as GPIO
import time
import sys

# GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Zet LED staat
led_state = True
GPIO.output(16, led_state)

# Wait for the button to be pressed
try:
    while led_state:
        if GPIO.input(13) == GPIO.LOW:
            # Als de knop is gedrukt, zet de LED uit en sluit het programma.
            led_state = False
            GPIO.output(16, led_state)
            sys.exit()

        time.sleep(0.1)

finally:
    # Clean up the GPIO pins
    GPIO.cleanup()
