# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zad4.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalScrollBar = QtWidgets.QScrollBar(Form)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(50, 10, 301, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setGeometry(QtCore.QRect(50, 40, 301, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalScrollBar = QtWidgets.QScrollBar(Form)
        self.verticalScrollBar.setGeometry(QtCore.QRect(10, 90, 16, 160))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalSlider = QtWidgets.QSlider(Form)
        self.verticalSlider.setGeometry(QtCore.QRect(40, 90, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 100, 71, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(240, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.verticalSlider.setInvertedAppearance(True)
        self.horizontalSlider.setInvertedAppearance(True)
        self.horizontalScrollBar.setInvertedAppearance(False)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Позиция"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
