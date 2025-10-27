import setupnfunctions as snf
from machine import Pin
import neopixel
import uasyncio
import random as Rondo
import ledspokehandler
import math


# General Setup
status="Water"
color=(40,128,20)
co_color=(0,0,0)
wait=60
np = ledspokehandler.ledSpoke(mcuPin=19, nr_of_leds=20)
np2 = ledspokehandler.ledSpoke(mcuPin=20, nr_of_leds=20) 
np3 = ledspokehandler.ledSpoke(mcuPin=21, nr_of_leds=20)

async def water_waves(np, waves=2, speed_factor=1, divider=2):
    global wait, status, color, co_color
    n = np.n
    if (n % 2 == 0):
        d = int(n/divider) # d = 20/2 = 10
    else:
        d = int((n-1)/divider)
    speed=math.pi*speed_factor*0.1
    rounds = int(2*math.pi/speed)
    print (rounds,2*math.pi/speed)


    # define base and highlight blues
    color = (0, 0, 80)
    co_color = (0, 150, 255)

    # smooth color blending between two colors
    def blend(c1, c2, t):
        return (
            int(c1[0] + (c2[0] - c1[0]) * t),
            int(c1[1] + (c2[1] - c1[1]) * t),
            int(c1[2] + (c2[2] - c1[2]) * t) )

    phase = 0
    for j in range (rounds):
        if status!='Water': # break if the mode has changed
            break
        for i in range(d):
            # sine wave pattern across LEDs
            wave = math.sin((i / d) * waves * 2 * math.pi - phase)
            # normalize -1..1 to 0..1
            t = (wave + 1) / 2

            # blend between deep blue and light blue
            np.np[i] = blend(color, co_color, t)
            np.np[n-1-i] = blend(color, co_color, t)

        np.illuminate()
        await uasyncio.sleep(0)
        await uasyncio.sleep_ms(wait)

        # move the wave along the strip
        phase += speed

        if phase > 2 * math.pi:
            phase -= 2 * math.pi

async def main():
    while True:
        await water_waves(np)
try:
    uasyncio.run(main())
finally:
    uasyncio.new_event_loop()

