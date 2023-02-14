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
        About.resize(450, 120)
        About.setMinimumSize(QtCore.QSize(450, 120))
        About.setMaximumSize(QtCore.QSize(450, 120))
        icon = QtGui.QIcon.fromTheme("d:\\MyProject\\Python\\ResistorCalculator\\images\\info.png")
        About.setWindowIcon(icon)
        self.labelName = QtWidgets.QLabel(About)
        self.labelName.setGeometry(QtCore.QRect(90, 15, 341, 16))
        font = QtGui.QFont()
        font.setFamily("Rubik Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.labelName.setFont(font)
        self.labelName.setObjectName("labelName")
        self.ButtonOk = QtWidgets.QPushButton(About)
        self.ButtonOk.setGeometry(QtCore.QRect(185, 85, 80, 25))
        self.ButtonOk.setObjectName("ButtonOk")
        self.labelCopyright = QtWidgets.QLabel(About)
        self.labelCopyright.setGeometry(QtCore.QRect(90, 40, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setKerning(True)
        self.labelCopyright.setFont(font)
        self.labelCopyright.setObjectName("labelCopyright")
        self.labelDescription = QtWidgets.QLabel(About)
        self.labelDescription.setGeometry(QtCore.QRect(90, 60, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(10)
        font.setKerning(True)
        self.labelDescription.setFont(font)
        self.labelDescription.setScaledContents(True)
        self.labelDescription.setObjectName("labelDescription")
        self.labelIcon = QtWidgets.QLabel(About)
        self.labelIcon.setGeometry(QtCore.QRect(10, 10, 70, 70))
        self.labelIcon.setMinimumSize(QtCore.QSize(70, 70))
        self.labelIcon.setMaximumSize(QtCore.QSize(70, 70))
        self.labelIcon.setStyleSheet("image: url(:/newPrefix/icon.png);")
        self.labelIcon.setText("")
        self.labelIcon.setObjectName("labelIcon")

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        self.labelName.setText(_translate("About", "About Resistor Calculator 0.0 (01.01.1970)"))
        self.ButtonOk.setText(_translate("About", "OK"))
        self.labelCopyright.setText(_translate("About", "Copyright © 2022-2022 by Stepan Toshel."))
        self.labelDescription.setText(_translate("About", "Program for calculating the resistance of electrical circuits."))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About = QtWidgets.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())

