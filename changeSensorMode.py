#!/usr/bin/env python3
import sensorReading
import ev3



# Set and update color sensor mode
def changeColorSensorMode(sensorLocation, mode):
    if sensorLocation == "left":
        ev3.colorSensor_lt.mode=mode
    if sensorLocation == "right":
        ev3.colorSensor_rt.mode=mode
    if sensorLocation == "both":
        ev3.colorSensor_lt.mode=mode
        ev3.colorSensor_rt.mode=mode


#https://python-ev3dev.readthedocs.io/en/ev3dev-stretch/sensors.html#ev3dev2.sensor.lego.ColorSensor.calibrate_white
def changeUltraSonicSensorMode(mode):
    ev3.ultrasonicSensor.mode=mode

