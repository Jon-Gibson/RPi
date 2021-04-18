from time import sleep
import gpio.interface as gpio
import gpio.config as config
from gpio.output import turn_off_all

current_color = config.outputs["GREEN"]

def main():
    setup()
    try:
        turn_off_all(config.outputs)
        current_color.turn_on()
        config.inputs["BUTTON"].listenBoth(callback=callback)
        input("\n")
        gpio.cleanup()
    except KeyboardInterrupt:          
        gpio.cleanup()  

def setup():
    gpio.setup(outputs=config.outputs, inputs=config.inputs)

def callback(channel):
    if gpio.input(channel):
        config.outputs["BLUE"].turn_on()
    else:
        config.outputs["BLUE"].turn_off()
        light_next_color(channel)

def light_next_color(channel):
    global current_color
    current_color.turn_off() 
    if current_color == config.outputs["RED"]:
         current_color = config.outputs["YELLOW"]
    elif current_color == config.outputs["YELLOW"]:
        current_color = config.outputs["GREEN"]
    else:
        current_color = config.outputs["RED"]
    current_color.turn_on()   

if __name__ == "__main__":
    main()
