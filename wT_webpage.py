import network
import setupnfunctions as snf
from machine import Pin
import neopixel
import uasyncio
import wT_webpage

import connect
import request_handler
import webpage

Lead = True



async def handle_request(reader, writer):
    global status, color, wait
    try:
        snf.led.toggle()      
        # allow other tasks to run while waiting for data
        raw_request = await reader.read(2048)
        print(raw_request)

        raw_request=raw_request.split()[1]
        

        # try to serve static file
#        await uasyncio.create_task(snf.modes(raw_request))
        # send reponse back to client
        if raw_request == b'inquisition':
            print (f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}')
            writer.write(bytes(f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}', 'utf-8'))
        else:
            html = wT_webpage.webpage(wT_webpage.web_request_parser(raw_request))
#             print (html)
            writer.write(html)
        # allow other tasks to run while data being sent
        await writer.drain()
        await writer.wait_closed()

    except OSError as e:
        print('connection error ' + str(e.errno) + " " + str(e))



async def main():
    global status, color
    uasyncio.new_event_loop()
    ip=await connect.connect()
    await uasyncio.sleep(1)
#     print('Setting up webserver...')
    server = uasyncio.start_server(handle_request, '192.168.4.1', 80)
    task=uasyncio.create_task(server)
    while True:
        status_report = task.done()
        if status_report:
            break
        await uasyncio.sleep(0.1)
    chunks=uasyncio.create_task(snf.pixelones())
    ledBlink=uasyncio.create_task(snf.led_blink(10,700))
    status="Cycle"
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




