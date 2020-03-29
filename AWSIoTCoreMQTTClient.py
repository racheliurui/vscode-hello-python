
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient



def getAWSIoTCoreMQTTClient(rootCAPath,certificatePath,privateKeyPath,endPoint,clientId,useWebsocket):
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
    return client
