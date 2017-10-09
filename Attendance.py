# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reco.ui'
#
# Created: Mon May 15 15:23:41 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
import subprocess
from welcome import welcomeMainWindow
import sys


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

class recoMainWindow(object):



    def setupUi(self, Attendance):
        Attendance.setObjectName(_fromUtf8("Attendance"))
        Attendance.resize(690, 600)
        self.centralwidget = QtGui.QWidget(Attendance)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        ##dataset##
        self.dataset_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.dataset_pushbtn.setGeometry(QtCore.QRect(260, 90, 181, 61))
        self.dataset_pushbtn.setObjectName(_fromUtf8("dataset_pushbtn"))
        self.dataset_pushbtn.clicked.connect(lambda: self.run1('dataset.py'))

        ##detect##
        self.detect_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.detect_pushbtn.setGeometry(QtCore.QRect(260, 300, 181, 61))
        self.detect_pushbtn.setObjectName(_fromUtf8("detect_pushbtn"))
        self.detect_pushbtn.clicked.connect(lambda: self.run1('detect.py'))

        ##trainer##
        self.trainer_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.trainer_pushbtn.setGeometry(QtCore.QRect(260, 190, 181, 61))
        self.trainer_pushbtn.setObjectName(_fromUtf8("trainer_pushbtn"))
        self.trainer_pushbtn.clicked.connect(lambda: self.run1('trainer.py'))
        ##
        ##logout##
        self.logout_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.logout_pushbtn.setGeometry(QtCore.QRect(500, 500, 100, 45))
        self.logout_pushbtn.setObjectName(_fromUtf8("logout_pushbtn"))
###########################################################################

        self.logout_pushbtn.clicked.connect(self.welcomeWindowShow)
        #self.logout_pushbtn.clicked.connect(lambda: self.run1('LoginForm.py'))


        ############

        Attendance.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Attendance)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Attendance.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Attendance)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Attendance.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(Attendance)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Attendance)
        QtCore.QMetaObject.connectSlotsByName(Attendance)

    def run1(self, path):
            subprocess.call(['python', path])

    def retranslateUi(self, Attendance):
        Attendance.setWindowTitle(_translate("Attendance", "Attendance", None))
        self.dataset_pushbtn.setText(_translate("Attendance", "Dataset", None))
        self.detect_pushbtn.setText(_translate("Attendance", "Detect", None))
        self.trainer_pushbtn.setText(_translate("Attendance", "Trainer", None))
        self.logout_pushbtn.setText(_translate("Attendance", "Logout", None))

        self.menuFile.setTitle(_translate("Attendance", "File", None))
        self.menuHelp.setTitle(_translate("Attendance", "Help", None))
        self.actionExit.setText(_translate("Attendance", "Exit", None))

    def welcomeWindowShow(self):
        sys.exit()
        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = welcomeMainWindow()
        self.ui.setupUi(self.welcomeWindow)
        self.welcomeWindow.show()
        Attendance.hide()







if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Attendance = QtGui.QMainWindow()
    ui = recoMainWindow()
    ui.setupUi(Attendance)
    Attendance.show()
    sys.exit(app.exec_())




