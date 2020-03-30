import sys
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import time
import vars

## Load Global Config
import config as config
rootCAPath= config.IoT["rootCAPath"]
certificatePath = config.IoT["certificatePath"]
privateKeyPath = config.IoT["privateKeyPath"]
endPoint = config.IoT["endPoint"]
clientId = config.IoT["clientId"]
useWebsocket = config.IoT["useWebsocket"]
QoS = config.IoT["QoS"]


def dummy_getAWSIoTCoreMQTTClient(rootCAPath,certificatePath,privateKeyPath,endPoint,clientId,useWebsocket):
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
    #client.configureConnectDisconnectTimeout(10)  # 10 sec
    #client.configureMQTTOperationTimeout(20)  # 5 sec
    return client



def dummy_publishEV3Status(mqttClient,topic):
    QoS=1
    data = {}
    # add more data points here to publish together
    data['measured_volts'] = 7.069066
    messageJson = json.dumps(data)
    #At most once (0) At least once (1)
    mqttClient.publish(topic, messageJson, QoS)
    print("message payload published with QoS " + str(QoS) + " to " + topic + ", with payload: " + json.dumps(data))
    #throttle
    #time.sleep(1)


def debugPublish():
    mqttClient=dummy_getAWSIoTCoreMQTTClient(rootCAPath,certificatePath,privateKeyPath,endPoint,clientId,useWebsocket)
    mqttClient.connect()
    loop=0
    while loop<5:
        try:
            dummy_publishEV3Status(mqttClient,"topic_1")
            print(loop)
            loop = loop +1
        except:
           print("error happened while publishing")
    print("published " + str(loop) + " mqtt messages" )
    mqttClient.disconnect()

def msgCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")

def cmdCallback(client, userdata, message):
    print("Received a new message: ")
    message.payload = message.payload.decode("utf-8")
    print(message.payload)
    if message.payload == "stop":
       vars.buttonPressed=True
    print("--------------\n\n")


mqttClient=dummy_getAWSIoTCoreMQTTClient(rootCAPath,certificatePath,privateKeyPath,endPoint,clientId,useWebsocket)
mqttClient.connect()
mqttClient.subscribe("topic_1", 1, msgCallback)
mqttClient.subscribe("topic_2", 1, cmdCallback)


while not vars.buttonPressed:
       time.sleep(2)
       dummy_publishEV3Status(mqttClient,"topic_1")



