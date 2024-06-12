# Form implementation generated from reading ui file 'e:\Coding projects\Jeb's Salon\ui_files\login_page.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        LoginPage.setObjectName("LoginPage")
        LoginPage.resize(1154, 713)
        LoginPage.setStyleSheet("#centralwidget{\n"
"    background-color: #2C2C3B;\n"
"}\n"
"\n"
"#header{\n"
"    color: #E9E8E8;\n"
"}\n"
"#login_pane{\n"
"    border-radius: 35.98px;\n"
"    background-color: #5A2E74;\n"
"}\n"
"#user_name, #user_password{\n"
"    background-color:  #E2CFEA;\n"
"}\n"
"#user_name, #user_password, #login_button{\n"
"    border-radius: 14.39px;\n"
"}\n"
"\n"
"\n"
"#login_button{\n"
"    color: #20262E;\n"
"    background-color: #E2CFEA;\n"
"}\n"
"\n"
"#login_button:hover, #login_button:clicked{\n"
"        \n"
"    background-color: #918596\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=LoginPage)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 4, 1, 1, 1)
        self.header = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        self.header.setFont(font)
        self.header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.header.setObjectName("header")
        self.gridLayout_2.addWidget(self.header, 1, 1, 1, 1)
        self.login_pane = QtWidgets.QWidget(parent=self.centralwidget)
        self.login_pane.setMinimumSize(QtCore.QSize(0, 400))
        self.login_pane.setStyleSheet("")
        self.login_pane.setObjectName("login_pane")
        self.gridLayout = QtWidgets.QGridLayout(self.login_pane)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem4 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_name = QtWidgets.QLineEdit(parent=self.login_pane)
        self.user_name.setMinimumSize(QtCore.QSize(250, 40))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        self.user_name.setFont(font)
        self.user_name.setStyleSheet("")
        self.user_name.setObjectName("user_name")
        self.verticalLayout.addWidget(self.user_name)
        self.user_password = QtWidgets.QLineEdit(parent=self.login_pane)
        self.user_password.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(10)
        font.setBold(True)
        self.user_password.setFont(font)
        self.user_password.setInputMask("")
        self.user_password.setText("")
        self.user_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.user_password.setObjectName("user_password")
        self.verticalLayout.addWidget(self.user_password)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.login_button = QtWidgets.QPushButton(parent=self.login_pane)
        self.login_button.setEnabled(True)
        self.login_button.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("JetBrains Mono")
        font.setPointSize(15)
        font.setBold(True)
        self.login_button.setFont(font)
        self.login_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.login_button.setStyleSheet("")
        self.login_button.setObjectName("login_button")
        self.verticalLayout_2.addWidget(self.login_button)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(1, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem8, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.login_pane, 3, 1, 1, 1)
        LoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginPage)
        QtCore.QMetaObject.connectSlotsByName(LoginPage)

    def retranslateUi(self, LoginPage):
        _translate = QtCore.QCoreApplication.translate
        LoginPage.setWindowTitle(_translate("LoginPage", "MainWindow"))
        self.header.setText(_translate("LoginPage", "JEB\'S SALON"))
        self.user_name.setPlaceholderText(_translate("LoginPage", "Username"))
        self.user_password.setPlaceholderText(_translate("LoginPage", "Password"))
        self.login_button.setText(_translate("LoginPage", "LOGIN"))
