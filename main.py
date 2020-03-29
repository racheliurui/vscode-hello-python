#!/usr/bin/env python3

from threading import Thread
import os
import sys
import time
import debug
import AWSIoTCoreMQTTClient
import EV3MQTTPublisher

## Load Global Config
import config as config
rootCAPath= config.IoT["rootCAPath"]
certificatePath = config.IoT["certificatePath"]
privateKeyPath = config.IoT["privateKeyPath"]
endPoint = config.IoT["endPoint"]
clientId = config.IoT["clientId"]
useWebsocket = config.IoT["useWebsocket"]
QoS = config.IoT["QoS"]


#https://sites.google.com/site/ev3devpython/learn_ev3_python/threads
def main():
    t1=Thread(target=mainPublisher,args=())
    t1.daemon=True
    t1.start()

    debug_makeSomeSound()


def mainPublisher():
   mqttClient=AWSIoTCoreMQTTClient.getAWSIoTCoreMQTTClient(rootCAPath,certificatePath,privateKeyPath,endPoint,clientId,useWebsocket)
   mqttClient.connect()
   loop=0
   while loop<30:
     try:
       EV3MQTTPublisher.publishEV3Status(mqttClient,"topic_1",QoS)
     except:
       print("error happened while publishing")
     debug.debug_print(loop)
     loop = loop +1

   debug.debug_print("published " + str(loop) + " mqtt messages" )
   mqttClient.disconnect()

def debug_makeSomeSound():
    from ev3dev2.sound import Sound
    sound = Sound()
    sound.speak("hello")


if __name__ == '__main__':
    main()
