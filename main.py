import network
import setupnfunctions as snf
from machine import Pin
import neopixel
import uasyncio

import connect
import request_handler
import webpage

Lead = True


# call connect
# loop
#   call request handler
#   call webpage handler
#   call pixelones


# main coroutine to boot async tasks
# ----- start web server task
# ------ check if the task of the web server is done
# get the status of the task
# report the status
#         print(f'>task done: {task.done()}')
# check if the task is done
# otherwise block for a moment
# ------ creates the task that manages the led stripes    


async def main():
    global status, color
    uasyncio.new_event_loop()
    ip=await connect.connect()
    await uasyncio.sleep(1)
#     print('Setting up webserver...')
    server = uasyncio.start_server(request_handler.handle_request, '192.168.4.1', 80)
    task=uasyncio.create_task(server)
    while True:
        status_report = task.done()
        if status_report:
            break
        await uasyncio.sleep(0.1)
    chunks=uasyncio.create_task(snf.pixelones())
    ledBlink=uasyncio.create_task(snf.led_blink(10,700))
    while True:
        await uasyncio.sleep(0)
#         print (f"current status: {status} \n current color: {color}" )


# start asyncio task and loop
# start the main async tasks
# reset and start a new event loop for the task scheduler


try:
    uasyncio.run(main())
finally:
    uasyncio.new_event_loop()


