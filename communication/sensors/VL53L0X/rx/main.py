import xbee
from machine import PWM
from time import sleep

pwm0 = PWM('P0')   # create PWM object from a pin
myDelay = 0.0005

print("Waiting for data...\n")

while True:
    received_msg = xbee.receive()
    if received_msg:
        # Get payload from the received message.
        payload = received_msg['payload']
        data = payload.decode()
        data = int(data)
        print("Data received: ", data) 
        if(data < 500):
            data = data * 2
            pwm0.duty(data)
