#!/usr/bin/env python3
'''Hello to the world from ev3dev.org'''

import os
import sys
import _thread
import Debug

from greengrass.pubsub import publish

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
from motor.largemotor import goforward


def main():
   Debug.debug_print(sys.path)
   _thread.start_new_thread(publish,())
   goforward(OUTPUT_A,OUTPUT_D)

if __name__ == '__main__':
    main()
