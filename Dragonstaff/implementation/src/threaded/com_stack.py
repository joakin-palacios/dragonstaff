import network
import setupnfunctions as snf
import socket
import time
import webpage
import parser

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
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

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
            raw_request = conn.recv(2048)
            print(raw_request)
            
            request_str = raw_request.decode()
            request_line = request_str.split('\r\n')[0]
            print("Request line:", request_line)

            # Split and safely extract path
            parts = request_line.split()
            if len(parts) >= 2:
                method = parts[0]
                path = parts[1]
                
                if path == '/inquisition':
                    print(f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}')
                    conn.sendall(bytes(f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}', 'utf-8'))
                else:
                    parser.modes(path)
                    html = webpage.webpage(snf.color, snf.status)
                    conn.sendall(html)
            else:
                print("Malformed request:", request_line)
                conn.sendall(b"HTTP/1.1 400 Bad Request\r\n\r\n")
# 
#             try:
#                 raw_request=raw_request.split()[1]
#             except OSError as e:
#                 print('connection error ' + str(e.errno) + " " + str(e))
#             if raw_request == b'inquisition':
#                 print (f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}')
#                 conn.sendall(bytes(f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}', 'utf-8'))
#             else:
#                 parser.modes(raw_request)
#                 html = webpage.webpage(snf.color, snf.status)
#                 conn.sendall(html)
            conn.close()
        except OSError as e:
            print('connection error ' + str(e.errno) + " " + str(e))
        finally :
            pass
            