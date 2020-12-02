""" Program to check input type in Python """
import xbee

# Replace the address with your xbee target address
TARGET_64BIT_ADDR = b'\x00\x13\xA2\x00\x41\xB4\xCA\x95'
MESSAGE = "Hello XBee!"

while True:
    COMMAND = input("Enter command : ")

    if COMMAND == "discover":
        print("Discovering network devices...\n")
        # Discover the network devices and print their basic information.
        for device in xbee.discover():
            addr64 = device['sender_eui64']
            node_id = device['node_id']
            rssi = device['rssi']


        print("New discovered device:\n"
              "  - 64-bit address: %s\n"
              "  - Node identifier: %s\n"
              "  - RSSI: %d\n"
              % (''.join('{:02x}'.format(x).upper() for x in addr64), node_id, rssi))

        print("Network discovery finished")

    if COMMAND == "connect":

        while MESSAGE != "exit":
            MESSAGE = input("enter message : ")
            print("\nSending data to %s >> %s" % (''.join('{:02x}'.format(x).upper() for x in TARGET_64BIT_ADDR), MESSAGE))

            try:
                xbee.transmit(TARGET_64BIT_ADDR, MESSAGE)
                print("\nData sent successfully")
            except Exception as e:
                print("\nTransmit failure: %s" % str(e))
        # reset the message string
        MESSAGE == ""
    else:
        print("\ninvalid command\n")
