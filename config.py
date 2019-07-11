#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4

# AWS Greengrass Config
host = "a1afr0tqzp932s-ats.iot.ap-southeast-2.amazonaws.com"
rootCAPath = "downloads/root-CA.crt"
certificatePath = "downloads/testtest.cert.pem"
privateKeyPath = "downloads/testtest.private.key"
useWebsocket = False
clientId = "basicPubSub"
topic = "sdk/test/Python"
mode = 'publish'
ggClient = None


# Port mapping
ColorSensor_Port_LT=INPUT_1
ColorSensor_Port_RT=INPUT_2
UltrasonicSensor_Port=INPUT_3
