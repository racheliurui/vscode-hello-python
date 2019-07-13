#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
import sensorReading

# initiate color sensors
colorSensor_lt = ColorSensor(INPUT_3)
colorSensor_rt = ColorSensor(INPUT_1)
colorSensor_lt.mode=sensorReading.colorSensor_mode_default
colorSensor_rt.mode=sensorReading.colorSensor_mode_default

ultrasonicSensor = UltrasonicSensor(INPUT_2)

# initiate all motors
largeMotor_lt = LargeMotor(OUTPUT_A)
largeMotor_rt = LargeMotor(OUTPUT_D)


