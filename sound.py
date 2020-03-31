#!/usr/bin/env python3
from ev3dev2.sound import Sound
sound = Sound()


def speakout(message):
    sound.speak(message)

