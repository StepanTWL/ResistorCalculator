# Подключение модуля serial
import time
import serial

port = serial.Serial(port='COM56', baudrate=230400, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

package = bytearray([0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd9, 0x35, 0x72, 0xcd])


def answerReader():
    global count, count1
    answer = port.read(size=16)
    '''
    answerList = list(answer)
    print(' ')
    for incomingByte in answerList:
        print('%-4d' % incomingByte, end=' ')
    '''

while True:
    port.write(package)
    answerReader()