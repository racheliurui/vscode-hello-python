import SensorReading
import LargeMotor
import vars



baseSpeed=vars.maxspeed*vars.baseSpeedpercent

def updateBlackDepth():
    if(SensorReading.getColorReadingInString("left")=="black"):
         vars.left_black_depth=vars.left_black_depth+1
    elif (SensorReading.getColorReadingInString("right")=="black"):
         vars.right_black_depth=vars.right_black_depth+1
    else:
         vars.left_black_depth=0
         vars.right_black_depth=0

def followline():
   while vars.FollowTheLine:
       updateBlackDepth()
       vars.delta=(vars.left_black_depth-vars.right_black_depth)*baseSpeed/4
       LargeMotor.largeMotor_lt.run_forever(speed_sp=(baseSpeed-vars.delta))
       LargeMotor.largeMotor_rt.run_forever(speed_sp=(baseSpeed+vars.delta))
