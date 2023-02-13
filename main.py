import sys
from datetime import datetime

from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtCore
from about import Ui_About
from window import Ui_ResistorCalculator
from work_string import parse_string

version = 'v0.1 from 10.02.2023'


def on_click_calculator():
    s = ui.ResistFormula.text()
    if not s:
        return
    if ui.radioButtonResistor.isChecked():
        s = parse_string(s, 'resistor')
        s = float(format(float(s), ".6f"))
        s = '{0:,}'.format(s).replace(',', '.')
        s = s[:s.rfind('.')] + ',' + s[s.rfind('.') + 1:]
        ui.Result.setText(f'Result    {s}R')
    elif ui.radioButtonCapacity.isChecked():
        s = parse_string(s, 'capacity')
        s = float(s)*1000000
        s = '{0:.7f}'.format(s).replace(',', '.')
        s = s[:s.rfind('.')] + ',' + s[s.rfind('.') + 1:]
        ui.Result.setText(f'Result    {s}μF')


def on_click_info():
    global ResistorCalculator, ui_about, About
    About = QtWidgets.QDialog()
    ui_about = Ui_About()
    ui_about.setupUi(About)
    About.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    x = ResistorCalculator.x() + (ResistorCalculator.width() - About.width())//2
    y = ResistorCalculator.y()
    About.setGeometry(x, y, 200, 120)
    a = datetime.today().year
    ui_about.labelCopyright.setText(f'Copyright © 2022-{a} by Stepan Toshel.')
    ui_about.labelName.setText(f"About Resistor Calculator {version[1:4]} ({version[10:]})")
    ui_about.ButtonOk.clicked.connect(About.close)
    About.show()


def on_click_new():
    ui.ResistFormula.setText('')
    ui.Result.setText(f'Result    0,0R')
    ui.radioButtonResistor.setChecked(True)


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
    ui.Result.setText("Result    0,0R")
    ui.ResistFormula.setText('')

def on_click_capacity():
    ui.label.setText("Example: 10m | (10mk + 10N + 20п)")
    ui.Result.setText("Result    0,0μF")
    ui.ResistFormula.setText('')

def on_click_rc():
    ui.label.setText("Example: 10k | (10k + 10M)")#tmp
    ui.Result.setText("Result    0,0R")
    ui.ResistFormula.setText('')


app = QtWidgets.QApplication(sys.argv)
ResistorCalculator = QtWidgets.QMainWindow()
ui = Ui_ResistorCalculator()
ui.setupUi(ResistorCalculator)
ResistorCalculator.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
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
