#Led Spoke Handler
from machine import Pin
import neopixel


class ledSpoke:
    def __init__(self, mcuPin, nr_of_leds=20, duplicate=False):
        self.mcuPin = mcuPin
        self.n = nr_of_leds
        self.duplicate = duplicate
        self.np = neopixel.NeoPixel(Pin(self.mcuPin), self.n)
        self.program = 'initialized'
        
    def illuminate(self):
        self.np.write()
        
    def setcolor(self, ith_led, color):
        if self.duplicate:
            self.np[int(self.n/2)+ith_led]=color
            pass
        self.np[ith_led]=color