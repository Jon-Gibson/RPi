from gpio.output import Output
from time import sleep
from math import exp

class Light(Output):
    def __init__(self, id):
        super().__init__(id)
        self.id = id

    # Turns the LED on for the given duration, uses rapid flashing to give illustion of different brightnesses
    def blink(self, duration = 1, brightness = 1, max_toggle = 1e-5):
        flash_rate = 0.01
        times_to_flash = int(duration / flash_rate)
        time_on_per_cycle = flash_rate * brightness
        time_off_per_cycle = flash_rate * (1 - brightness)
        for _ in range(0, times_to_flash):
            if (time_on_per_cycle > max_toggle):
                self.turn_on()
                sleep(time_on_per_cycle)
            if (time_off_per_cycle > max_toggle):
                self.turn_off()
                sleep(time_off_per_cycle)

    # Lighthouse-like effect, fade light in and out
    def flare(self, duration = 2, max_brightness = 1, min_brightness = 0.2):
        step_duration = 0.05
        step_count = int(duration / step_duration)
        stage_steps = int(step_count/2)
        # Increasing brightness
        for i in range(0, stage_steps):
            bright_factor = i / stage_steps * (max_brightness - min_brightness) + min_brightness
            self.blink(step_duration, brightness_func(bright_factor))
        # Descrease brightness
        for i in range(stage_steps, step_count):
            bright_factor = (step_count - i) / stage_steps * (max_brightness - min_brightness) + min_brightness
            self.blink(step_duration, brightness_func(bright_factor))

# Maps linear [0, 1] to a nice sigmoid brightness curve
def brightness_func(x):
    a = 8 # Slides signoid left/right
    b = 14 # Controls the steepness of the curve
    signoid = 1 / (1 + exp(a-b*x))
    return signoid