import time
import serial

ser = serial.Serial(
    # Serial Port to read the data from
    port='COM6',

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
packet.append(0x01)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x00)
packet.append(0x7c)
packet.append(0xe6)
packet.append(0x2e)
packet.append(0x06)
packet_rx = [0]*100
#ser.open()
# Mentions the Current Counter number for each line written
# Pauses for one second each iteration to avoid overworking the port
while 1:
    ser.write(packet)
    time.sleep(5)
    ser.read(packet_rx)
    print(packet_rx)
    time.sleep(5)