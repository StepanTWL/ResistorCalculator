import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from work_string import parse_string


def on_click_calculator():
    s = form.ResistFormula.text()
    if not s:
        return
    s = parse_string(s)
    s = float(format(float(s), ".6f"))
    s = '{0:,}'.format(s).replace(',', '.')
    s = s[:s.rfind('.')] + ',' + s[s.rfind('.')+1:]
    form.Result.setText(f'Result   {s}R')

def on_click_info():
    global windowAbout
    FormAbout, WindowAbout = uic.loadUiType("about.ui")
    windowAbout = WindowAbout()
    formAbout = FormAbout()
    formAbout.setupUi(windowAbout)
    width = window.size().width()
    height = window.size().height()
    x = window.x() + 300
    y = window.y() + 100
    windowAbout.setGeometry(x, y, 200, 120)
    windowAbout.setWindowTitle('Help')
    windowAbout.show()
    formAbout.ButtonOk.triggered.connect(sys.exit)


Form, Window = uic.loadUiType("window.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.ButtonCalculate.clicked.connect(on_click_calculator)
#form.actionNew.triggered.connect()
#form.actionSave.triggered.connect()
#form.actionOpen.triggered.connect()
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
