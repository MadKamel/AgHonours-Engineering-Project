import RPi.GPIO as gpio

# This script will handle the execution of tasks from the interpreter.

def InitPump(pin, pin2):
  gpio.setmode(gpio.BCM)
  gpio.setup(pin, gpio.OUT)
  gpio.setup(pin2, gpio.OUT)

def Flow(pin, pin2, status):
  if status:
    gpio.output(pin, 1) #no such function? fix this
    gpio.output(pin2, 1)
  else:
    gpio.output(pin, 0) #no such function? fix this
    gpio.output(pin2, 0)
  return True

def Finalize():
  gpio.cleanup()
