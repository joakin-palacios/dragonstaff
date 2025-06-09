import network
import setupnfunctions as snf
import socket
import time
import webpage
import parser
import select

def connect(Lead):
    if Lead:
        wlan = network.WLAN(network.AP_IF)
        wlan.active(False)
        wlan.config(ssid=snf.ssid, password=snf.password, channel=6, security=4)
        wlan.active(True)
        ip = wlan.ifconfig()[0]
        print ("my ip is: "+ip)
        
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
    s.bind(("192.168.4.1", 80))

    # Start listening for connections
    s.listen(5)
    s.setblocking(False)
    
    poller = select.poll()
    poller.register(s, select.POLLIN)
    
    clients = []

    print("Server is listening...")

    while True:
        events = poller.poll(1000)  # 100 ms timeout

        for sock, event in events:
            if sock is s:
                # Accept new client
                client, addr = s.accept()
                print("Client connected from", addr)
                client.setblocking(False)
                poller.register(client, select.POLLIN)
                clients.append(client)

            elif event & select.POLLIN:
                try:
                    data = sock.recv(1024)
                    if data:
#                         print("Received from", sock, ":", data)
                        requested_action=data.split()[1]
#                         print (requested_action)
                        if data == b'inquisition':
#                             print (f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}')
                            sock.sendall(bytes(f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}', 'utf-8'))
                        else:
                            parser.modes(requested_action)
#                             print(requested_action)
                            html = webpage.webpage(snf.color, snf.status)
                            sock.sendall(html)
#                             print("tried sending html")

                    else:
                        # Connection closed
#                         print("Client disconnected:", sock)
                        poller.unregister(sock)
                        clients.remove(sock)
                        sock.close()
                except OSError:
                    # Possibly a disconnection or read error
                    poller.unregister(sock)
                    if sock in clients:
                        clients.remove(sock)
                    sock.close()
#         try:
#             # Accept an incoming connection
#             conn, addr = s.accept()
#             print(f"Connected by {addr}")
# 
#             # Receive data from the client
#             raw_request = conn.recv(1024)
# #             print("raw request:"+raw_request)
#             if  raw_request != b'':          
#                 requested_action=raw_request.split()[1]
#                 print("requested action")
#                 print(requested_action)                
#             if raw_request == b'inquisition':
# #                 print (f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}')
#                 conn.sendall(bytes(f'{snf.status}  {snf.color}  {snf.co_color}  {snf.wait}', 'utf-8'))
#             else:
#                 parser.modes(requested_action)
#                 html = webpage.webpage(snf.color, snf.status)
#                 conn.sendall(html)
#             conn.close()
#         except OSError as e:
#             print('connection error ' + str(e.errno) + " " + str(e))
#         finally :
#             pass
#             