# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created: Mon May 15 09:21:14 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='', db='major')
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

class Ui_MainWindow(object):
    def signUpCheck(self):
        username=self.uname_lineEdit.text()
        password= self.pass_lineEdit.text()
        emailid=self.email_lineEdit.text()

       
        
        #conn=pymysql.connect(host='localhost', database='major' , user='root', password='')
        #connection=conn.cursor()
        #sql="INSERT INTO users(uname,password,emailid) VALUES (?,?,?)"

        #connection.execute(sql,[username,password,emailid])

        def setupUi(self, MainWindow):
            MainWindow.setObjectName(_fromUtf8("MainWindow"))
            MainWindow.resize(800, 600)
            self.centralwidget = QtGui.QWidget(MainWindow)
            self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

    
        self.uname_label = QtGui.QLabel(self.centralwidget)
        self.uname_label.setGeometry(QtCore.QRect(200, 170, 131, 51))
        self.uname_label.setObjectName(_fromUtf8("uname_label"))

        self.pass_label = QtGui.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(200, 220, 131, 51))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))

        self.email_label = QtGui.QLabel(self.centralwidget)
        self.email_label.setGeometry(QtCore.QRect(200, 270, 131, 51))
        self.email_label.setObjectName(_fromUtf8("email_label"))

        self.uname_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.uname_lineEdit.setGeometry(QtCore.QRect(310, 180, 281, 27))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.pass_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.pass_lineEdit.setGeometry(QtCore.QRect(310, 230, 281, 27))
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        self.email_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.email_lineEdit.setGeometry(QtCore.QRect(310, 280, 281, 27))
        self.email_lineEdit.setObjectName(_fromUtf8("email_lineEdit"))

        self.signup_btn = QtGui.QPushButton(self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(490, 340, 98, 27))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
########################Button Event################################
        self.signup_btn.clicked.connect(self.signUpCheck)
####################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.uname_label.setText(_translate("MainWindow", "Username", None))
        self.pass_label.setText(_translate("MainWindow", "Password", None))
        self.email_label.setText(_translate("MainWindow", "Email id", None))
        self.signup_btn.setText(_translate("MainWindow", "Sign Up", None))


        #conn.commit()
        #conn.close()
 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

