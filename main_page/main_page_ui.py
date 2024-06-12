# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)
import resourcs_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1234, 838)
        font = QFont()
        font.setPointSize(20)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"#main_screen{\n"
"    background-color: #20262E;\n"
"}\n"
"\n"
"#side_bar, #side_bar_icon_only{\n"
"    background-color: #5A2E74;\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: center;\n"
"	color: #E9E8E8;\n"
"	box-shadow: none;\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"	color: #E9E8E8;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.side_bar_icon_only = QWidget(self.centralwidget)
        self.side_bar_icon_only.setObjectName(u"side_bar_icon_only")
        self.side_bar_icon_only.setStyleSheet(u"QLabel{\n"
"	padding-right: 5px;\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #E2CFEA;\n"
"	color: #2C2C3B;\n"
"}")
        self.gridLayout = QGridLayout(self.side_bar_icon_only)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, -1, 9, -1)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.label = QLabel(self.side_bar_icon_only)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"JetBrains Mono"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_6.addWidget(self.label)

        self.verticalSpacer_4 = QSpacerItem(20, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(50)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.dashboard_icon_button = QPushButton(self.side_bar_icon_only)
        self.dashboard_icon_button.setObjectName(u"dashboard_icon_button")
        self.dashboard_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboard_icon_button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/dashboard_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/dashboard_dark.svg", QSize(), QIcon.Normal, QIcon.On)
        self.dashboard_icon_button.setIcon(icon)
        self.dashboard_icon_button.setIconSize(QSize(30, 30))
        self.dashboard_icon_button.setCheckable(True)
        self.dashboard_icon_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.dashboard_icon_button)

        self.employees_icon_button = QPushButton(self.side_bar_icon_only)
        self.employees_icon_button.setObjectName(u"employees_icon_button")
        self.employees_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/employees_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/employees_dark.svg", QSize(), QIcon.Normal, QIcon.On)
        self.employees_icon_button.setIcon(icon1)
        self.employees_icon_button.setIconSize(QSize(30, 30))
        self.employees_icon_button.setCheckable(True)
        self.employees_icon_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.employees_icon_button)

        self.customers_icon_button = QPushButton(self.side_bar_icon_only)
        self.customers_icon_button.setObjectName(u"customers_icon_button")
        self.customers_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/customers_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/customers_dark.svg", QSize(), QIcon.Normal, QIcon.On)
        self.customers_icon_button.setIcon(icon2)
        self.customers_icon_button.setIconSize(QSize(30, 30))
        self.customers_icon_button.setCheckable(True)
        self.customers_icon_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.customers_icon_button)

        self.services_icon_button = QPushButton(self.side_bar_icon_only)
        self.services_icon_button.setObjectName(u"services_icon_button")
        self.services_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/services_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/services_dark.svg", QSize(), QIcon.Normal, QIcon.On)
        self.services_icon_button.setIcon(icon3)
        self.services_icon_button.setIconSize(QSize(30, 30))
        self.services_icon_button.setCheckable(True)
        self.services_icon_button.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.services_icon_button)

        self.transac_history_button_2 = QPushButton(self.side_bar_icon_only)
        self.transac_history_button_2.setObjectName(u"transac_history_button_2")
        self.transac_history_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/receipt_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/receipt_dark.svg", QSize(), QIcon.Normal, QIcon.On)
        self.transac_history_button_2.setIcon(icon4)
        self.transac_history_button_2.setIconSize(QSize(30, 30))
        self.transac_history_button_2.setCheckable(True)
        self.transac_history_button_2.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.transac_history_button_2)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 168, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.profile_icon_button = QPushButton(self.side_bar_icon_only)
        self.profile_icon_button.setObjectName(u"profile_icon_button")
        self.profile_icon_button.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/admin_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u":/admin_dark.svg", QSize(), QIcon.Normal, QIcon.On)
        self.profile_icon_button.setIcon(icon5)
        self.profile_icon_button.setIconSize(QSize(40, 40))
        self.profile_icon_button.setCheckable(True)
        self.profile_icon_button.setAutoExclusive(True)

        self.verticalLayout_5.addWidget(self.profile_icon_button)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_5, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.side_bar_icon_only, 0, 0, 1, 1)

        self.side_bar = QWidget(self.centralwidget)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setStyleSheet(u"QLabel{\n"
"	padding-left: 5px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	text-align: left;\n"
"	padding-left: 10px;\n"
"	padding-right: 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: #E2CFEA;\n"
"	color: #2C2C3B;\n"
"}")
        self.verticalLayout_15 = QVBoxLayout(self.side_bar)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, -1, 0, -1)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 10, -1, -1)
        self.label_4 = QLabel(self.side_bar)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_12.addWidget(self.label_4)

        self.verticalSpacer_14 = QSpacerItem(20, 78, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_14)


        self.verticalLayout_15.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(50)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.dashboard_button = QPushButton(self.side_bar)
        self.dashboard_button.setObjectName(u"dashboard_button")
        font2 = QFont()
        font2.setFamilies([u"JetBrains Mono"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.dashboard_button.setFont(font2)
        self.dashboard_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.dashboard_button.setStyleSheet(u"")
        self.dashboard_button.setIcon(icon)
        self.dashboard_button.setIconSize(QSize(30, 30))
        self.dashboard_button.setCheckable(True)
        self.dashboard_button.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.dashboard_button)

        self.employees_button = QPushButton(self.side_bar)
        self.employees_button.setObjectName(u"employees_button")
        self.employees_button.setFont(font2)
        self.employees_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.employees_button.setIcon(icon1)
        self.employees_button.setIconSize(QSize(30, 30))
        self.employees_button.setCheckable(True)
        self.employees_button.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.employees_button)

        self.customers_button = QPushButton(self.side_bar)
        self.customers_button.setObjectName(u"customers_button")
        self.customers_button.setFont(font2)
        self.customers_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.customers_button.setIcon(icon2)
        self.customers_button.setIconSize(QSize(30, 30))
        self.customers_button.setCheckable(True)
        self.customers_button.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.customers_button)

        self.services_button = QPushButton(self.side_bar)
        self.services_button.setObjectName(u"services_button")
        self.services_button.setFont(font2)
        self.services_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.services_button.setIcon(icon3)
        self.services_button.setIconSize(QSize(30, 30))
        self.services_button.setCheckable(True)
        self.services_button.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.services_button)

        self.transac_history_button = QPushButton(self.side_bar)
        self.transac_history_button.setObjectName(u"transac_history_button")
        font3 = QFont()
        font3.setFamilies([u"JetBrains Mono"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.transac_history_button.setFont(font3)
        self.transac_history_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.transac_history_button.setIcon(icon4)
        self.transac_history_button.setIconSize(QSize(30, 30))
        self.transac_history_button.setCheckable(True)
        self.transac_history_button.setAutoExclusive(True)

        self.verticalLayout_13.addWidget(self.transac_history_button)


        self.verticalLayout_15.addLayout(self.verticalLayout_13)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_15 = QSpacerItem(20, 168, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_15)

        self.profile_button = QPushButton(self.side_bar)
        self.profile_button.setObjectName(u"profile_button")
        font4 = QFont()
        font4.setFamilies([u"JetBrains Mono"])
        font4.setPointSize(13)
        font4.setBold(True)
        self.profile_button.setFont(font4)
        self.profile_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.profile_button.setIcon(icon5)
        self.profile_button.setIconSize(QSize(40, 40))
        self.profile_button.setCheckable(True)
        self.profile_button.setChecked(False)
        self.profile_button.setAutoExclusive(True)

        self.verticalLayout_14.addWidget(self.profile_button)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_16)


        self.verticalLayout_15.addLayout(self.verticalLayout_14)


        self.gridLayout_2.addWidget(self.side_bar, 0, 1, 1, 1)

        self.main_screen = QWidget(self.centralwidget)
        self.main_screen.setObjectName(u"main_screen")
        self.verticalLayout_16 = QVBoxLayout(self.main_screen)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, -1, 0, -1)
        self.header_widget = QWidget(self.main_screen)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_12 = QPushButton(self.header_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/menu_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon6)
        self.pushButton_12.setIconSize(QSize(30, 30))
        self.pushButton_12.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton_12)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_16.addWidget(self.header_widget)

        self.stackedWidget = QStackedWidget(self.main_screen)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: #20262E;")
        self.dashboard_page = QWidget()
        self.dashboard_page.setObjectName(u"dashboard_page")
        self.label_2 = QLabel(self.dashboard_page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 210, 351, 231))
        font5 = QFont()
        font5.setFamilies([u"JetBrains Mono"])
        font5.setPointSize(50)
        font5.setBold(True)
        self.label_2.setFont(font5)
        self.stackedWidget.addWidget(self.dashboard_page)
        self.employees_page = QWidget()
        self.employees_page.setObjectName(u"employees_page")
        self.label_3 = QLabel(self.employees_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 190, 351, 231))
        self.label_3.setFont(font5)
        self.stackedWidget.addWidget(self.employees_page)
        self.customers_page = QWidget()
        self.customers_page.setObjectName(u"customers_page")
        self.label_5 = QLabel(self.customers_page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 210, 351, 231))
        self.label_5.setFont(font5)
        self.stackedWidget.addWidget(self.customers_page)
        self.services_page = QWidget()
        self.services_page.setObjectName(u"services_page")
        self.label_6 = QLabel(self.services_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(290, 210, 321, 231))
        self.label_6.setFont(font5)
        self.stackedWidget.addWidget(self.services_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.label_8 = QLabel(self.profile_page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 240, 281, 231))
        self.label_8.setFont(font5)
        self.stackedWidget.addWidget(self.profile_page)
        self.transaction_history_page = QWidget()
        self.transaction_history_page.setObjectName(u"transaction_history_page")
        self.label_7 = QLabel(self.transaction_history_page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(90, 210, 731, 291))
        self.label_7.setFont(font5)
        self.stackedWidget.addWidget(self.transaction_history_page)

        self.verticalLayout_16.addWidget(self.stackedWidget)

        self.footer_widget = QWidget(self.main_screen)
        self.footer_widget.setObjectName(u"footer_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.footer_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(858, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.pushButton_13 = QPushButton(self.footer_widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/sign_out_light.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon7)
        self.pushButton_13.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.pushButton_13)


        self.verticalLayout_16.addWidget(self.footer_widget)


        self.gridLayout_2.addWidget(self.main_screen, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_12.toggled.connect(self.side_bar_icon_only.setHidden)
        self.pushButton_12.toggled.connect(self.side_bar.setVisible)
        self.transac_history_button_2.toggled.connect(self.transac_history_button.setChecked)
        self.services_icon_button.toggled.connect(self.services_button.setChecked)
        self.customers_icon_button.toggled.connect(self.customers_button.setChecked)
        self.employees_icon_button.toggled.connect(self.employees_button.setChecked)
        self.dashboard_icon_button.toggled.connect(self.dashboard_button.setChecked)
        self.profile_icon_button.toggled.connect(self.profile_button.setChecked)
        self.dashboard_button.toggled.connect(self.dashboard_icon_button.setChecked)
        self.employees_button.toggled.connect(self.employees_icon_button.setChecked)
        self.customers_button.toggled.connect(self.customers_icon_button.setChecked)
        self.services_button.toggled.connect(self.services_icon_button.setChecked)
        self.transac_history_button.toggled.connect(self.transac_history_button_2.setChecked)
        self.profile_button.toggled.connect(self.profile_icon_button.setChecked)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"JEB'S", None))
        self.dashboard_icon_button.setText("")
        self.employees_icon_button.setText("")
        self.customers_icon_button.setText("")
        self.services_icon_button.setText("")
        self.transac_history_button_2.setText("")
        self.profile_icon_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"JEB'S SALON", None))
        self.dashboard_button.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.employees_button.setText(QCoreApplication.translate("MainWindow", u"EMPLOYEES", None))
        self.customers_button.setText(QCoreApplication.translate("MainWindow", u"CUSTOMERS", None))
        self.services_button.setText(QCoreApplication.translate("MainWindow", u"SERVICES", None))
        self.transac_history_button.setText(QCoreApplication.translate("MainWindow", u"TRANSACTION HISTORY", None))
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"HELLO, ADMIN", None))
        self.pushButton_12.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"EMPLOYEES", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"CUSTOMERS", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"SERVICES", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"TRANSCTION HISTORY", None))
        self.pushButton_13.setText("")
    # retranslateUi

