import xbee
import time
from machine import Pin

LED_PIN_ID = "D9"

led_pin = Pin(LED_PIN_ID, Pin.OUT, value=0)

# Blink LED at start to make sure we are ready
for x in range(5):
    led_pin.off()
    time.sleep(.5)
    led_pin.on()
    time.sleep(.5)


print("Waiting for data...\n")

while True:
    # Check if the XBee has any message in the queue.
    received_msg = xbee.receive()
    if received_msg:
        # Get payload from the received message.
        payload = received_msg['payload']
        data = payload.decode()
        print("Data received: ", data) 
        if data == "ON":
            led_pin.on()
        elif data == "OFF":
            led_pin.off()
            
