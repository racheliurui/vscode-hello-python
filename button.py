#!/usr/bin/env python3
import vars
def wait_buttonPressed():
    while True:
       i = input("Enter text (or Enter to quit): ")
       if not i:
          break
    print("Your input:", i)
    vars.buttonPressed=True
    print("While loop has exited")
