import network
import secrets
import time
import machine

CONNECT_GIVEUP = 15

def init_wlan():
    print('intializing wlan')
    wlanconn = network.WLAN(network.STA_IF)
    wlanconn.active(True)
    wlanconn.connect(secrets.SSID, secrets.PASSWORD)
    print('wlan connecting initiated')

    # use onboard LED to indicate connection status to WLAN
    led = machine.Pin("LED", machine.Pin.OUT)
    counter: int = 0

    while (wlanconn.isconnected() == False and counter < CONNECT_GIVEUP):
        if wlanconn.status() == network.STAT_IDLE:
            print('wlan status: STAT_IDLE')
        elif wlanconn.status() == network.STAT_CONNECTING:
            print('wlan status: STAT_CONNECTING')
        elif wlanconn.status() == network.STAT_WRONG_PASSWORD:
            print('wlan status: STAT_WRONG_PASSWORD')
        elif wlanconn.status() == network.STAT_NO_AP_FOUND:
            print('wlan status: STAT_NO_AP_FOUND')
        elif wlanconn.status() == network.STAT_CONNECT_FAIL:
            print('wlan status: STAT_CONNECT_FAIL')
        counter = counter + 1
        led.off()
        time.sleep(1)
        led.on()

    led.off()
    print('Connection complete. Connect: ' + str(wlanconn.isconnected()))

    if (wlanconn.isconnected() == True):
        led.on()
        print('WLAN connected successfully.')
        print('IP Address: ' + wlanconn.ifconfig()[0])
    else:
        print('WLAN connection unsuccessful.')