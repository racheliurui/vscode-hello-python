#!/usr/bin/env python3

# Read current sensor reading and publish
#import sensorReading
import ev3
import ggClient
import json
import time
import debug
import checkColor
import sound

def publish():
    while True:
        data = {}

        #COL-REFLECT COL-AMBIENT COL-COLOR RGB-RAW
        data['colorSensor_mode_lt'] = ev3.colorSensor_lt.mode
        data['colorSensor_mode_rt'] = ev3.colorSensor_rt.mode
        if data['colorSensor_mode_lt']=="COL-COLOR":
             data['colorSensor_color_reading_lt'] = ev3.colorSensor_lt.value()
             data['colorSensor_color_reading_lt_string'] = checkColor.getColorString(data['colorSensor_color_reading_lt'])

        if data['colorSensor_mode_rt']=="COL-COLOR":
             data['colorSensor_color_reading_rt'] = ev3.colorSensor_rt.value()
             data['colorSensor_color_reading_rt_string'] = checkColor.getColorString(data['colorSensor_color_reading_rt'])

        data['ultrasonicSensor_ReadingInCm'] = ev3.ultrasonicSensor.value()

        #print("sensor reading published as  " + json.dumps(data) )
        debug.debug_print(json.dumps(data))
        #time.sleep(0.1)
        time.sleep(1)
