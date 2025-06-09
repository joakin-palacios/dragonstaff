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

def interpret(ss):
    pub=str(ss).replace("b", "",1).replace("'", "").replace("(", "").replace(")", "").replace(",", "").split()
    snf.status=pub[0]
    snf.wait=int(pub[-1])
    snf.color=(int(pub[1]),int(pub[2]),int(pub[3]))
    snf.co_color=(int(pub[4]),int(pub[5]),int(pub[6]))
    
def connect():
    print ('i have started doing stuffffff !!!!')
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    wlan.active(True)
    wlan.connect(snf.ssid, snf.password)

    while not wlan.isconnected():
        print("Waiting to connect:")
        print (wlan.status())
        time.sleep(1)
        
    print (wlan.isconnected() )
    # Should be connected and have an IP address
    wlan.status() # 3 == success
    wlan.ifconfig()
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
    while True:
        await uasyncio.sleep(1)



#     uasyncio.run(main())
 
connect()
_thread.start_new_thread(uasyncio.run, ([main()]))
threaded_connection()