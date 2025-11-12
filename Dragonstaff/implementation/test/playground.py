import asyncio
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
async def initialize(np):
        print(np.status)        
async def main():        
    np1 = otherSideSpoke()
    print(np1.status)
    np2 = otherSideSpoke()
    np3 = otherSideSpoke()
    np3.status="hi"

    spokes = {1: np1, 2: np2, 3: np3}
    spokes_active = [1,2,3]

    current_status=[]
    for x in spokes_active:
        current_status.append(spokes[x].status)
    if any(spokes[x].status == 'hi' for x in spokes_active):
        await asyncio.gather(*(initialize(spokes[x]) for x in spokes_active if spokes[x].status == 'hi')) 

try:
    asyncio.run(main())
finally:
    asyncio.new_event_loop()


