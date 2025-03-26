#Led Spoke Handler
from machine import Pin
import neopixel
import uasyncio

class ledSpoke:
    def __init__(self, mcuPin, nr_of_leds, duplicate=False):
        self.program = 'init'
        self.mcuPin = mcuPin
        self.n = nr_of_leds
        self.duplicate = duplicate
        self.np = neopixel.NeoPixel(Pin(self.mcuPin), self.n)
        
        
a = ledSpoke(1,2)
print (a.program)