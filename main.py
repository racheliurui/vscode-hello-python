#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
sys.path.append('/usr/local/lib/python2.7/dist-packages/AWSIoTPythonSDK')
import AWSIoTPythonSDK

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from motor.largemotor import goforward




def main():
   print( sys.modules['AWSIoTPythonSDK'])
   goforward(OUTPUT_A,OUTPUT_D)

if __name__ == '__main__':
    main()
