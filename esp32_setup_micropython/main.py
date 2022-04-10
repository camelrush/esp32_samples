from machine import PWM,Pin
import time

LED = Pin(32, Pin.OUT)

while True:
    LED.on()
    time.sleep(1)
    LED.off()
    time.sleep(1)
