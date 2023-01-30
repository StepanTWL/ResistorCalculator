from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QVBoxLayout, QMessageBox


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.line_edit = QLineEdit('123')
        self.button_check = QPushButton('Проверить число!')
        self.button_check.clicked.connect(self._on_check)

        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button_check)

        self.setLayout(layout)

    def _on_check(self):
        text = self.line_edit.text()

        try:
            value = int(text)
            QMessageBox.information(self, 'Информация', 'Введено число: "{}"'.format(value))

        except ValueError:
            QMessageBox.warning(self, 'Внимание', 'Введено невалидное число: "{}"'.format(text))


if __name__ == '__main__':
    app = QApplication([])

    mw = Window()
    mw.show()

    app.exec()