import RPi.GPIO as gpio

# This script will handle the execution of tasks from the interpreter.

def InitPump(pin):
  gpio.setmode(gpio.BCM)
  gpio.setup(pin, gpio.OUT)

def Flow(pin, status):
  if status:
    gpio.output(pin, 1) #no such function? fix this

  else:
    gpio.output(pin, 0) #no such function? fix this

  return True

def Finalize():
  gpio.cleanup()
