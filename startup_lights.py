from gpio.interface import cleanup
from gpio.config import outputs
import gpio.interface as gpio
import light_util

def main():
    gpio.setup(outputs)
    light_util.loading_sequence_start(load_count=1, synchronous=True)
    light_util.shutdown_sequence(delay=0.2)
    cleanup()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        cleanup()
        
