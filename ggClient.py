#!/usr/bin/env python3
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# AWS Greengrass Config
host = "a1afr0tqzp932s-ats.iot.ap-southeast-2.amazonaws.com"
rootCAPath = "downloads/root-CA.crt"
certificatePath = "downloads/testtest.cert.pem"
privateKeyPath = "downloads/testtest.private.key"
useWebsocket = False
clientId = "basicPubSub"
topic = "sdk/test/Python"
mode = 'publish'


def getnewclient():
    # Port defaults
    if useWebsocket:  # When no port override for WebSocket, default to 443
        port = 443
    if not useWebsocket:  # When no port override for non-WebSocket, default to 8883
        port = 8883

    if useWebsocket:
        client = AWSIoTMQTTClient(clientId, useWebsocket=True)
        client.configureEndpoint(host, port)
        client.configureCredentials(rootCAPath)
    else:
        client = AWSIoTMQTTClient(clientId)
        client.configureEndpoint(host, port)
        client.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    # config.ggClient connection configuration
    #http://www.bitreactive.com/blog/2015/06/26/how-fast-can-you-publish-mqtt-messages/
    client.configureAutoReconnectBackoffTime(1, 32, 20)
    client.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    client.configureDrainingFrequency(2)  # Draining: 2 Hz
    client.configureConnectDisconnectTimeout(10)  # 10 sec
    client.configureMQTTOperationTimeout(5)  # 5 sec
    return client


def refresh_ggclient():
    global ggClient
    ggClient=getnewclient()


ggClient = getnewclient()
