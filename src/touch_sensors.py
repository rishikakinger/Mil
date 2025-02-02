import RPi.GPIO as GPIO
import time

# GPIO pins for touch sensors and buzzer
GOOD_TOUCH_PIN = 17
BAD_TOUCH_PIN = 27
BUZZER_PIN = 22

def setup_touch_sensors():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GOOD_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BAD_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)

def check_touch():
    if GPIO.input(GOOD_TOUCH_PIN) == GPIO.LOW:
        return "good"
    elif GPIO.input(BAD_TOUCH_PIN) == GPIO.LOW:
        return "bad"
    return None

def buzz(frequency, duration):
    p = GPIO.PWM(BUZZER_PIN, frequency)
    p.start(50)
    time.sleep(duration)
    p.stop()

def cleanup():
    GPIO.cleanup()