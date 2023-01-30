from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
#from PyQt5 import uic
#from PyQt5.QtWidgets import QApplication
from work_string import parse_string

s = '0'

Form, Window = uic.loadUiType("window.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()

s = form.ResistFormula.text()
form.ButtonCalculate.clicked.connect(lambda s: parse_string(s))
form.Result.setText(s)

app.exec()