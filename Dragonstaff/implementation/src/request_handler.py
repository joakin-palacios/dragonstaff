import setupnfunctions as snf
import webpage
import uasyncio

# coroutine to handle HTTP request
async def handle_request(reader, writer):
    global status, color, wait
    try:
        snf.led.toggle()      
        # allow other tasks to run while waiting for data
        raw_request = await reader.read(2048)
        print(raw_request)

        raw_request=raw_request.split()[1]
        

        # try to serve static file
        await uasyncio.create_task(snf.modes(raw_request))
        # send reponse back to client
        if raw_request == b'inquisition':
            print (f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}')
            writer.write(bytes(f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}', 'utf-8'))
        else:
            html = await webpage.webpage(snf.color, snf.status)
#             print (html)
            writer.write(html)
        # allow other tasks to run while data being sent
        await writer.drain()
        await writer.wait_closed()

    except OSError as e:
        print('connection error ' + str(e.errno) + " " + str(e))
