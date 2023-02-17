import time
import serial

ser = serial.Serial(
    # Serial Port to read the data from
    port='COM56',

    # Rate at which the information is shared to the communication channel
    baudrate=230400,

    # Applying Parity Checking (none in this case)
    #parity=serial.PARITY_NONE,

    # Pattern of Bits to be read
    #stopbits=serial.STOPBITS_ONE,

    # Total number of bits to be read
    #bytesize=serial.EIGHTBITS,

    # Number of serial commands to accept before timing out
    timeout=0
)

packet = bytearray()
packet.append(0x0c)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0xd9)
packet.append(0x35)
packet.append(0x72)
packet.append(0xcd)
#ser.open()
# Mentions the Current Counter number for each line written
# Pauses for one second each iteration to avoid overworking the port
while 1:
    ser.write(packet)
    time.sleep(5)