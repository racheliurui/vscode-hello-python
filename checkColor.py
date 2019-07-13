#!/usr/bin/env python3
import sensorReading

def getColorString(color_reading):
    if(color_reading==1):
       return "black"
    elif(color_reading==2):
       return "blue"
    elif(color_reading==3):
       return "green"
    elif(color_reading==4):
       return "yellow"
    elif(color_reading==5):
       return "red"
    elif(color_reading==6):
       return "white"
    elif(color_reading==7):
       return "brown"

