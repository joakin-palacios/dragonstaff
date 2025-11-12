#Led Spoke Handler
from machine import Pin
import neopixel


class ledSpoke:
    def __init__(self, mcuPin, nr_of_leds=20):
        self.mcuPin = mcuPin
        self.n = nr_of_leds
        self.np = neopixel.NeoPixel(Pin(self.mcuPin), self.n)
        self.program = 'initialized'
        self.color = (40,128,20)
        self.co_color = (0,0,0)
        self.status = "start_up"
        self.wait = 60
        self.last_side = "both_sides"
        self.magic_number = 1
        self.brightness = 1
    
    def illuminate(self):
        self.np.write()
        
    def setcolor(self, ith_led, color, duplicate = False):
        if duplicate:
            self.np[int(self.n/2)+ith_led]=color
            pass
        self.np[ith_led]=color

class otherSideSpoke:
    def __init__(self, nr_of_leds=20):
        self.n = nr_of_leds
        self.program = 'initialized'
        self.color = (40,128,20)
        self.co_color = (0,0,0)
        self.status = "start_up"
        self.wait = 60
        self.last_side = "both_sides"
        self.magic_number = 1
        self.brightness = 1