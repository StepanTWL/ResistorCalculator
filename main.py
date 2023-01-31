from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from work_string import parse_string


def on_click():
    s = form.ResistFormula.text()
    s = parse_string(s)
    form.Result.setText(f'Result   {format(float(s), ".6f")}R')


Form, Window = uic.loadUiType("window.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

form.ButtonCalculate.clicked.connect(on_click)

app.exec_()
