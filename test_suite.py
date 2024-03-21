import time
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import grovepi


#using physical pin 11 to blink an LED
GPIO.setmode(GPIO.BOARD)
chan_list = [11]
GPIO.setup(chan_list, GPIO.OUT)
#Following commands control the state of the output
#GPIO.output(pin, GPIO.HIGH)
#GPIO.output(pin, GPIO.LOW)
light_thresh = 300
sound_thresh = 10


# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
# get reading from adc 
# mcp.read_adc(adc_channel)

while True: 
  time.sleep(0.5) 

  #test 1
  for i in range(0,4):
    print('led 4 times');
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(0.5)

  #test 2
  end = time.time() + 5
  while time.time() < end:
    time.sleep(0.1)
    light_val = mcp.read_adc(0)
    time.sleep(0.1)
    print(light_val)
    if light_val > light_thresh:
      print("Bright")
    else:
      print("Dark")
  
  
  #test3
  for i in range(0,10):
    print('led 10 times')
    GPIO.output(chan_list, GPIO.HIGH)
    time.sleep(0.2)
    GPIO.output(chan_list, GPIO.LOW)
    time.sleep(0.2)

  #test 4: 
  end = time.time() + 5
  while time.time() < end:
    time.sleep(0.1)
    sound_val = mcp.read_adc(1)
    print(sound_val)
    if sound_val > sound_thresh:
      GPIO.output(chan_list, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(chan_list, GPIO.LOW)
    else:
      GPIO.output(chan_list, GPIO.LOW)
      time.sleep(0.1)


  
  