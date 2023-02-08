import sys
from datetime import datetime
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QFileDialog
from work_string import parse_string

version = '0.1'


def on_click_calculator():
    s = form.ResistFormula.text()
    if not s:
        return
    s = parse_string(s)
    s = float(format(float(s), ".6f"))
    s = '{0:,}'.format(s).replace(',', '.')
    s = s[:s.rfind('.')] + ',' + s[s.rfind('.') + 1:]
    form.Result.setText(f'Result    {s}R')


def on_click_info():
    global windowAbout, window, formAbout
    FormAbout, WindowAbout = uic.loadUiType("about.ui")
    windowAbout = WindowAbout()
    formAbout = FormAbout()
    formAbout.setupUi(windowAbout)
    width = window.size().width()
    height = window.size().height()
    x = window.x() + 300
    y = window.y() + 100
    windowAbout.setGeometry(x, y, 200, 120)
    windowAbout.show()
    a = datetime.today().year
    s = formAbout.label_2.text()
    formAbout.label_2.setText(s[:17] + str(a) + s[21:])
    a = datetime.today().strftime("%d.%m.%Y")
    s = formAbout.label.text()
    formAbout.label.setText(f"About Resistor Calculator {version} ({a})")
    formAbout.ButtonOk.clicked.connect(windowAbout.close)


def on_click_new():
    form.ResistFormula.setText('')
    form.Result.setText(f'Result    0,0R')


def on_click_save():
    file, check = QFileDialog.getSaveFileName(None, 'Save file', 'c:\\', "Text Files (*.txt);;All Files (*)")

    if check:
        with open(file, "w") as file:
            formula = form.ResistFormula.text()
            file.write(f"Formula   {formula}\n")
            result = form.Result.text()
            file.write(result)


def on_click_open():
    file, check = QFileDialog.getOpenFileName(None, 'Open file', 'c:\\', "Text Files (*.txt);;All Files (*)")

    if check:
        with open(file, "r") as file:
            formula = file.readline()
            form.ResistFormula.setText(formula[10:-1])
            result = file.readline()
            form.Result.setText(result)


Form, Window = uic.loadUiType("window.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.ButtonCalculate.clicked.connect(on_click_calculator)
form.actionNew.triggered.connect(on_click_new)
form.actionSave.triggered.connect(on_click_save)
form.actionOpen.triggered.connect(on_click_open)
form.actionInfo.triggered.connect(on_click_info)
form.actionExit.triggered.connect(sys.exit)

app.exec_()

'''
    @pyqtSlot()
    def on_pushButtonPrint_clicked(self):

        cmd = 'python _QPushButton-SignalsExample.py'                       # python
        output = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)  # 

        exePath = "C:/Windows/system32/calc.exe"                            # .exe
        subprocess.Popen(exePath)                                           #

        self.close()                                                        # <<<===                                   

'''
