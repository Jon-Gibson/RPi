"""
Logs to file and lights up LEDs on my raspberry pi so
I can tell if it's still running ok.
"""
import logging

ALIVE = 18
INFO = 25
WARNING = 23
ERROR = 24

def default_config():
    config_pi()
    config_logger()

def config_pi(gpio_alive = 18, gpio_info = 25, gpio_warn = 23, gpio_error = 24, gpio_mode = GPIO.BCM):
    global ALIVE, INFO, WARNING, ERROR
    ALIVE = gpio_alive
    INFO = gpio_info
    WARNING = gpio_warn
    ERROR = gpio_error

    GPIO.setmode(gpio_mode)             # BCM or BOARD

    GPIO.setup(gpio_alive, GPIO.OUT)
    GPIO.setup(gpio_info, GPIO.OUT)
    GPIO.setup(gpio_warn, GPIO.OUT)
    GPIO.setup(gpio_error, GPIO.OUT)

    turn_off(gpio_alive)
    turn_off(gpio_info)
    turn_off(gpio_warn)
    turn_off(gpio_error)

def turn_on(gpio):
    GPIO.output(gpio, GPIO.HIGH)

def turn_off(gpio):
    GPIO.output(gpio, GPIO.LOW)

def config_logger(file_name = "pi_logger.log", log_level = logging.WARNING):
    logging.basicConfig(filename=file_name, encoding='utf-8', level=log_level)

def start():
    turn_on(ALIVE)

def info(msg):
    logging.info(msg)

def warning(msg):
    logging.warning(msg)

def error(msg):
    logging.error(msg)

def end():
    turn_off(ALIVE)