# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created: Sat Jun  3 13:15:13 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
import pymysql
import subprocess
import Surveillance
import Attendance
import Home
from signup1 import signupMainWindow
from Home import Ui_Home
from Attendance import recoMainWindow
from Attendance import welcomeMainWindow
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

class abc(object):
    def showMessageBox(self,title,message):
        msgBox=QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()
                                  


    def HomeWindowShow(self):
        self.HomeWindow=QtGui.QMainWindow()
        self.ui=Ui_Home()
        self.ui.setupUi(self.HomeWindow)
        Login.hide()
        self.HomeWindow.show()


    def signupWindowShow(self):
        self.signupWindow=QtGui.QMainWindow()
        self.ui=signupMainWindow()
        self.ui.setupUi(self.signupWindow)
        Login.hide()
        self.signupWindow.show()

    def logincheck(self):
        usernames=self.uname_lineEdit.text()
        passwords= self.pass_lineEdit.text()
        conn=pymysql.connect(host='localhost', database='major' , user='root', password='')
        connection=conn.cursor()
        
        sql= """select * from users where uname='%s' and password='%s'""" %(usernames,passwords)  
        connection.execute(sql)
        conn.commit()
        countrow= connection.execute(sql)
        if(countrow>0):
            print("user found!")
            #Login.hide()
            self.HomeWindowShow()
        else:
            print("user not found")
            self.showMessageBox('Warning','Invalid Username And Password')

        conn.close()
        #sys.exit(app.exec_())



    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Login)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.uname_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.uname_lineEdit.setGeometry(QtCore.QRect(290, 200, 241, 41))
        self.uname_lineEdit.setObjectName(_fromUtf8("uname_lineEdit"))
        self.pass_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.pass_lineEdit.setGeometry(QtCore.QRect(290, 246, 241, 41))
        self.pass_lineEdit.setObjectName(_fromUtf8("pass_lineEdit"))
        self.login_btn = QtGui.QPushButton(self.centralwidget)
        self.login_btn.setGeometry(QtCore.QRect(320, 320, 98, 27))
        self.login_btn.setObjectName(_fromUtf8("login_btn"))
        #################Button Event################################
        self.login_btn.clicked.connect(self.logincheck)
        #############################################################

        self.signup_btn = QtGui.QPushButton(self.centralwidget)
        self.signup_btn.setGeometry(QtCore.QRect(430, 320, 98, 27))
        self.signup_btn.setObjectName(_fromUtf8("signup_btn"))
        ####################Button Event############################

        self.signup_btn.clicked.connect(self.signupWindowShow)
        #self.signup_btn.clicked.connect(lambda: self.run1('signup1.py'))

        ###########################################################

        self.uname_label = QtGui.QLabel(self.centralwidget)
        self.uname_label.setGeometry(QtCore.QRect(150, 200, 131, 41))
        self.uname_label.setObjectName(_fromUtf8("uname_label"))
        self.pass_label = QtGui.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(150, 240, 121, 41))
        self.pass_label.setObjectName(_fromUtf8("pass_label"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 50, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFIle = QtGui.QMenu(self.menubar)
        self.menuFIle.setObjectName(_fromUtf8("menuFIle"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        Login.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Login)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Login.setStatusBar(self.statusbar)
        self.actionSave = QtGui.QAction(Login)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(Login)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFIle.addAction(self.actionSave)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionExit)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def run1(self, path):
            subprocess.call(['python', path])

    def retranslateUi(self, MainWindow):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.login_btn.setText(_translate("Login", "Login", None))
        self.signup_btn.setText(_translate("Login", "Sign Up", None))
        self.uname_label.setText(_translate("Login", "Username", None))
        self.pass_label.setText(_translate("Login", "Password", None))
        self.label.setText(_translate("Login", "Login Form", None))
        self.menuFIle.setTitle(_translate("Login", "FIle", None))
        self.menuEdit.setTitle(_translate("Login", "Edit", None))
        self.actionSave.setText(_translate("Login", "Save", None))
        self.actionExit.setText(_translate("Login", "Exit", None))





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Login = QtGui.QMainWindow()
    ui = abc()
    ui.setupUi(Login)
    Login.show()
    #Login.hide()

    sys.exit(app.exec_())

