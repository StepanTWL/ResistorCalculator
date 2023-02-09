import sys
from datetime import datetime
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from about import Ui_About
from window import Ui_ResistorCalculator
from work_string import parse_string

version = '0.1'


def on_click_calculator():
    s = ui.ResistFormula.text()
    if not s:
        return
    s = parse_string(s)
    s = float(format(float(s), ".6f"))
    s = '{0:,}'.format(s).replace(',', '.')
    s = s[:s.rfind('.')] + ',' + s[s.rfind('.') + 1:]
    ui.Result.setText(f'Result    {s}R')


def on_click_info():
    global ui, ui_about, About
    About = QtWidgets.QDialog()
    ui_about = Ui_About()
    ui_about.setupUi(About)
    About.show()
    #x = ui.x() + 300
    #y = ui.y() + 100
    #ui_about.setGeometry(x, y, 200, 120)
    a = datetime.today().year
    s = ui_about.labelCopyright.text()
    ui_about.labelCopyright.setText(s[:17] + str(a) + s[21:])
    a = datetime.today().strftime("%d.%m.%Y")
    s = ui_about.labelName.text()
    ui_about.labelName.setText(f"About Resistor Calculator {version} ({a})")
    ui_about.ButtonOk.clicked.connect(About.close)


def on_click_new():
    ui.ResistFormula.setText('')
    ui.Result.setText(f'Result    0,0R')


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


app = QtWidgets.QApplication(sys.argv)
ResistorCalculator = QtWidgets.QMainWindow()
ui = Ui_ResistorCalculator()
ui.setupUi(ResistorCalculator)
ResistorCalculator.show()


ui.ButtonCalculate.clicked.connect(on_click_calculator)
ui.actionNew.triggered.connect(on_click_new)
ui.actionSave.triggered.connect(on_click_save)
ui.actionOpen.triggered.connect(on_click_open)
ui.actionInfo.triggered.connect(on_click_info)
ui.actionExit.triggered.connect(sys.exit)

sys.exit(app.exec_())

'''
    @pyqtSlot()
    def on_pushButtonPrint_clicked(self):

        cmd = 'python _QPushButton-SignalsExample.py'                       # python
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)  # 

        exePath = "C:/Windows/system32/calc.exe"                            # .exe
        subprocess.Popen(exePath)                                           #

        self.close()                                                        # <<<===                                   

'''
