#!/usr/bin/env python3
# AWS IoT Core MQTT Client Config
'''
rootCAPath= "downloads/root-CA.crt"
certificatePath = "downloads/EV3Lego1.cert.pem"
privateKeyPath = "downloads/EV3Lego1.private.key"
endPoint = "a2rizlo4ii9h59-ats.iot.ap-southeast-2.amazonaws.com"
clientId = "EV3Lego1"
useWebsocket = False
'''

from threading import Thread
import os
import sys
import time
import debug
import AWSIoTCoreMQTTClient
import EV3MQTTPublisher

#https://sites.google.com/site/ev3devpython/learn_ev3_python/threads
def main():
    t1=Thread(target=mainPublisher,args=())
    t1.daemon=True
    t1.start()

    debug_makeSomeSound()


def mainPublisher():
   rootCAPath= "downloads/root-CA.crt"
   certificatePath = "downloads/EV3Lego1.cert.pem"
   privateKeyPath = "downloads/EV3Lego1.private.key"
   endPoint = "a2rizlo4ii9h59-ats.iot.ap-southeast-2.amazonaws.com"
   clientId = "EV3Lego1"
   useWebsocket = False
   mqttClient=AWSIoTCoreMQTTClient.getAWSIoTCoreMQTTClient(rootCAPath,certificatePath,privateKeyPath,endPoint,clientId,useWebsocket)
   loop=0
   while loop<1000:
     EV3MQTTPublisher.publishEV3Status(mqttClient,"topic_1")
     loop = loop +1
   debug.debug_print("published " + str(loop) + " mqtt messages" )

def debug_makeSomeSound():
    from ev3dev2.sound import Sound
    sound = Sound()
    sound.speak("hello")


if __name__ == '__main__':
    main()
