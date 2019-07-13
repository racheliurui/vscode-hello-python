#!/usr/bin/env python3

# Read current sensor reading and publish
import sensorReading
import ggClient
import json
import time
import debug

def publish():
    while True:
      data = {}
      data['colorSensor_mode_lt'] = sensorReading.colorSensor_mode_lt
      data['colorSensor_mode_rt'] = sensorReading.colorSensor_mode_rt

      data['colorSensor_reflect_lt'] = sensorReading.colorSensor_reflect_lt
      data['colorSensor_reflect_rt'] = sensorReading.colorSensor_reflect_rt
      data['colorSensor_color_lt'] = sensorReading.colorSensor_color_lt
      data['colorSensor_color_rt'] = sensorReading.colorSensor_color_rt
      data['colorSensor_rawred_lt'] = sensorReading.colorSensor_rawred_lt
      data['colorSensor_rawgreen_lt'] = sensorReading.colorSensor_rawgreen_lt


      data['colorSensor_rawblue_lt'] = sensorReading.colorSensor_rawblue_lt
      data['colorSensor_rawred_rt'] = sensorReading.colorSensor_rawred_rt
      data['colorSensor_rawgreen_rt'] = sensorReading.colorSensor_rawgreen_rt
      data['colorSensor_rawblue_rt'] = sensorReading.colorSensor_rawblue_rt

      data['ultrasonicSensor_ReadingInCm'] = sensorReading.ultrasonicSensor_ReadingInCm

      #print("sensor reading published as  " + json.dumps(data) )
      debug.debug_print(json.dumps(data))
      time.sleep(0.1)
