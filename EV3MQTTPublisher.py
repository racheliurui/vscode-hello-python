
import json
import debug
import time
from ev3dev2.power import PowerSupply

powerSupply = PowerSupply()

def publishEV3Status(mqttClient,topic,QoS):
    QoS=0
    data = {}
    # add more data points here to publish together
    data['measured_volts'] = powerSupply.measured_volts

    messageJson = json.dumps(data)
    #At most once (0) At least once (1)
    mqttClient.publish(topic, messageJson, QoS)
    debug.debug_print("message payload published with QoS " + str(QoS) + " to topic " + topic + ", with payload: " + json.dumps(data))
    #throttle
    #time.sleep(1)

