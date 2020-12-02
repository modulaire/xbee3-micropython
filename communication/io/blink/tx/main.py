import xbee
from time import sleep

# Replace the address with your xbee target address
TARGET_64BIT_ADDR = b'\x00\x13\xA2\x00\x41\xB9\xF8\x9B'
MESSAGE = "ON"

while True:
    if MESSAGE == "ON":
        MESSAGE = "OFF"
    elif MESSAGE == "OFF":
        MESSAGE = "ON"
    sleep(.6)

    try:
        xbee.transmit(TARGET_64BIT_ADDR, MESSAGE)
        print("\nData sent successfully")
    except Exception as e:
        print("\nTransmit failure: %s" % str(e))

