#!/usr/bin/env python3
'''
Main entrance to the logic
1) Read the config from Config.py
2) Initiate Sensor Reading from SensorReading.py
3) Keep updating the Sensor Reading
'''

import os
import sys
from threading import Thread
import Debug
import ggpubsub
import SensorReading
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from motor.largemotor import goforward

global Readings
Readings=None


#https://sites.google.com/site/ev3devpython/learn_ev3_python/threads
def main():
   Debug.debug_print(sys.path)
   Thread(target=ggpubsub.publish,args=())
   goforward(OUTPUT_A,OUTPUT_D)

if __name__ == '__main__':
    main()
