from machine import I2C
from VL53L0X import VL53L0X
from time import sleep

i2c = I2C(1, freq=400000)
sensor = VL53L0X(i2c=1)

while True:
    distance = sensor.read()
    print(distance)
    sleep(.01)
