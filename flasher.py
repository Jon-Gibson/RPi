from gpio.interface import cleanup
from gpio.config import outputs
import gpio.interface as gpio
import light_util
import multiprocessing

def main():
    setup()

    light_util.loading_sequence_start()

    input("")

    light_util.loading_sequence_stop()
    # processes = multiprocessing.active_children()
    # for p in processes:
    #     p.terminate()
    light_util.shutdown_sequence(delay=0.2)
    cleanup()

def setup():
    gpio.setup(outputs)   

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
        
