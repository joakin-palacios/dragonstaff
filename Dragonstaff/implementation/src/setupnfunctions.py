from machine import Pin
import neopixel
import uasyncio
import random as Rondo
import ledspokehandler
import math

# General Setup
class Side:
    color = (40,128,20)
    co_color = (0,0,0)
    status = "start_up"
    wait = 60
    last_side="both_sides"
    
this_side = Side()
side_b = Side()

led = Pin("LED", Pin.OUT)

# Wifi Setup
ssid = '''J's DragonStaff'''
password = 'flowstate'


BLACK = (0, 0, 0)
RED = (128, 0, 0)
YELLOW = (128, 75, 0)
GREEN = (0, 128, 0)
CYAN = (0, 128, 128)
BLUE = (0, 0, 128)
PURPLE = (90, 0, 128)
WHITE = (128, 128, 128)
ORANGE = (140,50,0)
COLORS = (RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, ORANGE, WHITE, BLACK)


# Neopixel Setup
BRIGHTNESS= 0.05 # between 0 and 1
np = ledspokehandler.ledSpoke(mcuPin=19, nr_of_leds=20)
np2 = ledspokehandler.ledSpoke(mcuPin=20, nr_of_leds=20) 
np3 = ledspokehandler.ledSpoke(mcuPin=21, nr_of_leds=20) 




# General functions
async def pixelones():
# controls all neopixels asynchronously depending on the mode and the color
# if the status changes, then it changes the routine,
# if the color changes, then it changes the color,
# if nothing changes, then it continues doing whatever it was doing, until it detects a change
    global this.side
    
    current_status = this_side.status
    
    if this_side.status=='start_up':
        await uasyncio.gather(initialize(np),
                              initialize(np2),
                              initialize(np3)) #---- initialize them lights ! ----
            
    while True:
        if current_status != this_side.status :
            #detects a change in the force and acts upon it !
            #otherwise the functions themselves should be the ones that keep alive?
            if this_side.status=='start_up':
                current_status = 'start_up'
                await uasyncio.gather(initialize(np), initialize(np2), initialize(np3)) #---- initialize them lights ! ----
            elif this_side.status=='Monochrome':
                current_status = 'Monochrome'
                while this_side.status=='Monochrome':
                    await uasyncio.gather(fillpix(np), fillpix(np2), fillpix(np3))
            elif this_side.status== 'Blink':
                current_status = 'Blink'
                while this_side.status=='Blink':
                    await uasyncio.gather(blink(np), blink(np2), blink(np3))
            elif this_side.status== 'Cycle':
                current_status = 'Cycle'
                while this_side.status=='Cycle':
                    await uasyncio.gather(cycle(np), cycle(np2), cycle(np3))
            elif this_side.status== 'Bycle':
                current_status = 'Bycle'
                while this_side.status=='Bycle':
                    await uasyncio.gather(bycle(np), bycle(np2), bycle(np3))                
            elif this_side.status== 'Bounce':
                current_status = 'Bounce'
                while this_side.status=='Bounce':
                    await uasyncio.gather(bounce(np), bounce(np2), bounce(np3))
            elif this_side.status== 'MPU Sensor':
                current_status = 'MPU Sensor'
                pass
            elif this_side.status== 'Rainbow':
                current_status = 'Rainbow'
                while this_side.status=='Rainbow':
                    await uasyncio.gather(rainbow(np), rainbow(np2), rainbow(np3))
            elif this_side.status== 'Firework':
                current_status = 'Firework'
                while this_side.status=='Firework':
                    await uasyncio.gather(firework(np), firework(np2), firework(np3))
            elif this_side.status== 'OnlyEnds':
                current_status = 'OnlyEnds'
                while this_side.status=='OnlyEnds':
                    await uasyncio.gather(only_ends(np), only_ends(np2), only_ends(np3))
            elif this_side.status== 'OnlyEndsBlink':
                current_status = 'OnlyEndsBlink'
                while this_side.status=='OnlyEndsBlink':
                    await uasyncio.gather(only_ends(np, blink=True), only_ends(np2, blink=True), only_ends(np3, blink=True))
            elif this_side.status== 'AdditiveRandom':
                current_status = 'AdditiveRandom'
                while this_side.status=='AdditiveRandom':
                    await uasyncio.gather(additive_random(np), additive_random(np2), additive_random(np3))          
            elif this_side.status== 'WaterWaves':
                current_status = 'WaterWaves'
                while this_side.status=='WaterWaves':
                    await uasyncio.gather(water_waves(np), water_waves(np2), water_waves(np3))
            elif this_side.status== 'TrigonometricFade':
                current_status = 'TrigonometricFade'
                while this_side.status=='WaterWaves':
                    await uasyncio.gather(trigonometric_fade(np), trigonometric_fade(np2), trigonometric_fade(np3))          
            elif this_side.status== 'Random':
                current_status = 'Random'
                while this_side.status=='Random':
                    await uasyncio.gather(random(np), random(np2), random(np3))
            current_color = color
        await uasyncio.sleep_ms(100)

async def side_parser(request):
    global this_side, side_b
    # first determines which side needs a change and then calls the function to change the global params
    if "side_b" in request :
        this_side.last_side = "side_b"    
    elif "side_a" in request:
        this_side.last_side = "side_a"        
    elif "both_sides" in request:
        this_side.last_side = "both_sides"
        
    if this_side.last_side ==  "side_a":
        await modes(request, this_side)
    elif this_side.last_side ==  "side_b":
        await modes(request, side_b)
    else:
        await asyncio.gather(modes(request, this_side), modes(request, side_b))
        
async def modes(request, side_in_question):

    if "main_color" in request :
        side_in_question.color=findrgbs(request)
        
    if "co_color" in request :
        side_in_question.co_color=findrgbs(request)    
        
    if "wait" in request:
        side_in_question.wait = set_waiting_time(request)
        
    commands = {
        "/monochrome": "Monochrome",
        "/blink": "Blink",
        "/cycle": "Cycle",
        "/bycle": "Bycle",
        "/bounce": "Bounce",
        "/MPU": "MPU Sensor",
        "/rainbow": "Rainbow",
        "/firework": "Firework",
        "/random_xD": "Random",
        "/only_ends": "OnlyEnds",
        "/only_blink": "OnlyEndsBlink",
        "/add_random": "AdditiveRandom",
        "/water_waves": "WaterWaves",
        "/trigonometric_fade": "TrigonometricFade",
    }

    for cmd, value in commands.items():
        if cmd in request:
            side_in_question.status = value
            break        

    await uasyncio.sleep(0)
    
def set_waiting_time(raw_request):
    get_string=str(raw_request)
    start_index = get_string.find("wait=") + len("wait=")
    end_index = len(get_string)-1
    if start_index!= end_index: 
        wait_time = int(float(get_string[start_index:end_index]))
    else:
        wait_time=60
    print (f"time has set to {wait_time}")
    return wait_time
    
def findrgbs(string):
    # Extract the color code from the string
    string=str(string)
    color_code = string.split('=')[1].strip()

    # Convert the color code to RGB tuple
    r = int(color_code[3:5], 16)
    g = int(color_code[5:7], 16)
    b = int(color_code[7:9], 16)
#     print (color_code[3:5],color_code[5:7],color_code[7:9])

    return (r, g, b)


# Neopixel functions
async def rainbow(np):
    global status, wait      
    n=np.n
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        # Uses 85 cuz 255/3 = 85
        if pos < 0 or pos > 255: # Out of bound
            return (0, 0, 0)
        if pos < 85: 
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)
     
    for j in range(255): # does a FULL lap around the color wheel in steps of 3
        if status!='Rainbow': # break if the mode has changed
            break
        for i in range(n): # sets each Led to the corresponding rainbow-wheel color
            rc_index = (i * 256 // n) + j
            np.setcolor(ith_led=i, color=wheel(rc_index & 255))
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(int(wait/5))




async def fillpix (np):
    global color
    np.np.fill(color)
    await uasyncio.sleep(0)
    np.illuminate()

async def initialize(np):
    n=np.n
    for i in range (n):
        np.setcolor(ith_led=i, color=COLORS[i%len(COLORS)])
        await uasyncio.sleep(0)
        np.illuminate()

async def cycle(np, rounds=1):
    global wait, color, co_color
    n = np.n
    # cycle
    for i in range(rounds * n):
        if status!='Cycle': # break if the mode has changed
            break
        np.np.fill(co_color)         # make all leds co_colored !
        np.setcolor(i % n, color=color)        # turn the i-th led to the color
        await uasyncio.sleep(0)  # wait for all them nps to be done 
        np.illuminate()
        await uasyncio.sleep_ms(wait)

async def bycle(np, rounds=1):
    global wait, color, co_color
    n = np.n
    # bycle
    for i in range(rounds * n):
        if status!='Bycle': # break if the mode has changed
            break
        np.np.fill(BLACK)         # make all leds BLACK !
        np.setcolor(i % n, color)
        np.setcolor(n-1-(i % n), color)
        # turn the i-th led to the color
        await uasyncio.sleep(0)  # wait for all them nps to be done 
        np.illuminate()
        await uasyncio.sleep_ms(wait)

async def bounce(np, rounds=2):
    global wait, color
    n = np.n
    for i in range(rounds * n):
        if status!='Bounce': # break if the mode has changed
            break
        np.np.fill(color)            # color all them pixels 
        if (i // n) % 2 == 0:     # check if it is going forward
            np.setcolor(i % n, co_color) # co_color out the i-th led 
        else:
            np.setcolor(n - 1 - (i % n), co_color)
        await uasyncio.sleep(0)    
        np.illuminate()
        await uasyncio.sleep_ms(wait)
        
def map_to_rgb(x, y, z):
    r = int(abs(x)/2*255)
    g = int(abs(y)/2*255)
    b = int(abs(z)/2*255)

    return r, g, b

async def blink(np) :
    global wait
#     This function takes in a neopixel object.
#     Saves its values before changing it to all black.
#     writes the black, waits a set time and then rewrites the saved colors back (and writes them).    
    n=np.n
    previous_np=[0 for _ in range(n)]
    for i in range(n):
        previous_np[i]=np.np[i]
    np.np.fill(co_color)
    np.illuminate()
    await uasyncio.sleep_ms(wait*5)
    for i in range(n):
        np.setcolor(i, previous_np[i])
        await uasyncio.sleep(0)
    np.illuminate()
    await uasyncio.sleep_ms(wait*5)

async def led_blink(on_time_ms = 5, off_time_ms= 5) :
    while True:
        led.on()
        await uasyncio.sleep_ms(on_time_ms)
        led.off()
        await uasyncio.sleep_ms(off_time_ms)

async def firework(np, divider=2, pops=15):
    global wait, color, co_color
    icolor = color
    icocolor = co_color
    factor = 0.75
    n = np.n
    if (n % 2 == 0):
        d = int(n/divider) # d = 20/2 = 10
    else:
        d = int((n-1)/divider)
        
    def repeat_pulses(rounds, fcolor):
        for v in range (rounds):
            np.np[d-v-1] = fcolor
            np.np[d+v] = fcolor
            
    # cycle
    for i in range(d): # goes from 0 to 9
        if status!='Firework': # break if the mode has changed
            break
        np.np.fill(BLACK)         # make all leds Black !
        np.np[i % n] = icolor        # turn the i-th led to the color
        np.np[n-1-i % n] = icolor        # turn the i-th led to the color
        await uasyncio.sleep(0)  # wait for all them nps to be done 
        np.illuminate()
        await uasyncio.sleep_ms(wait)
        
        np.np[i % n] = icocolor        # turn the i-th led to the color
        np.np[n-1-i % n] = icocolor 
        await uasyncio.sleep(0)  # wait for all them nps to be done 
        np.illuminate()
        await uasyncio.sleep_ms(wait)
        
    np.np.fill(BLACK)
    repeat_pulses(2, icolor)
    await uasyncio.sleep(0)
    np.illuminate()
    await uasyncio.sleep_ms(wait*2)
    repeat_pulses(2, icocolor)    
    await uasyncio.sleep(0)
    np.illuminate()
    await uasyncio.sleep_ms(wait*2)
    
    for i in range (pops):
        if status!='Firework': # break if the mode has changed
            break
        repeat_pulses(3, icolor) 
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(wait*2)
        repeat_pulses(3, icocolor) 
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(wait*2)
        
        icolor = (int(icolor[0]*factor),int(icolor[1]*factor),int(icolor[2]*factor))
        icocolor = (int(icocolor[0]*factor),int(icocolor[1]*factor),int(icocolor[2]*factor))
    
    
async def random(np):
    global wait
    # random leds get turned into random colors for a random amout of time :D
    # First we calculate the random nr of colors that will be colored
    
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        # Uses 85 cuz 255/3 = 85
        if pos < 0 or pos > 255: # Out of bound
            return (0, 0, 0)
        if pos < 85: 
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)
    
    n=np.n
    # how many leds will be on
    leds_on= Rondo.randrange(n) 
    
    # random wait time
    rand_wait=Rondo.randrange(wait)
    
    #make all leds black
    np.np.fill(BLACK)
    
    # Usual list
    U_list= list(range(n))
    
    # randomly chosen nrs out of list
    # choose something out of the list and then delete from list // add to new list
    rand_list = []
    for x in range(leds_on):
        choice = Rondo.choice(U_list)
        rand_list.append(choice)
        U_list.remove(choice)
    
    # pick a 'leds_on' nr of items out of a range n list, asign a random color (from the weel)
    for i in rand_list:
        np.np[i]= wheel(Rondo.randrange(256))
    np.illuminate()    
    await uasyncio.sleep_ms(rand_wait)
    
async def only_ends(np, end_length=3, blink=False):
    global wait, color, co_color
    n=np.n
    for i in range (end_length):
        np.setcolor(ith_led= 9-i, color = color)
        np.setcolor(ith_led= 10+i, color = color)
    np.illuminate()
    await uasyncio.sleep_ms(wait)
    if blink:
        for i in range (end_length):
            np.setcolor(ith_led= 9-i, color = co_color)
            np.setcolor(ith_led= 10+i, color = co_color)
        np.illuminate()            
        await uasyncio.sleep_ms(wait)
        
async def additive_random(np):
    global wait
    n=np.n
    # ONE random led gets turned into a random color for
    
    def wheel_two(pos, steps=1024):
        pos = pos % steps
        segment = steps // 3
        if pos < segment:
            return (
                255 - int(pos * 255 / segment),
                int(pos * 255 / segment),
                0
            )
        elif pos < 2 * segment:
            pos -= segment
            return (
                0,
                255 - int(pos * 255 / segment),
                int(pos * 255 / segment)
            )
        else:
            pos -= 2 * segment
            return (
                int(pos * 255 / segment),
                0,
                255 - int(pos * 255 / segment)
            )

    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        # Uses 85 cuz 255/3 = 85
        if pos < 0 or pos > 255: # Out of bound
            return (0, 0, 0)
        if pos < 85: 
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)
    lucky_Led = Rondo.randrange(n)
    lucky_color = wheel_two(Rondo.randrange(1024))
#     lucky_color = wheel(Rondo.randrange(256))
#     lucky_color = (Rondo.randrange(256),Rondo.randrange(256),Rondo.randrange(256))
    np.setcolor(ith_led= lucky_Led, color = lucky_color)
    np.illuminate()
    await uasyncio.sleep_ms(wait)
    
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
        if status!='WaterWaves': # break if the mode has changed
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
            
async def trigonometric_fade(np, steps=20):
    global wait, status, color, co_color

    def ease(t):
        return 0.5 * (1 - math.cos(math.pi * t))
    
    def blend(c1, c2, t):
        """Blend two RGB colors by fraction t (0–1)."""
        return (
            int(c1[0] + (c2[0] - c1[0]) * t),
            int(c1[1] + (c2[1] - c1[1]) * t),
            int(c1[2] + (c2[2] - c1[2]) * t))

    for i in range(steps + 1):
        if status != 'TrigonometricFade':
            break
        t = ease(i / steps)
        color_now = blend(co_color, color, t)
        np.np.fill(color_now)
        np.illuminate()
        await uasyncio.sleep(0)
        await uasyncio.sleep_ms(wait)

    # Fade backward (to → from)
    for i in range(steps + 1):
        if status != 'TrigonometricFade':
            break
        t = ease(i / steps)
        color_now = blend(color, co_color, t)
        np.np.fill(color_now)
        np.illuminate()
        await uasyncio.sleep(0)
        await uasyncio.sleep_ms(wait)