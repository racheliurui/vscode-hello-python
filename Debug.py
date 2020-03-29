#!/usr/bin/env python3
import sys
import config as config

debugToConsole= config.debugToConsole

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    if(debugToConsole):
       print(*args, **kwargs, file=sys.stderr)
