import gpio.interface as gpio

class Input:
    def __init__(self, id):
        self.id = id

    def value(self):
        gpio.input(self.id)

    def listenBoth(self, callback):
        gpio.add_event_detect(self.id, gpio.BOTH, callback=callback)
