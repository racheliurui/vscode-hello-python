#!/usr/bin/env python3

from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
import Config

speedReading=0

# Color Sensor Readings
colorSensor_reflect_reading_lt=0
colorSensor_reflect_reading_rt=0

colorSensor_rawred_reading_lt=0
colorSensor_rawgreen_reading_lt=0
colorSensor_rawblue_reading_lt=0

colorSensor_rawred_reading_rt=0
colorSensor_rawgreen_reading_rt=0
colorSensor_rawblue_reading_rt=0

# Color Sensor Modes
colorSensor_mode_lt='COL-REFLECT'
colorSensor_mode_rt='COL-REFLECT'

ultrasonicSensor_ReadingInCm=0

# initiate all the sensors
colorSensor_lt = ColorSensor(Config.ColorSensor_Port_LT)
colorSensor_rt = ColorSensor(Config.ColorSensor_Port_RT)
ultrasonicSensor = UltrasonicSensor(Config.UltrasonicSensor_Port)


# According to current color sensor mode, update corresponding reading
def updateColorSensorReading(sensorLocation):
    global colorSensor_mode_lt
    global colorSensor_reflect_reading_lt
    global colorSensor_mode_rt
    global colorSensor_reflect_reading_rt
    global colorSensor_lt
    global colorSensor_rt
    global colorSensor_rawred_reading_lt
    global colorSensor_rawgreen_reading_lt
    global colorSensor_rawblue_reading_lt
    global colorSensor_rawred_reading_rt
    global colorSensor_rawgreen_reading_rt
    global colorSensor_rawblue_reading_rt

    if sensorLocation == "left":
        if colorSensor_mode_lt == "COL-REFLECT":
           colorSensor_reflect_reading_lt=colorSensor_lt.value()
        elif colorSensor_mode_lt == "RGB-RAW":
           colorSensor_rawred_reading_lt=colorSensor_lt.red
           colorSensor_rawgreen_reading_lt=colorSensor_lt.green
           colorSensor_rawblue_reading_lt=colorSensor_lt.blue

    if sensorLocation == "right":
        if colorSensor_mode_rt == "COL-REFLECT":
           colorSensor_reflect_reading_rt=colorSensor_rt.value()
        elif colorSensor_mode_rt == "RGB-RAW":
           colorSensor_rawred_reading_rt=colorSensor_rt.red
           colorSensor_rawgreen_reading_rt=colorSensor_rt.green
           colorSensor_rawblue_reading_rt=colorSensor_rt.blue

    if sensorLocation == "both":
        if colorSensor_mode_lt == "COL-REFLECT":
           colorSensor_reflect_reading_lt=colorSensor_lt.value()
        elif colorSensor_mode_lt == "RGB-RAW":
           colorSensor_rawred_reading_lt=colorSensor_lt.red
           colorSensor_rawgreen_reading_lt=colorSensor_lt.green
           colorSensor_rawblue_reading_lt=colorSensor_lt.blue

        if colorSensor_mode_rt == "COL-REFLECT":
           colorSensor_reflect_reading_rt=colorSensor_rt.value()
        elif colorSensor_mode_rt == "RGB-RAW":
           colorSensor_rawred_reading_rt=colorSensor_rt.red
           colorSensor_rawgreen_reading_rt=colorSensor_rt.green
           colorSensor_rawblue_reading_rt=colorSensor_rt.blue

# Set and update color sensor mode
def changeColorSensorMode(sensorLocation, mode):
    global colorSensor_mode_lt
    global colorSensor_mode_rt
    global colorSensor_lt
    global colorSensor_rt
    if sensorLocation == "left":
        colorSensor_lt.mode=mode
        colorSensor_mode_lt=mode
    if sensorLocation == "right":
        colorSensor_rt.mode=mode
        colorSensor_mode_rt=mode
    if sensorLocation == "both":
        colorSensor_lt.mode=mode
        colorSensor_mode_lt=mode
        colorSensor_rt.mode=mode
        colorSensor_mode_rt=mode

#https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/sensors.html#ev3dev2.sensor.lego.ColorSensor.calibrate_white
def updateUltraSonicSensorMode(mode):
    global ultrasonicSensor
    ultrasonicSensor.mode=mode


def updateUltrasonicSensorReading():
    global ultrasonicSensor_ReadingInCm
    ultrasonicSensor_ReadingInCm=ultrasonicSensor.value()
