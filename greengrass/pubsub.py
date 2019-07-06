import os
import sys
from downloads.AWSIoTPythonSDK import AWSIoTMQTTClient
import logging
import time
import argparse
import json



def publish():
    host = "a1afr0tqzp932s-ats.iot.ap-southeast-2.amazonaws.com"
    rootCAPath = "downloads/root-CA.crt"
    certificatePath = "downloads/testtest.cert.pem"
    privateKeyPath = "downloads/testtest.private.key"
    useWebsocket = False
    clientId = "basicPubSub"
    topic = "sdk/test/Python"
    mode = 'publish'


    # Port defaults
    if useWebsocket:  # When no port override for WebSocket, default to 443
        port = 443
    if not useWebsocket:  # When no port override for non-WebSocket, default to 8883
        port = 8883


    # Init AWSIoTMQTTClient
    myAWSIoTMQTTClient = None
    if useWebsocket:
        myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId, useWebsocket=True)
        myAWSIoTMQTTClient.configureEndpoint(host, port)
        myAWSIoTMQTTClient.configureCredentials(rootCAPath)
    else:
        myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
        myAWSIoTMQTTClient.configureEndpoint(host, port)
        myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

    # AWSIoTMQTTClient connection configuration
    myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
    myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
    myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
    myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
    myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

    # Publish to the same topic in a loop forever
    loopCount = 0
    while True:
        if mode == 'both' or mode == 'publish':
            message = {}
            message['message'] = "hellow from EV3"
            message['sequence'] = loopCount
            messageJson = json.dumps(message)
            myAWSIoTMQTTClient.publish(topic, messageJson, 1)
            if mode == 'publish':
                print('Published topic %s: %s\n' % (topic, messageJson))
            loopCount += 1
        time.sleep(1)
