import RPi.GPIO as GPIO
from time import sleep

def setup(outputs = {}, inputs = {}):
    GPIO.setmode(GPIO.BCM) # BCM or BOARD  
    for _, output in outputs.items():
        GPIO.setup(output.id, GPIO.OUT)
        output_off(output.id)

    for _, input in inputs.items():
        GPIO.setup(input.id, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def cleanup():
    GPIO.cleanup()

def output_on(id):
    GPIO.output(id, GPIO.HIGH)

def output_off(id):
    GPIO.output(id, GPIO.LOW)

def input(id):
    return GPIO.input(id)

def add_event_detect(*args, **kwargs):
    GPIO.add_event_detect(*args, **kwargs)

BOTH = GPIO.BOTH