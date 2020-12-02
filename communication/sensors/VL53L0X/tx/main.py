import xbee
from machine import I2C
from VL53L0X import VL53L0X
from time import sleep

# Replace the address with your xbee target address
TARGET_64BIT_ADDR = b'\x00\x13\xA2\x00\x41\xB4\xCA\x95'

i2c = I2C(1, freq=400000)
sensor = VL53L0X(i2c=1)

while True:
    distance = sensor.read()
    print(distance)
    sleep(.01)
    data = str(distance)
    try:
        xbee.transmit(TARGET_64BIT_ADDR, data)
        print("\nData sent successfully")
    except Exception as e:
        print("\nTransmit failure: %s" % str(e))

