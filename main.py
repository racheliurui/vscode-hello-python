#!/usr/bin/env python3

import AWSIoTCoreMQTTClient
import sound



#https://sites.google.com/site/ev3devpython/learn_ev3_python/threads
def main():
    sound.speakout("mission started, I will keep you posted")
    AWSIoTCoreMQTTClient.startPubSub()

    AWSIoTCoreMQTTClient.mqttClient.disconnect()
    sound.speakout("mission completed")


if __name__ == '__main__':
    main()
