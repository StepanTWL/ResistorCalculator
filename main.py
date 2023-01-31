from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from work_string import parse_string


def on_click():
    s = form.ResistFormula.text()
    if not s:
        return
    s = parse_string(s)
    s = float(format(float(s), ".6f"))
    s = '{0:,}'.format(s).replace(',', '.', str(s).count(','))
    form.Result.setText(f'Result   {s}R')


Form, Window = uic.loadUiType("window.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.ButtonCalculate.clicked.connect(on_click)

app.exec_()
