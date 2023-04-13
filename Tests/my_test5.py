import time
import serial

port = serial.Serial(port='COM6', baudrate=230400, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

package = bytearray([0x0c, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x7c, 0xe6, 0x2e, 0x06])
while True:
    c = port.write(package)
    answer = port.read(size=16)
    answerList = list(answer)
    for j in package:
        print(hex(j), end=' ')
    print('')
    for j in answerList:
        print(hex(j), end=' ')
    print('')
    time.sleep(1)