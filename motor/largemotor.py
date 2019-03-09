
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedRPM, SpeedRPS, SpeedDPM,SpeedPercent


def runlargemoto(output):

    # run large moto
    lm = LargeMotor(address=output)
    lm.on_for_rotations(SpeedPercent(75), 1)
