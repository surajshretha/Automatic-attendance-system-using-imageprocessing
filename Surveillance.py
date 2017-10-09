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
    def clo():
        Surveillance.hide()

class survMainWindow(object):
    def welcomeWindowShow(self):
        sys.exit()
        Surveillance = QtGui.QMainWindow()
        self.welcomeWindow = QtGui.QMainWindow()
        self.ui = welcomeMainWindow()
        self.ui.setupUi(self.welcomeWindow)
        Surveillance.hide()
        self.welcomeWindow.show()



    def setupUi(self, Surveillance):
        Surveillance.setObjectName(_fromUtf8("Surveillance"))
        Surveillance.resize(690, 600)
        self.centralwidget = QtGui.QWidget(Surveillance)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        ##dataset##
        self.dataset_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.dataset_pushbtn.setGeometry(QtCore.QRect(260, 90, 181, 61))
        self.dataset_pushbtn.setObjectName(_fromUtf8("dataset_pushbtn"))
        self.dataset_pushbtn.clicked.connect(lambda: self.run1('surv_dataset.py'))

        ##detect##
        self.Surveillance_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.Surveillance_pushbtn.setGeometry(QtCore.QRect(260, 300, 181, 61))
        self.Surveillance_pushbtn.setObjectName(_fromUtf8("detect_pushbtn"))
        self.Surveillance_pushbtn.clicked.connect(lambda: self.run1('surv_detect.py'))

        ##trainer##
        self.trainer_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.trainer_pushbtn.setGeometry(QtCore.QRect(260, 190, 181, 61))
        self.trainer_pushbtn.setObjectName(_fromUtf8("trainer_pushbtn"))
        self.trainer_pushbtn.clicked.connect(lambda: self.run1('surv_trainer.py'))
        ##
        ##logout##
        self.logout_pushbtn = QtGui.QPushButton(self.centralwidget)
        self.logout_pushbtn.setGeometry(QtCore.QRect(500, 500, 100, 45))
        self.logout_pushbtn.setObjectName(_fromUtf8("logout_pushbtn"))
###########################################################################

        self.logout_pushbtn.clicked.connect(self.welcomeWindowShow,)
        #self.logout_pushbtn.clicked.connect(lambda: self.run1('LoginForm.py'))


        ############

        Surveillance.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Surveillance)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        Surveillance.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Surveillance)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Surveillance.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(Surveillance)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Surveillance)
        QtCore.QMetaObject.connectSlotsByName(Surveillance)

    def run1(self, path):
            subprocess.call(['python', path])

    def retranslateUi(self, Surveillance):
        Surveillance.setWindowTitle(_translate("Surveillance", "Surveillance", None))
        self.dataset_pushbtn.setText(_translate("Surveillance", "Dataset", None))
        self.Surveillance_pushbtn.setText(_translate("Surveillance", "Surveillance", None))
        self.trainer_pushbtn.setText(_translate("Surveillance", "Trainer", None))
        self.logout_pushbtn.setText(_translate("Surveillance", "Logout", None))

        self.menuFile.setTitle(_translate("Surveillance", "File", None))
        self.menuHelp.setTitle(_translate("Surveillance", "Help", None))
        self.actionExit.setText(_translate("Surveillance", "Exit", None))









if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Surveillance = QtGui.QMainWindow()
    ui = survMainWindow()
    ui.setupUi(Surveillance)
    Surveillance.show()
    sys.exit(app.exec_())




