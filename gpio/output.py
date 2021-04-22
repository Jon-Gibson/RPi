import gpio.interface as gpio
from time import sleep

class Output:
    def __init__(self, id):
        self.id = id

    def turn_on(self):
        gpio.output_on(self.id)
    
    def turn_off(self):
        gpio.output_off(self.id)

    def is_on(self):
        return gpio.input(self.id) == 1

    def toggle(self):
        if self.is_on():
            self.turn_off()
        else:
            self.turn_on()

def turn_off_all(outputs, sleep_time = 0):
    for _, output in outputs.items():
        output.turn_off()
        sleep(sleep_time)

def turn_on_all(outputs, sleep_time = 0):
    for _, output in outputs.items():
        output.turn_on()
        sleep(sleep_time)