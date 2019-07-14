#!/usr/bin/env python3
import ev3
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,SpeedPercent
from ev3dev2.motor import MoveTank


def goforward(seconds):
     tank_drive = MoveTank(ev3.largeMotor_port_lt, ev3.largeMotor_port_rt)
     tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(10), seconds)
