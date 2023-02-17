from PyQt5 import QtWidgets, uic
from PyQt5.QtSerialPort import QSerialPort

app = QtWidgets.QApplication([])
win = uic.loadUi('test.ui')

serial = QSerialPort()
serial.setBaudRate(230400)

def Begin():
    nameBt = win.ComBt.text()
    if nameBt == 'SEARCH':
        port

