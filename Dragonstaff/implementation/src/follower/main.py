# Program to read RGB values from a local Pico Web Server
# Tony Goodhew 5th July 2022
# Connect to network
import network
import time
import socket
import setupnfunctions as snf
import neopixel
import uasyncio
import _thread

DEBUG= False

def parse_tuple(s):
    s = s.strip("() ")           # remove parentheses and spaces
    if not s:
        return tuple()
    return tuple(int(x) for x in s.split(','))

def interpret(ss):

    text = ss.decode('utf-8')
    parts = text.split('!!')
    s=[]
    x=0
    for i in parts:
        s.append(parts[x].split('/'))
        x=x+1
    if DEBUG:
        print(s)
    snf.np1.color = parse_tuple(s[0][0])
    snf.np1.co_color = parse_tuple(s[0][1])
    snf.np1.status = s[0][2]
    snf.np1.wait = int(s[0][3])
    snf.np1.magic_number = int(s[0][4])
    snf.np1.brightness = int(s[0][5])
    
    snf.np2.color = parse_tuple(s[1][0])
    snf.np2.co_color = parse_tuple(s[1][1])
    snf.np2.status = s[1][2]
    snf.np2.wait = int(s[1][3])
    snf.np2.magic_number = int(s[1][4])
    snf.np2.brightness = int(s[1][5])
    
    snf.np3.color = parse_tuple(s[2][0])
    snf.np3.co_color = parse_tuple(s[2][1])
    snf.np3.status = s[2][2]
    snf.np3.wait = int(s[2][3])
    snf.np3.magic_number = int(s[2][4])
    snf.np3.brightness = int(s[2][5])

    
def connect():
    if DEBUG:
        print ('i have started doing stuffffff !!!!')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.connect(snf.ssid, snf.password)

    while not wlan.isconnected():
        if DEBUG:
            print("Waiting to connect:")
            print (wlan.status())
        time.sleep(1)
        
    if DEBUG:
        print (wlan.isconnected() )
    # Should be connected and have an IP address
    wlan.status() # 3 == success
    wlan.ifconfig()
    if DEBUG:
        print(wlan.ifconfig())
    
def threaded_connection():
    while True:
        try:
            ai = socket.getaddrinfo("192.168.4.1", 80) # Address of Web Server
            addr = ai[0][-1]

            # Create a socket and make a HTTP request
            s = socket.socket() # Open socket
            s.connect(addr)
            s.send(b"THE inquisition") # Send request

            ss=s.recv(512) # Store reply
            # Print what we received
            interpret(ss)
#             print (f'{snf.status}  {snf.color} {snf.co_color} {snf.wait}')
            
            
            s.close()          # Close socket
            time.sleep(0.8)    # wait
        except OSError as e:
            print('connection error ' + str(e.errno) + " " + str(e))

            
async def main():
    chunks=uasyncio.create_task(snf.pixelones())
    ledBlink=uasyncio.create_task(snf.led_blink(10,700))
    while True:
        await uasyncio.sleep(1)



#     uasyncio.run(main())
_thread.start_new_thread(uasyncio.run, ([main()]))
connect()
threaded_connection()