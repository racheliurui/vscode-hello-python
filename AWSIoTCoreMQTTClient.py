from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
from datetime import datetime

import config
import debug
import SensorReading
import vars
import sound
import followline


rootCAPath= config.IoT["rootCAPath"]
certificatePath = config.IoT["certificatePath"]
privateKeyPath = config.IoT["privateKeyPath"]
endPoint = config.IoT["endPoint"]
clientId = config.IoT["clientId"]
useWebsocket = config.IoT["useWebsocket"]
QoS = config.IoT["QoS"]



def initAWSIoTCoreMQTTClient():

    # Port defaults
    if useWebsocket:  # When no port override for WebSocket, default to 443
        port = 443
    if not useWebsocket:  # When no port override for non-WebSocket, default to 8883
        port = 8883

    if useWebsocket:
        client = AWSIoTMQTTClient(clientId, useWebsocket)
        client.configureEndpoint(endPoint, port)
        client.configureCredentials(rootCAPath, KeyPath=privateKeyPath, CertificatePath=certificatePath)
    else:
        client = AWSIoTMQTTClient(clientId)
        client.configureEndpoint(endPoint, port)
        client.configureCredentials(rootCAPath, KeyPath=privateKeyPath, CertificatePath=certificatePath)

    # config.ggClient connection configuration
    #http://www.bitreactive.com/blog/2015/06/26/how-fast-can-you-publish-mqtt-messages/
    client.configureAutoReconnectBackoffTime(1, 32, 20)
    client.configureOfflinePublishQueueing(1000)  # Infinite offline Publish queueing
    client.configureDrainingFrequency(2)  # Draining: 2 Hz
    client.configureConnectDisconnectTimeout(10)  # 10 sec
    client.configureMQTTOperationTimeout(20)  # 5 sec
    client.connect()
    return client


def publishEV3Status(mqttClient,topic,QoS):
    data = {}
    # add more data points here to publish together
    data['measured_volts'] = SensorReading.powerSupply.measured_volts
    data['left_color'] = SensorReading.getColorReadingInString("left")
    data['right_color'] = SensorReading.getColorReadingInString("right")
    if(vars.FollowTheLine):
        data['delta'] = vars.delta
    if(vars.messagesPerSecond>0):
        data['messagesPerSecond'] = vars.messagesPerSecond
    messageJson = json.dumps(data)
    #At most once (0) At least once (1)
    mqttClient.publish(topic, messageJson, QoS)
    debug.debug_print("message payload published with QoS " + str(QoS) + " to topic " + topic + ", with payload: " + json.dumps(data))
    #throttle
    #time.sleep(1)

def publishIoT(mqttClient,topic,QoS):
    # Run publisher
    start=datetime.now()
    numOfPublishedMQTTMessage=0
    while vars.PublishingIoT:
       try:
           publishEV3Status(mqttClient,topic,QoS)
           numOfPublishedMQTTMessage=numOfPublishedMQTTMessage+1
           vars.messagesPerSecond=0
           if(numOfPublishedMQTTMessage>=vars.msgRateEvaluateBatch):
              total_seconds=(datetime.now()-start).total_seconds()
              vars.messagesPerSecond=vars.msgRateEvaluateBatch/total_seconds
              numOfPublishedMQTTMessage=0
       except Exception as e:
           debug.debug_print("publishIoT"+e)

def commandCallback(client, userdata, message):
    debug.debug_print("Received a new command: ")
    message.payload = message.payload.decode("utf-8")
    debug.debug_print(message.payload)
    sound.speakout("I have received to command to " + message.payload)
    if message.payload == "stop":
       vars.PublishingIoT=False
       vars.FollowTheLine=False
    if message.payload == "follow the line":
       vars.FollowTheLine=True
       followline.followline()
    debug.debug_print("--------------\n\n")


def startPubSub():
    mqttClient=initAWSIoTCoreMQTTClient()

    # Run subscriber
    mqttClient.subscribe("command/"+clientId, 1, commandCallback)
    publishIoT(mqttClient,"data/"+clientId,QoS)
