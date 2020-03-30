#!/usr/bin/env python3

from threading import Thread
import os
import sys
import time
from ev3dev2.sound import Sound
import AWSIoTCoreMQTTClient


import EV3MQTTPublisher
import vars
import debug

sound = Sound()
## Load Global Config
import config as config
rootCAPath= config.IoT["rootCAPath"]
certificatePath = config.IoT["certificatePath"]
privateKeyPath = config.IoT["privateKeyPath"]
endPoint = config.IoT["endPoint"]
clientId = config.IoT["clientId"]
useWebsocket = config.IoT["useWebsocket"]
QoS = config.IoT["QoS"]


def commandCallback(client, userdata, message):
    debug.debug_print("Received a new message: ")
    message.payload = message.payload.decode("utf-8")
    debug.debug_print(message.payload)
    sound.speak("I have received to command to " + message.payload)
    if message.payload == "stop":
       vars.keepRunning=False
    debug.debug_print("--------------\n\n")

#https://sites.google.com/site/ev3devpython/learn_ev3_python/threads
def main():
    sound.speak("mission started, I will keep you posted")
    mqttClient=AWSIoTCoreMQTTClient.getAWSIoTCoreMQTTClient(rootCAPath,certificatePath,privateKeyPath,endPoint,clientId,useWebsocket)
    mqttClient.connect()
    # Run subscriber
    mqttClient.subscribe("command", 1, commandCallback)

    # Run publisher
    while vars.keepRunning:
     try:
       EV3MQTTPublisher.publishEV3Status(mqttClient,"topic_1",QoS)
       time.sleep(2)
     except:
       debug.debug_print("error happened while publishing")

    mqttClient.disconnect()
    debug_makeSomeSound()


def debug_makeSomeSound():
    sound.speak("mission completed")


if __name__ == '__main__':
    main()
