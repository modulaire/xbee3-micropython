from machine import PWM
from time import sleep

pwm0 = PWM('P0')   # create PWM object from a pin
myDelay = 0.0005
print("code starts here")

while True:
  for duty_cycle in range(0,1023):
    pwm0.duty(duty_cycle)
    sleep(myDelay)
  for duty_cycle in range(1023,0,-1):
    pwm0.duty(duty_cycle)
    sleep(myDelay)
