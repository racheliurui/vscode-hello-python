#!/usr/bin/env python3


# https://sites.google.com/site/ev3python/learn_ev3_python/using-sensors/sensor-modes


speedReading=0



# Color Sensor Readings
# COL-REFLECT COL-AMBIENT COL-COLOR RGB-RAW
colorSensor_mode_default = "COL-COLOR"
colorSensor_mode_lt = colorSensor_mode_default
colorSensor_mode_rt = colorSensor_mode_default
colorSensor_reflect_lt=0
colorSensor_reflect_rt=0
colorSensor_color_lt=0
colorSensor_color_rt=0

colorSensor_rawred_lt=0
colorSensor_rawgreen_lt=0
colorSensor_rawblue_lt=0

colorSensor_rawred_rt=0
colorSensor_rawgreen_rt=0
colorSensor_rawblue_rt=0

ultrasonicSensor_ReadingInCm=0
