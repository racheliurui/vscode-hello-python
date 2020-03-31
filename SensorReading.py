#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.power import PowerSupply

# initiate color sensors
# the colour sensor needs to be between 1-2 cm away from the surface you are trying to measure. (color mode)
# TODO confirm the mapping
colorSensor_lt = ColorSensor(INPUT_4)
colorSensor_rt = ColorSensor(INPUT_1)
ultrasonicSensor = UltrasonicSensor(INPUT_2)

# COL-REFLECT COL-AMBIENT COL-COLOR RGB-RAW
colorSensor_mode_default = "COL-COLOR"
colorSensor_lt.mode="COL-COLOR"
colorSensor_rt.mode="COL-COLOR"
ultrasonicSensor.mode="US-DIST-CM"

powerSupply = PowerSupply()

def getColorString(color_reading):
    if(color_reading==1):
       return "black"
    elif(color_reading==2):
       #return "blue"
       return "white"
    elif(color_reading==3):
       return "green"
    elif(color_reading==4):
       #return "yellow"
       return "white"
    elif(color_reading==5):
       return "red"
    elif(color_reading==6):
       return "white"
    elif(color_reading==7):
       return "brown"
    return str(color_reading)

def getColorReadingInString(sensor_positon):
    if(sensor_positon=="left"):
       return getColorString(colorSensor_lt.value())
    if(sensor_positon=="right"):
       return getColorString(colorSensor_rt.value())


