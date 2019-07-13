#!/usr/bin/env python3
import sys
from ev3dev2.sound import Sound
sound = Sound()

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

def speakout(message):
    sound.speak(message)

