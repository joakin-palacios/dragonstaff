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
    global this_side
    
    current_status = this_side.status
    
    if this_side.status=='start_up':
        await uasyncio.gather(initialize(np),
                              initialize(np2),
                              initialize(np3)) #---- initialize them lights ! ----
    status_functions = {
        'start_up': lambda: uasyncio.gather(initialize(np), initialize(np2), initialize(np3)),
        'Monochrome': lambda: uasyncio.gather(fillpix(np), fillpix(np2), fillpix(np3)),
        'Blink': lambda: uasyncio.gather(blink(np), blink(np2), blink(np3)),
        'Cycle': lambda: uasyncio.gather(cycle(np), cycle(np2), cycle(np3)),
        'Bycle': lambda: uasyncio.gather(bycle(np), bycle(np2), bycle(np3)),
        'Bounce': lambda: uasyncio.gather(bounce(np), bounce(np2), bounce(np3)),
        'MPU Sensor': lambda: None,  # Placeholder
        'Rainbow': lambda: uasyncio.gather(rainbow(np), rainbow(np2), rainbow(np3)),
        'Firework': lambda: uasyncio.gather(firework(np), firework(np2), firework(np3)),
        'OnlyEnds': lambda: uasyncio.gather(only_ends(np), only_ends(np2), only_ends(np3)),
        'OnlyEndsBlink': lambda: uasyncio.gather(only_ends(np, blink=True), only_ends(np2, blink=True), only_ends(np3, blink=True)),
        'AdditiveRandom': lambda: uasyncio.gather(additive_random(np), additive_random(np2), additive_random(np3)),
        'WaterWaves': lambda: uasyncio.gather(water_waves(np), water_waves(np2), water_waves(np3)),
        'TrigonometricFade': lambda: uasyncio.gather(trigonometric_fade(np), trigonometric_fade(np2), trigonometric_fade(np3)),
        'Random': lambda: uasyncio.gather(random(np), random(np2), random(np3)),
    }
    while True:
        if current_status != this_side.status:
            current_status = this_side.status
            routine = status_functions.get(current_status)
            if routine:
                while this_side.status == current_status:
                    await routine() 

        await uasyncio.sleep_ms(100)

async def side_parser(request):
    global this_side, side_b
    # first determines which side needs a change and then calls the function to change the global params
    if "/side_b" in request :
        this_side.last_side = "side_b"    
    elif "/side_a" in request:
        this_side.last_side = "side_a"        
    elif "/both_sides" in request:
        this_side.last_side = "both_sides"
        
    if this_side.last_side ==  "side_a":
        await modes(request, this_side)
    elif this_side.last_side ==  "side_b":
        await modes(request, side_b)
    else:
        await uasyncio.gather(modes(request, this_side), modes(request, side_b))
        
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
    global this_side       
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
        if this_side.status!='Rainbow': # break if the mode has changed
            break
        for i in range(n): # sets each Led to the corresponding rainbow-wheel color
            rc_index = (i * 256 // n) + j
            np.setcolor(ith_led=i, color=wheel(rc_index & 255))
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(int(this_side.wait/5))


async def fillpix(np):
    global this_side
    np.np.fill(this_side.color)
    await uasyncio.sleep(0)
    np.illuminate()

async def initialize(np):
    global this_side
    n=np.n
    for i in range (n):
        np.setcolor(ith_led=i, color=COLORS[i%len(COLORS)])
        await uasyncio.sleep(0)
        np.illuminate()

async def cycle(np, rounds=1):
    global this_side
    n = np.n
    # cycle
    for i in range(rounds * n):
        if this_side.status!='Cycle':
            break
        np.np.fill(this_side.co_color)
        np.setcolor(i % n, color=this_side.color)
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(this_side.wait)


async def bycle(np, rounds=1):
    global this_side
    n = np.n
    # bycle
    for i in range(rounds * n):
        if this_side.status!='Bycle':
            break
        np.np.fill(BLACK)
        np.setcolor(i % n, this_side.color)
        np.setcolor(n-1-(i % n), this_side.color)
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(this_side.wait)


async def bounce(np, rounds=2):
    global this_side
    n = np.n
    for i in range(rounds * n):
        if this_side.status!='Bounce':
            break
        np.np.fill(this_side.color)            # color all them pixels 
        if (i // n) % 2 == 0:     # check if it is going forward
            np.setcolor(i % n, this_side.co_color) # co_color out the i-th led 
        else:
            np.setcolor(n - 1 - (i % n), this_side.co_color)
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(this_side.wait)
        
def map_to_rgb(x, y, z):
    r = int(abs(x)/2*255)
    g = int(abs(y)/2*255)
    b = int(abs(z)/2*255)

    return r, g, b

async def blink(np) :
    global this_side
#     This function takes in a neopixel object.
#     Saves its values before changing it to all black.
#     writes the black, waits a set time and then rewrites the saved colors back (and writes them).    
    n=np.n
    previous_np=[0 for _ in range(n)]
    for i in range(n):
        previous_np[i]=np.np[i]
    np.np.fill(this_side.co_color)
    np.illuminate()
    await uasyncio.sleep_ms(this_side.wait*5)
    for i in range(n):
        np.setcolor(i, previous_np[i])
        await uasyncio.sleep(0)
    np.illuminate()
    await uasyncio.sleep_ms(this_side.wait*5)

async def led_blink(on_time_ms = 5, off_time_ms= 5) :
    while True:
        led.on()
        await uasyncio.sleep_ms(on_time_ms)
        led.off()
        await uasyncio.sleep_ms(off_time_ms)

async def firework(np, divider=2, pops=15):
    global this_side
    icolor = this_side.color
    icocolor = this_side.co_color
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
        if this_side.status!='Firework': # break if the mode has changed
            break
        np.np.fill(BLACK)         # make all leds Black !
        np.np[i % n] = icolor        # turn the i-th led to the color
        np.np[n-1-i % n] = icolor        # turn the i-th led to the color
        await uasyncio.sleep(0)  # wait for all them nps to be done 
        np.illuminate()
        await uasyncio.sleep_ms(this_side.wait)
        
        np.np[i % n] = icocolor        # turn the i-th led to the color
        np.np[n-1-i % n] = icocolor 
        await uasyncio.sleep(0)  # wait for all them nps to be done 
        np.illuminate()
        await uasyncio.sleep_ms(this_side.wait)
        
    np.np.fill(BLACK)
    repeat_pulses(2, icolor)
    await uasyncio.sleep(0)
    np.illuminate()
    await uasyncio.sleep_ms(this_side.wait*2)
    repeat_pulses(2, icocolor)
    await uasyncio.sleep(0)
    np.illuminate()
    await uasyncio.sleep_ms(this_side.wait*2)
    
    for i in range (pops):
        if this_side.status!='Firework': # break if the mode has changed
            break
        repeat_pulses(3, icolor) 
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(this_side.wait*2)
        repeat_pulses(3, icocolor) 
        await uasyncio.sleep(0)
        np.illuminate()
        await uasyncio.sleep_ms(this_side.wait*2)
        
        icolor = (int(icolor[0]*factor),int(icolor[1]*factor),int(icolor[2]*factor))
        icocolor = (int(icocolor[0]*factor),int(icocolor[1]*factor),int(icocolor[2]*factor))
    
    
async def random(np):
    global this_side
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
    rand_wait=Rondo.randrange(this_side.wait)
    
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
    global this_side
    n=np.n
    for i in range (end_length):
        np.setcolor(ith_led= 9-i, color=this_side.color)
        np.setcolor(ith_led= 10+i, color=this_side.color)
    np.illuminate()
    await uasyncio.sleep_ms(this_side.wait)
    if blink:
        for i in range (end_length):
            np.setcolor(ith_led= 9-i, color=this_side.co_color)
            np.setcolor(ith_led= 10+i, color=this_side.co_color)
        np.illuminate()            
        await uasyncio.sleep_ms(this_side.wait)
        
async def additive_random(np):
    global this_side
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
    await uasyncio.sleep_ms(this_side.wait)
    
async def water_waves(np, waves=2, speed_factor=1, divider=2):
    global this_side
    n = np.n
    if (n % 2 == 0):
        d = int(n/divider) # d = 20/2 = 10
    else:
        d = int((n-1)/divider)
    speed=math.pi*speed_factor*0.1
    rounds = int(2*math.pi/speed)

    this_side.color = (0, 0, 80)
    this_side.co_color = (0, 150, 255)

   # smooth color blending between two colors
    def blend(c1, c2, t):
        return (
            int(c1[0] + (c2[0] - c1[0]) * t),
            int(c1[1] + (c2[1] - c1[1]) * t),
            int(c1[2] + (c2[2] - c1[2]) * t) )

    phase = 0
    for j in range (rounds):
        if this_side.status!='WaterWaves':
            break
        for i in range(d):
            # sine wave pattern across LEDs
            wave = math.sin((i / d) * waves * 2 * math.pi - phase)
            # normalize -1..1 to 0..1
            t = (wave + 1) / 2
	# blend between deep blue and light blue
            np.np[i] = blend(this_side.color, this_side.co_color, t)
            np.np[n-1-i] = blend(this_side.color, this_side.co_color, t)

        np.illuminate()
        await uasyncio.sleep(0)
        await uasyncio.sleep_ms(this_side.wait)

        # move the wave along the strip
        phase += speed

        if phase > 2 * math.pi:
            phase -= 2 * math.pi
            
            
async def trigonometric_fade(np, steps=20):
    global this_side

    def ease(t):
        return 0.5 * (1 - math.cos(math.pi * t))
    
    def blend(c1, c2, t):
        """Blend two RGB colors by fraction t (0–1)."""
        return (
            int(c1[0] + (c2[0] - c1[0]) * t),
            int(c1[1] + (c2[1] - c1[1]) * t),
            int(c1[2] + (c2[2] - c1[2]) * t))

    for i in range(steps + 1):
        if this_side.status != 'TrigonometricFade':
            break
        t = ease(i / steps)
        color_now = blend(this_side.co_color, this_side.color, t)
        np.np.fill(color_now)
        np.illuminate()
        await uasyncio.sleep(0)
        await uasyncio.sleep_ms(this_side.wait)

    # Fade backward (to → from)
    for i in range(steps + 1):
        if this_side.status != 'TrigonometricFade':
            break
        t = ease(i / steps)
        color_now = blend(this_side.color, this_side.co_color, t)
        np.np.fill(color_now)
        np.illuminate()
        await uasyncio.sleep(0)
        await uasyncio.sleep_ms(this_side.wait)
