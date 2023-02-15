import sys
from datetime import datetime
from typing import Union

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtCore
from about import Ui_About
from window import Ui_ResistorCalculator
from work_string import parse_string

version = '0.1.5 14.02.2023'


def select_symbol(type: str) -> Union[float, str]:
    if ui.radioButtonResistor.isChecked() or ui.radioButtonRC.isChecked():
        if ui.radioButtonSymbol1.isChecked():  # may be switch if it can?
            if type == 'value':
                return 1.0
            elif type == 'symbol':
                return 'Ω'
        elif ui.radioButtonSymbol2.isChecked():
            if type == 'value':
                return 0.001
            elif type == 'symbol':
                return 'kΩ'
        elif ui.radioButtonSymbol3.isChecked():
            if type == 'value':
                return 0.000001
            elif type == 'symbol':
                return 'MΩ'
        elif ui.radioButtonSymbol4.isChecked():
            if type == 'value':
                return 0.000000001
            elif type == 'symbol':
                return 'GΩ'
    elif ui.radioButtonCapacity.isChecked():
        if ui.radioButtonSymbol1.isChecked():
            if type == 'value':
                return 1000.0
            elif type == 'symbol':
                return 'mF'
        elif ui.radioButtonSymbol2.isChecked():
            if type == 'value':
                return 1000000.0
            elif type == 'symbol':
                return 'μF'
        elif ui.radioButtonSymbol3.isChecked():
            if type == 'value':
                return 1000000000.0
            elif type == 'symbol':
                return 'nF'
        elif ui.radioButtonSymbol4.isChecked():
            if type == 'value':
                return 1000000000000.0
            elif type == 'symbol':
                return 'pF'


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
    s = float(s) * select_symbol('value')
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
    file, check = QFileDialog.getSaveFileName(None, 'Save file', 'c:\\', "Text Files (*.txt);;All Files (*)")

    if check:
        with open(file, "w") as file:
            formula = ui.ResistFormula.text()
            file.write(f"Formula   {formula}\n")
            result = ui.Result.text()
            file.write(result)


def on_click_open():
    file, check = QFileDialog.getOpenFileName(None, 'Open file', 'c:\\', "Text Files (*.txt);;All Files (*)")

    if check:
        with open(file, "r") as file:
            formula = file.readline()
            ui.ResistFormula.setText(formula[10:-1])
            result = file.readline()
            ui.Result.setText(result)


def on_click_resistor():
    ui.label.setText("Example: 10k | (10k + 10M)")
    ui.Result.setText("Result    0Ω")
    ui.ResistFormula.setText('')
    ui.radioButtonSymbol1.setChecked(True)
    ui.radioButtonSymbol1.setText("Ω")
    ui.radioButtonSymbol2.setText("kΩ")
    ui.radioButtonSymbol3.setText("MΩ")
    ui.radioButtonSymbol4.setText("GΩ")


def on_click_capacity():
    ui.label.setText("Example: 10m | (10mk + 10N + 20п)")
    ui.Result.setText("Result    0μF")
    ui.ResistFormula.setText('')
    ui.radioButtonSymbol2.setChecked(True)
    ui.radioButtonSymbol1.setText("mF")
    ui.radioButtonSymbol2.setText("μF")
    ui.radioButtonSymbol3.setText("nF")
    ui.radioButtonSymbol4.setText("pF")


def on_click_rc():
    ui.label.setText("Example: 10k + 10mk + 2.7V/3.3V (or 82%)")  # tmp
    ui.Result.setText("Result    0s")
    ui.ResistFormula.setText('')
    ui.radioButtonSymbol1.setChecked(True)
    ui.radioButtonSymbol1.setText("s")
    ui.radioButtonSymbol2.setText("ms")
    ui.radioButtonSymbol3.setText("mks")
    ui.radioButtonSymbol4.setText("ns")


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

sys.exit(app.exec_())
