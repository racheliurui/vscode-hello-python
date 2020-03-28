#!/usr/bin/env python3

import ggClient
import json
import time
import debug
from ev3dev2.power import PowerSupply

powerSupply= PowerSupply()

def publishVoltage(mqttClient,topic):
     while True:
        data = {}
        data['measured_volts'] = powerSupply.measured_volts
        #print("sensor reading published as  " + json.dumps(data) )
        debug.debug_print(json.dumps(data))
        messageJson = json.dumps(data)
        mqttClient.publish(topic, messageJson, 1)
        time.sleep(1)

