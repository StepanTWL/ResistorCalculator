# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 120)
        About.setMinimumSize(QtCore.QSize(400, 120))
        About.setMaximumSize(QtCore.QSize(400, 120))
        self.label = QtWidgets.QLabel(About)
        self.label.setGeometry(QtCore.QRect(30, 20, 311, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.ButtonOk = QtWidgets.QPushButton(About)
        self.ButtonOk.setGeometry(QtCore.QRect(160, 90, 75, 23))
        self.ButtonOk.setObjectName("ButtonOk")
        self.label_2 = QtWidgets.QLabel(About)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(9)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(About)
        self.label_4.setGeometry(QtCore.QRect(40, 29, 351, 71))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(9)
        font.setKerning(True)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(About)
        self.label_3.setGeometry(QtCore.QRect(40, 60, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(9)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.label.setText(_translate("About", "About Resistor Calculator 0.1 (02.02.2023)"))
        self.ButtonOk.setText(_translate("About", "OK"))
        self.label_2.setText(_translate("About", "Copyright © 2022-2022 by Stepan Toshel."))
        self.label_3.setText(_translate("About", "Program for calculating the resistance of electrical circuits."))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

