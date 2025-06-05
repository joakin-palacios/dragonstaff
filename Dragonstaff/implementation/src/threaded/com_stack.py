import network
import setupnfunctions as snf
import socket
import time


def connect(Lead):
    if Lead:
        wlan = network.WLAN(network.AP_IF)
        wlan.active(False)
        wlan.config(ssid=snf.ssid, password=snf.password, channel=6, security=4)
        wlan.active(True)
        ip = wlan.ifconfig()[0]
        
    elif Lead == False:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(False)
        wlan.active(True)
        wlan.connect(snf.ssid, snf.password)
        
        while not wlan.isconnected():
            print("Waiting to connect:")
            print (wlan.status())
            time.sleep(1)
            
#         wlan.status() # 3 == success
#         wlan.ifconfig()
#         print(wlan.ifconfig())
    
def threaded_connection():
    # Create a socket (IPv4, TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind to an address and port
    s.bind(('192.168.4.1', 80))

    # Start listening for connections
    s.listen()

    print("Server is listening...")

    while True:
        try:
            # Accept an incoming connection
            conn, addr = s.accept()
            print(f"Connected by {addr}")

            # Receive data from the client
            data = conn.recv(1024)
            print(f"Received: {data}")

            # Send a response
            conn.sendall(b'Hello from server!')

            # Close the connection
            conn.close()
        except OSError as e:
            print('connection error ' + str(e.errno) + " " + str(e))
            