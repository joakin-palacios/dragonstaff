import setupnfunctions as snf
import uasyncio
import _thread
import com_stack

Lead = True
  


async def main():
    chunks=uasyncio.create_task(snf.pixelones())
    ledBlink=uasyncio.create_task(snf.led_blink(10,700))
    while True:
        await uasyncio.sleep(1) 


com_stack.connect(Lead=Lead)

try:
    _thread.start_new_thread(uasyncio.run, ([main()]))
except OSError as e:
    print('connection error ' + str(e.errno) + " " + str(e))
    
com_stack.threaded_connection()