#!/usr/bin/env python3
from ev3dev2.sound import Sound
import time
sound = Sound()

message=None

def debug_makeSomeSound():
    global message
    global sound
    while True:
      if (not message is None):
           sound.speak(message)
           time.sleep(1)
           message=None

def speak(message):
    sound.speak(message)

