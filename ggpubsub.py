import Config
import Debug
import json
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

def getGreenGrassMQTTClient():
    host = Config.host
    rootCAPath = Config.rootCAPath
    certificatePath = Config.certificatePath
    privateKeyPath = Config.privateKeyPath
    useWebsocket = Config.useWebsocket
    clientId = Config.clientId

    # Port defaults
    if useWebsocket:  # When no port override for WebSocket, default to 443
        port = 443
    if not useWebsocket:  # When no port override for non-WebSocket, default to 8883
        port = 8883

    # Init AWSIoTMQTTClient
    awsIoTMQTTClient = None
    if useWebsocket:
        awsIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
        awsIoTMQTTClient.configureEndpoint(host, port)
        awsIoTMQTTClient.configureCredentials(rootCAPath)
    else:
        awsIoTMQTTClient = AWSIoTMQTTClient(clientId)
        awsIoTMQTTClient.configureEndpoint(host, port)
        awsIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    # AWSIoTMQTTClient connection configuration
    awsIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    awsIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    awsIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    awsIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    awsIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    return awsIoTMQTTClient


def getDebugMsg():
    message = {}
    message['message'] = "hellow from EV3"
    messageJson = json.dumps(message)
    return messageJson


def publish(topic, messageJson):
    global ggClient
    if ggClient is None:
       ggClient = getGreenGrassMQTTClient()
    ggClient.publish(topic, messageJson, 1)
    Debug.debug_print('Published topic %s: %s\n' % (topic, messageJson))
