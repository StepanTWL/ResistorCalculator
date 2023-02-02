import sys
from PyQt5.Qt import *
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QTextDocument, QPainter
from PyQt5.QtWidgets import QLabel, QApplication


class Window(QLabel):
    def __init__(self):
        super(Window, self).__init__()

        self.setStyleSheet('background-color: rgb(68, 207, 203);')
        self.setText("Hello World")

    def paintEvent(self, event):
        doc = QTextDocument()
        if self.textFormat() == Qt.RichText or \
                self.textFormat() == Qt.AutoText and \
                Qt.mightBeRichText(self.text()):

            doc.setHtml(self.text())
        else:
            doc.setPlainText(self.text())

        frame = doc.rootFrame().frameFormat()
        frame.setMargin(0)
        doc.rootFrame().setFrameFormat(frame)
        scale = min(
            self.width() / doc.size().width(),
            self.height() / doc.size().height()
        )
        qp = QPainter(self)
        qp.scale(scale, scale)
        doc.drawContents(qp, QRectF(self.rect()))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())