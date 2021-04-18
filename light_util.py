from gpio.interface import cleanup
from gpio.config import outputs
from gpio.output import turn_off_all
from gpio.output import turn_on_all
from gpio.light import Light
from time import sleep
import multiprocessing

loaders = []

def loading_sequence_start(load_count=float('inf'), synchronous=False):
    for name, output in outputs.items():
        if isinstance(output, Light):
            thread = multiprocessing.Process(name=f"{name} Light", target=load_light, args=[output, load_count, 1])
            thread.start()
            loaders.append(thread)
            sleep(1/4)
    if synchronous:
        for loader in loaders:
            loader.join()

def loading_sequence_stop():
    for loader in loaders:
        loader.terminate()

def shutdown_sequence(delay = 0):
    turn_on_all(outputs, sleep_time = delay)
    sleep(delay)
    turn_off_all(outputs, sleep_time = delay)
    sleep(delay)
    turn_on_all(outputs)
    sleep(delay/2)
    turn_off_all(outputs)

def load_light(light, count = 1, duration = 2):
    try:
        i = 0
        while i < count:
            light.flare(duration=duration)
            sleep(duration)
            i += 1
    except KeyboardInterrupt: 
        cleanup()
        
