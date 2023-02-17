import random
import string
import serial

# port = serial.Serial(port='COM56', baudrate=230400, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

package = bytearray([0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd9, 0x35, 0x72, 0xcd])

package_def = bytearray(
    [0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd9, 0x35, 0x72, 0xcd])  # все вых. дис. каналы выключены
package_start = bytearray(
    [0x0c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xd9, 0x35, 0x72, 0xcd])  # все вых. дис. каналы включены
count_def = 1
count_start = 0
MAX_COUNT_DEF = 20000
MAX_COUNT_START = 5000


def answerReader():
    # answer = port.read(size=16)
    # answerList = " ".join(list(answer))+'\n'
    answerList = ' '.join(
        (random.choice(string.digits + 'abcdef') + random.choice(string.digits + 'abcdef')) for i in range(56)) + '\n'
    if '00 00 00' == answerList[6:14]:
        pass  # сокращенное
    else:
        pass  # полное
    save_data(answerList)
    parser_data(answerList)
    '''
    print(' ')
    for incomingByte in answerList:
        print('%-4d' % incomingByte, end=' ')
    '''


def save_data(s: str):
    with open('test.txt', 'a') as file:  # дописывание файла
        file.write(s)


def load_data():
    with open('test.txt', 'r') as file:
        pass


def parser_data(s: str):
    pass


while True:
    if count_def != MAX_COUNT_DEF and count_def:
        port.write(package)
        count_def += 1
    else:
        count_def = 0
        count_start = 1
    if count_start != MAX_COUNT_START and count_start:
        port.write(package)
        count_start += 1
    else:
        count_def = 1
        count_start = 0
    answerReader()
