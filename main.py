from wireless import Wireless
import os
import time
# By Thomas McLaughlin and Roman Morasco

def connectEspKey():
    hostname = "google.com" #TOBE 192.168.4.1
    isConnected = False
    while isConnected is False:
        time.sleep(15)
        wire = Wireless()
        wire.connect(ssid = 'namewifi', password = 'passwrd')
        time.sleep(5)
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            isConnected = True
    print("Connection Established")

def connectInternet():
    hostname = "google.com"
    isConnected = False
    while isConnected is False:
        time.sleep(15)
        wire = Wireless()
        wire.connect(ssid = 'namewifi', password = 'passwrd')
        time.sleep(5)
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            isConnected = True
    print("Connection Established")   


def main():
    time.sleep(0)# increase to around 30 to allow computer to start up
    print("STARTING INITIAL CONNECTION")
    connectEspKey()
    print("STARTING SECOND CONNECTION")
    connectInternet()

  
if __name__=="__main__":
    main()