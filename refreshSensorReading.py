#!/usr/bin/env python3
import sensorReading
import ev3


# constantly update left color reading values according to current mode
# run as daemon with main until quit
def refresh_colorsensor_reading_lt():
    while True:
      #update left color sensor readings according to current mode
      sensorReading.colorSensor_mode_lt = ev3.colorSensor_lt.mode
      if (ev3.colorSensor_lt.mode=="COL-REFLECT"):
           sensorReading.colorSensor_reflect_reading_lt=ev3.colorSensor_lt.value()
      elif ev3.colorSensor_lt.mode == "RGB-RAW":
           sensorReading.colorSensor_rawred_reading_lt=ev3.colorSensor_lt.red
           sensorReading.colorSensor_rawgreen_reading_lt=ev3.colorSensor_lt.green
           sensorReading.colorSensor_rawblue_reading_lt=ev3.colorSensor_lt.blue

def refresh_colorsensor_reading_rt():
    while True:
      #update left color sensor readings according to current mode
      sensorReading.colorSensor_mode_rt = ev3.colorSensor_rt.mode
      if (ev3.colorSensor_rt.mode =="COL-REFLECT"):
          sensorReading.colorSensor_reflect_reading_rt=ev3.colorSensor_rt.value()
      elif ev3.colorSensor_rt.mode == "RGB-RAW":
           sensorReading.colorSensor_rawred_reading_rt=ev3.colorSensor_rt.red
           sensorReading.colorSensor_rawgreen_reading_rt=ev3.colorSensor_rt.green
           sensorReading.colorSensor_rawblue_reading_rt=ev3.colorSensor_rt.blue




def refresh_ultrasonicSensorReading():
    while True:
      #update left color sensor readings according to current mode
      sensorReading.ultrasonicSensor_ReadingInCm=ev3.ultrasonicSensor.value()
