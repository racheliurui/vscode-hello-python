#!/usr/bin/env python3
'''
Main entrance to the logic
1) Read the config from Config.py
2) Initiate Sensor Reading from SensorReading.py
3) Keep updating the Sensor Reading
'''

from threading import Thread
import powerSupply
import os
import sys
import time
from ev3dev2.sound import Sound
from ev3dev2.power import PowerSupply
import ggClient
import ggpub
sound = Sound()
powerSupply= PowerSupply()
mqttClient=ggClient.getnewclient()

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


#https://sites.google.com/site/ev3devpython/learn_ev3_python/threads
def main():

    t1=Thread(target=ggpub.publishVoltage,args=(mqttClient,"topic_1"))
    t1.daemon=True
    t1.start()
    debug_print("================???==========="+str(powerSupply.measured_volts))
    debug_makeSomeSound()



def debug_getreading():
   debug_print(powerSupply.measured_volts)

def debug_makeSomeSound():
    sound.speak("hello")


if __name__ == '__main__':
    main()
