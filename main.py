"""
TODO:
1 Save file *.txt, *.json.
2 Save broke.
"""

import sys
from datetime import datetime
from decimal import Decimal
from time import sleep
from typing import Union

from PyQt5 import QtWidgets, QtCore, QtGui
from about import Ui_About
from window import Ui_ResistorCalculator
from work_string import parse_string

version = '0.2.1 13.04.2023'


def select_symbol(type: str) -> Union[float, str]:
    if ui.radioButtonResistor.isChecked():
        if ui.radioButtonSymbol1.isChecked():  # may be switch if it can?
            if type == 'value':
                return Decimal('1.0')
            elif type == 'symbol':
                return 'Ω'
        elif ui.radioButtonSymbol2.isChecked():
            if type == 'value':
                return Decimal('0.001')
            elif type == 'symbol':
                return 'kΩ'
        elif ui.radioButtonSymbol3.isChecked():
            if type == 'value':
                return Decimal('0.000001')
            elif type == 'symbol':
                return 'MΩ'
        elif ui.radioButtonSymbol4.isChecked():
            if type == 'value':
                return Decimal('0.000000001')
            elif type == 'symbol':
                return 'GΩ'
    elif ui.radioButtonCapacity.isChecked():
        if ui.radioButtonSymbol1.isChecked():
            if type == 'value':
                return Decimal('1000.0')
            elif type == 'symbol':
                return 'mF'
        elif ui.radioButtonSymbol2.isChecked():
            if type == 'value':
                return Decimal('1000000.0')
            elif type == 'symbol':
                return 'μF'
        elif ui.radioButtonSymbol3.isChecked():
            if type == 'value':
                return Decimal('1000000000.0')
            elif type == 'symbol':
                return 'nF'
        elif ui.radioButtonSymbol4.isChecked():
            if type == 'value':
                return Decimal('1000000000000.0')
            elif type == 'symbol':
                return 'pF'
    elif ui.radioButtonRC.isChecked():
        if ui.radioButtonSymbol1.isChecked():
            if type == 'value':
                return Decimal('1.0')
            elif type == 'symbol':
                return 's'
        elif ui.radioButtonSymbol2.isChecked():
            if type == 'value':
                return Decimal('1000.0')
            elif type == 'symbol':
                return 'ms'
        elif ui.radioButtonSymbol3.isChecked():
            if type == 'value':
                return Decimal('1000000.0')
            elif type == 'symbol':
                return 'μs'
        elif ui.radioButtonSymbol4.isChecked():
            if type == 'value':
                return Decimal('1000000000.0')
            elif type == 'symbol':
                return 'ns'


def on_click_calculator():
    s1 = ''
    s2 = ''
    s = ui.ResistFormula.text()
    if not s:
        ui.Result.setText(f'Result    0,0{select_symbol("symbol")}')
        return
    if ui.radioButtonResistor.isChecked():
        s = parse_string(s, 'resistor')
    elif ui.radioButtonCapacity.isChecked():
        s = parse_string(s, 'capacity')
    elif ui.radioButtonRC.isChecked():
        s = parse_string(s, 'rc')
    s = Decimal(s) * select_symbol('value')
    s = '{0:.7f}'.format(s).replace('.', ',')
    s = "{:,}".format(int(s[:s.rfind(',')])).replace(',', '.') + s[s.rfind(','):].rstrip(',0')
    if s:
        ui.Result.setText(f'Result    {s}{select_symbol("symbol")}')
    else:
        ui.Result.setText(f'Result    0{select_symbol("symbol")}')


def on_click_info():
    global ResistorCalculator, ui_about, About
    About = QtWidgets.QDialog()
    ui_about = Ui_About()
    ui_about.setupUi(About)
    About.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    x = ResistorCalculator.x() + (ResistorCalculator.width() - About.width()) // 2
    y = ResistorCalculator.y()
    About.setGeometry(x, y, 200, 120)
    a = datetime.today().year
    ui_about.labelCopyright.setText(f'Copyright © 2022-{a} by Stepan Toshel.')
    ui_about.labelName.setText(f"About Resistor Calculator {version.split()[0]} ({version.split()[1]})")
    ui_about.ButtonOk.clicked.connect(About.close)
    About.show()


def on_click_new():
    ui.ResistFormula.setText('')
    ui.Result.setText(f'Result    0Ω')
    ui.radioButtonResistor.setChecked(True)
    ui.radioButtonSymbol1.setChecked(True)


def on_click_save():
    file, check = QtWidgets.QFileDialog.getSaveFileName(None, 'Save file', 'c:\\', "Text Files (*.txt);;All Files (*)")

    if check:
        with open(file, "w") as file:
            formula = ui.ResistFormula.text()
            file.write(f"Formula   {formula}\n")
            result = ui.Result.text()
            file.write(result+"\n")
            if ui.radioButtonResistor.isChecked():
                file.write("Type      R\n")
            elif ui.radioButtonCapacity.isChecked():
                file.write("Type      C\n")
            elif ui.radioButtonRC.isChecked():
                file.write("Type      RC\n")



def on_click_open():
    file, check = QtWidgets.QFileDialog.getOpenFileName(None, 'Open file', 'c:\\', "Text Files (*.txt);;All Files (*)")

    if check:
        with open(file, "r") as file:
            formula = file.readline()
            result = file.readline()
            type = file.readline()
            sleep(1)
            if 'RC' in type:
                ui.radioButtonRC.setChecked(True)
            elif 'R' in type:
                ui.radioButtonCapacity.setChecked(True)
            elif 'C' in type:
                ui.radioButtonResistor.setChecked(True)
            ui.ResistFormula.setText(formula[10:-1])
            ui.Result.setText(result)
            sleep(1)
            if 'ms' in result:
                ui.radioButtonSymbol2.setChecked(True)
            elif 'mks' in type:
                ui.radioButtonSymbol3.setChecked(True)
            elif 'ns' in type:
                ui.radioButtonSymbol4.setChecked(True)
            elif 's' in type:
                ui.radioButtonSymbol1.setChecked(True)

def on_click_resistor():
    ui.ResistFormula.setPlaceholderText("Example: 10.5k|(10k+10m)|(5g+1000)")
    ui.Result.setText("Result    0Ω")
    ui.ResistFormula.setText('')
    ui.radioButtonSymbol1.setChecked(True)
    ui.radioButtonSymbol1.setText("Ω")
    ui.radioButtonSymbol2.setText("kΩ")
    ui.radioButtonSymbol3.setText("MΩ")
    ui.radioButtonSymbol4.setText("GΩ")
    reg = QtCore.QRegExp("[kmgKMG0-9+|*().,]{100}")
    pValidator = QtGui.QRegExpValidator()
    pValidator.setRegExp(reg)
    ui.ResistFormula.setValidator(pValidator)


def on_click_capacity():
    ui.ResistFormula.setPlaceholderText("Example: 10.5m|(10mk+10n+20p)|(1mk+1000p)")
    ui.Result.setText("Result    0μF")
    ui.ResistFormula.setText('')
    ui.radioButtonSymbol2.setChecked(True)
    ui.radioButtonSymbol1.setText("mF")
    ui.radioButtonSymbol2.setText("μF")
    ui.radioButtonSymbol3.setText("nF")
    ui.radioButtonSymbol4.setText("pF")
    reg = QtCore.QRegExp("[kmnpKMNP0-9+|*().,]{100}")
    pValidator = QtGui.QRegExpValidator()
    pValidator.setRegExp(reg)
    ui.ResistFormula.setValidator(pValidator)


def on_click_rc():
    ui.ResistFormula.setPlaceholderText("Example: 10.5k+10mk+2.7V/3.3V(82%)")
    ui.Result.setText("Result    0s")
    ui.ResistFormula.setText('')
    ui.radioButtonSymbol1.setChecked(True)
    ui.radioButtonSymbol1.setText("s")
    ui.radioButtonSymbol2.setText("ms")
    ui.radioButtonSymbol3.setText("mks")
    ui.radioButtonSymbol4.setText("ns")
    reg = QtCore.QRegExp("[kmnpgvKMNPGV0-9+.,%/]{100}")
    pValidator = QtGui.QRegExpValidator()
    pValidator.setRegExp(reg)
    ui.ResistFormula.setValidator(pValidator)


app = QtWidgets.QApplication(sys.argv)
ResistorCalculator = QtWidgets.QMainWindow()
ui = Ui_ResistorCalculator()
ui.setupUi(ResistorCalculator)
ResistorCalculator.setWindowFlags(
    QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
ResistorCalculator.show()

ui.ButtonCalculate.clicked.connect(on_click_calculator)
ui.actionNew.triggered.connect(on_click_new)
ui.actionSave.triggered.connect(on_click_save)
ui.actionOpen.triggered.connect(on_click_open)
ui.actionInfo.triggered.connect(on_click_info)
ui.actionExit.triggered.connect(sys.exit)

ui.radioButtonResistor.toggled.connect(on_click_resistor)
ui.radioButtonCapacity.toggled.connect(on_click_capacity)
ui.radioButtonRC.toggled.connect(on_click_rc)

#reg = QtCore.QRegExp("[kmnpgvKMNPGV0-9+|*().,%/]{100}")
reg = QtCore.QRegExp("[kmgKMG0-9+|*().,]{100}")
pValidator = QtGui.QRegExpValidator()
pValidator.setRegExp(reg)
ui.ResistFormula.setValidator(pValidator)
ui.ResistFormula.setPlaceholderText("Example: 10.5k|(10k+10m)|(5g+1000)")

sys.exit(app.exec_())
