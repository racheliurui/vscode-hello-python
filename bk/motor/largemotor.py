
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,SpeedPercent
from ev3dev2.motor import MoveTank
import datetime


def runlargemoto(output):

    # run large moto
    lm = LargeMotor(address=output)
    lm.on_for_rotations(SpeedPercent(75), 1)

def timebasedSlowdon():
    datetime.datetime.now()

def goforward(leftengine, rightengine):

     # go forward
     tank_drive = MoveTank(leftengine, rightengine)

     # drive in a turn for 5 rotations of the outer motor
     # the first two parameters can be unit classes or percentages.
     #tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(15), 5)

     # drive in a different turn for 3 seconds
     tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(10), 3)
