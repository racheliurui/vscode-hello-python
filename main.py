#!/usr/bin/env python3
'''
Main entrance to the logic
1) Read the config from Config.py
2) Initiate Sensor Reading from SensorReading.py
3) Keep updating the Sensor Reading
'''

from threading import Thread
import debug
import ggpub
import refreshSensorReading
import button
import vars



#https://sites.google.com/site/ev3devpython/learn_ev3_python/threads
def main():
   t1=Thread(target=refreshSensorReading.refresh_colorsensor_reading_lt,args=())
   t2=Thread(target=refreshSensorReading.refresh_colorsensor_reading_rt,args=())
   t3=Thread(target=refreshSensorReading.refresh_ultrasonicSensorReading,args=())
   t4=Thread(target=button.wait_buttonPressed,args=())
   t5=Thread(target=ggpub.publish,args=())
   t1.daemon=True
   t2.daemon=True
   t3.daemon=True
   t4.daemon=True
   t5.daemon=True
   t1.start()
   t2.start()
   t3.start()
   t4.start()
   t5.start()
   while not vars.buttonPressed :
       pass

if __name__ == '__main__':
    main()
