import xbee


print("Waiting for data...\n")

while True:
    # Check if the XBee has any message in the queue.
    received_msg = xbee.receive()
    if received_msg:
        # Get payload from the received message.
        payload = received_msg['payload']
        print("Data received: ", payload.decode())

