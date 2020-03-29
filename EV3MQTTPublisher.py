
import json
import debug
from ev3dev2.power import PowerSupply

powerSupply = PowerSupply()

def publishEV3Status(mqttClient,topic):
    data = {}
    # add more data points here to publish together
    data['measured_volts'] = powerSupply.measured_volts

    debug.debug_print(json.dumps(data))
    messageJson = json.dumps(data)
    mqttClient.publish(topic, messageJson, 1)

