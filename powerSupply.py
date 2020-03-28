#!/usr/bin/env python3

from ev3dev2.power import PowerSupply

def getPowerSupplyReading():
    return PowerSupply.measured_volts
