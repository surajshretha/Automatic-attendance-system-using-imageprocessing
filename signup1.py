# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created: Mon May 15 09:21:14 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

import sys
import pymysql
from PyQt4 import QtCore, QtGui

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

class signupMainWindow(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName(_fromUtf8("MainWindow"))
        SignUp.resize(800, 600)
        self.centralwidget = QtGui.QWidget(SignUp)
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
        ###################################################
        SignUp.hide()
        self.signup_btn.clicked.connect(self.signUpCheck)

        ############################################


        SignUp.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(SignUp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        SignUp.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(SignUp)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        SignUp.setStatusBar(self.statusbar)

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        SignUp.setWindowTitle(_translate("SignUp", "SignUp", None))
        self.uname_label.setText(_translate("SignUp", "Username", None))
        self.pass_label.setText(_translate("SignUp", "Password", None))
        self.email_label.setText(_translate("SignUp", "Email id", None))
        self.signup_btn.setText(_translate("SignUp", "Sign Up", None))


    def signUpCheck(self):
        username= self.uname_lineEdit.text()
        password= self.pass_lineEdit.text()
        emailid= self.email_lineEdit.text()

        a=username
        b=password
        c=emailid

        print(a)
        print (b)
        print(c)

        conn=pymysql.connect(host='localhost',database='major',user='root',password='')
        mycursor=conn.cursor()


        sql= """insert into users (uname,password,emailid) values("%s" , "%s" , "%s")""" % (a,b,c)
        mycursor.execute(sql)
        conn.commit()
        conn.close()
        print("New User Created!")
        sys.exit()
    
    


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SignUp = QtGui.QMainWindow()
    ui = signupMainWindow()
    ui.setupUi(SignUp)
    SignUp.show()
    sys.exit(app.exec_())

