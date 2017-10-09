# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created: Fri Jul 28 08:52:57 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Attendance import recoMainWindow
from Surveillance import survMainWindow
import Surveillance
import Attendance
import subprocess
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Home(object):
    def recoWindowShow(self):
        self.recoWindow=QtGui.QMainWindow()
        self.ui=recoMainWindow()
        self.ui.setupUi(self.recoWindow)
        #Home.hide()
        self.recoWindow.show()


    def survWindowShow(self):
        self.survWindow = QtGui.QMainWindow()
        self.ui = survMainWindow()
        self.ui.setupUi(self.survWindow)
        #Home.hide()
        self.survWindow.show()


    def setupUi(self, Home):
        Home.setObjectName(_fromUtf8("Home"))
        Home.resize(400, 300)
        self.attendance_pushbtn = QtGui.QPushButton(Home)
        self.attendance_pushbtn.setGeometry(QtCore.QRect(40, 110, 151, 61))
        self.attendance_pushbtn.setObjectName(_fromUtf8("attendance_pushbtn"))
        ################################################################
        self.attendance_pushbtn.clicked.connect(self.recoWindowShow)
        ####################################################
        self.surveillance_pushbtn = QtGui.QPushButton(Home)
        self.surveillance_pushbtn.setGeometry(QtCore.QRect(220, 110, 151, 61))
        self.surveillance_pushbtn.setObjectName(_fromUtf8("surveillance_pushbtn"))
        ################################################################
        self.surveillance_pushbtn.clicked.connect(self.survWindowShow)
        ####################################################
        self.welcome_lineEdit = QtGui.QLineEdit(Home)
        self.welcome_lineEdit.setGeometry(QtCore.QRect(92, 20, 231, 27))
        self.welcome_lineEdit.setObjectName(_fromUtf8("welcome_lineEdit"))

        self.retranslateUi(Home)
        QtCore.QMetaObject.connectSlotsByName(Home)

    def retranslateUi(self, Home):
        Home.setWindowTitle(_translate("Home", "Home", None))
        self.attendance_pushbtn.setText(_translate("Home", "Attendance System", None))
        self.surveillance_pushbtn.setText(_translate("Home", "Surveillance System", None))
        self.welcome_lineEdit.setText(_translate("Home", "                      WELCOME", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Home = QtGui.QDialog()
    ui = Ui_Home()
    ui.setupUi(Home)
    Home.show()
    sys.exit(app.exec_())


