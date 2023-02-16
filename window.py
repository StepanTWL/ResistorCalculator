# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ResistorCalculator(object):
    def setupUi(self, ResistorCalculator):
        ResistorCalculator.setObjectName("ResistorCalculator")
        ResistorCalculator.setEnabled(True)
        ResistorCalculator.resize(800, 200)
        ResistorCalculator.setMinimumSize(QtCore.QSize(800, 200))
        ResistorCalculator.setMaximumSize(QtCore.QSize(800, 200))
        icon = QtGui.QIcon.fromTheme("d:\\MyProject\\Python\\ResistorCalculator\\images\\icon.png")
        ResistorCalculator.setWindowIcon(icon)
        ResistorCalculator.setStyleSheet("#QMainWindow{background-color: rgb(200,200,200);}")
        ResistorCalculator.setIconSize(QtCore.QSize(64, 64))
        self.centralwidget = QtWidgets.QWidget(ResistorCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.Result = QtWidgets.QLabel(self.centralwidget)
        self.Result.setGeometry(QtCore.QRect(70, 96, 640, 20))
        self.Result.setMinimumSize(QtCore.QSize(640, 20))
        self.Result.setMaximumSize(QtCore.QSize(640, 20))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.Result.setFont(font)
        self.Result.setObjectName("Result")
        self.ResistFormula = QtWidgets.QLineEdit(self.centralwidget)
        self.ResistFormula.setGeometry(QtCore.QRect(70, 26, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(12)
        self.ResistFormula.setFont(font)
        self.ResistFormula.setInputMask("")
        self.ResistFormula.setText("")
        self.ResistFormula.setObjectName("ResistFormula")
        self.ButtonCalculate = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonCalculate.setGeometry(QtCore.QRect(300, 127, 200, 30))
        self.ButtonCalculate.setMinimumSize(QtCore.QSize(200, 30))
        self.ButtonCalculate.setMaximumSize(QtCore.QSize(200, 30))
        font = QtGui.QFont()
        font.setFamily("Rubik SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.ButtonCalculate.setFont(font)
        self.ButtonCalculate.setStyleSheet("QPushButton {\n"
"    background-color:  rgb(0, 120, 255);\n"
"    color:  rgb(240, 240, 240);\n"
"    border-radius: 8px;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:  rgb(0, 120, 255);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(0, 25, 240);\n"
"}")
        self.ButtonCalculate.setObjectName("ButtonCalculate")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(720, 8, 120, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButtonResistor = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButtonResistor.setChecked(True)
        self.radioButtonResistor.setObjectName("radioButtonResistor")
        self.verticalLayout.addWidget(self.radioButtonResistor)
        self.radioButtonCapacity = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButtonCapacity.setChecked(False)
        self.radioButtonCapacity.setObjectName("radioButtonCapacity")
        self.verticalLayout.addWidget(self.radioButtonCapacity)
        self.radioButtonRC = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButtonRC.setObjectName("radioButtonRC")
        self.verticalLayout.addWidget(self.radioButtonRC)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 60, 261, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonSymbol1 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.radioButtonSymbol1.setFont(font)
        self.radioButtonSymbol1.setChecked(True)
        self.radioButtonSymbol1.setObjectName("radioButtonSymbol1")
        self.horizontalLayout.addWidget(self.radioButtonSymbol1)
        self.radioButtonSymbol2 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.radioButtonSymbol2.setFont(font)
        self.radioButtonSymbol2.setObjectName("radioButtonSymbol2")
        self.horizontalLayout.addWidget(self.radioButtonSymbol2)
        self.radioButtonSymbol3 = QtWidgets.QRadioButton(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButtonSymbol3.sizePolicy().hasHeightForWidth())
        self.radioButtonSymbol3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.radioButtonSymbol3.setFont(font)
        self.radioButtonSymbol3.setObjectName("radioButtonSymbol3")
        self.horizontalLayout.addWidget(self.radioButtonSymbol3)
        self.radioButtonSymbol4 = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Rubik")
        font.setPointSize(11)
        self.radioButtonSymbol4.setFont(font)
        self.radioButtonSymbol4.setAutoRepeatDelay(0)
        self.radioButtonSymbol4.setObjectName("radioButtonSymbol4")
        self.horizontalLayout.addWidget(self.radioButtonSymbol4)
        ResistorCalculator.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ResistorCalculator)
        self.statusbar.setObjectName("statusbar")
        ResistorCalculator.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(ResistorCalculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        ResistorCalculator.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(ResistorCalculator)
        icon = QtGui.QIcon.fromTheme("d:\\MyProject\\Python\\ResistorCalculator\\images\\new.png")
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(ResistorCalculator)
        icon = QtGui.QIcon.fromTheme("d:\\MyProject\\Python\\ResistorCalculator\\images\\save.png")
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(ResistorCalculator)
        icon = QtGui.QIcon.fromTheme("d:\\MyProject\\Python\\ResistorCalculator\\images\\open.png")
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(ResistorCalculator)
        icon = QtGui.QIcon.fromTheme("d:\\MyProject\\Python\\ResistorCalculator\\images\\exit.png")
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.actionInfo = QtWidgets.QAction(ResistorCalculator)
        icon = QtGui.QIcon.fromTheme("d:\\MyProject\\Python\\ResistorCalculator\\images\\info.png")
        self.actionInfo.setIcon(icon)
        self.actionInfo.setObjectName("actionInfo")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInfo)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(ResistorCalculator)
        QtCore.QMetaObject.connectSlotsByName(ResistorCalculator)

    def retranslateUi(self, ResistorCalculator):
        _translate = QtCore.QCoreApplication.translate
        ResistorCalculator.setWindowTitle(_translate("ResistorCalculator", "Resistor Calculator"))
        self.Result.setText(_translate("ResistorCalculator", "Result    0Ω"))
        self.ButtonCalculate.setText(_translate("ResistorCalculator", "Calculate"))
        self.radioButtonResistor.setText(_translate("ResistorCalculator", "Resistor"))
        self.radioButtonCapacity.setText(_translate("ResistorCalculator", "Capacity"))
        self.radioButtonRC.setText(_translate("ResistorCalculator", "RC-circuit"))
        self.radioButtonSymbol1.setText(_translate("ResistorCalculator", "Ω"))
        self.radioButtonSymbol2.setText(_translate("ResistorCalculator", "kΩ"))
        self.radioButtonSymbol3.setText(_translate("ResistorCalculator", "MΩ"))
        self.radioButtonSymbol4.setText(_translate("ResistorCalculator", "GΩ"))
        self.menuFile.setTitle(_translate("ResistorCalculator", "File"))
        self.menuHelp.setTitle(_translate("ResistorCalculator", "Help"))
        self.actionNew.setText(_translate("ResistorCalculator", "New"))
        self.actionNew.setShortcut(_translate("ResistorCalculator", "Ctrl+N"))
        self.actionSave.setText(_translate("ResistorCalculator", "Save"))
        self.actionSave.setShortcut(_translate("ResistorCalculator", "Ctrl+S"))
        self.actionOpen.setText(_translate("ResistorCalculator", "Open"))
        self.actionOpen.setShortcut(_translate("ResistorCalculator", "Ctrl+O"))
        self.actionExit.setText(_translate("ResistorCalculator", "Exit"))
        self.actionExit.setShortcut(_translate("ResistorCalculator", "Alt+X"))
        self.actionInfo.setText(_translate("ResistorCalculator", "Info"))
        self.actionInfo.setShortcut(_translate("ResistorCalculator", "F1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ResistorCalculator = QtWidgets.QMainWindow()
    ui = Ui_ResistorCalculator()
    ui.setupUi(ResistorCalculator)
    ResistorCalculator.show()
    sys.exit(app.exec_())

