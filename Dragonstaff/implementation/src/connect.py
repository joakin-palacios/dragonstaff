# connect
import network
import setupnfunctions as snf


async def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.AP_IF)
    wlan.active(False)
    wlan.config(ssid=snf.ssid, password=snf.password, channel=6, security=4)
    wlan.active(True)
    ip = wlan.ifconfig()[0]
#     print(f'Connected on {ip}')
    return ip