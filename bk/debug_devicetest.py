#!/usr/bin/env python3
import debug
import ev3
import timeit



#######################
#  Conclusion, the sensor reading can be directly read from sensor, no need multi-thread.
######################

#Time:  55.147123357000055
# without print, total time is 0.158 sec
def test_comparison():
    i =0
    start = timeit.default_timer()
    while i<10000 :
       i=i+1
       #debug.debug_print("1")
    stop = timeit.default_timer()
    debug.debug_print('Time: ', stop - start)

# color sensor reading took 75 second for 10000 readings.
# without debug print, Time:  0.17401769299976877
def test_ColorSensorSpeed():
    i =0
    start = timeit.default_timer()
    while i<10000 :
       i=i+1
       #debug.debug_print(str(ev3.colorSensor_lt.value()))
    stop = timeit.default_timer()
    debug.debug_print('Time: ', stop - start)

