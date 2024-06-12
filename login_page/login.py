import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)


from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsDropShadowEffect, QMessageBox
from PyQt6.QtGui import QColor
from PyQt6.uic import loadUi
from database.connect_db import Database

class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super(LoginPage, self).__init__()
        loadUi(r"ui_files/login_page.ui", self)
        
        #drop shadow effects
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(35)
        shadow_effect.setOffset(0, 0)
        shadow_effect.setColor(QColor(0, 0, 0, 150))

        shadow_effect_2 = QGraphicsDropShadowEffect()
        shadow_effect_2.setBlurRadius(35)
        shadow_effect_2.setOffset(0, 0)
        shadow_effect_2.setColor(QColor(0, 0, 0, 150))
        
        shadow_effect_3 = QGraphicsDropShadowEffect()
        shadow_effect_3.setBlurRadius(35)
        shadow_effect_3.setOffset(0, 0)
        shadow_effect_3.setColor(QColor(0, 0, 0, 150))

        shadow_effect_4 = QGraphicsDropShadowEffect()
        shadow_effect_4.setBlurRadius(35)
        shadow_effect_4.setOffset(0, 0)
        shadow_effect_4.setColor(QColor(0, 0, 0, 150))
        
        
        self.login_pane.setGraphicsEffect(shadow_effect)
        self.user_name.setGraphicsEffect(shadow_effect_2)
        self.user_password.setGraphicsEffect(shadow_effect_3)
        self.login_button.setGraphicsEffect(shadow_effect_4)
        
        #initialize database
        self.db = Database()
        
        
        self.login_button.clicked.connect(self.login)
        
        
        
        
    def login(self):
        
        user_name = "admin"
        user_password = "12345"
        
        user_name_input = self.user_name.text()
        user_password_input = self.user_password.text()
        if user_name_input == "" and user_password_input == "":
            QMessageBox.warning(self, " ", "Please enter username and password.")
        elif user_name != user_name_input or user_password != user_password_input:
            QMessageBox.warning(self, " ", "Wrong password or username.")
        else:
            from main_page.main_page import MainPage
            self.main_page = MainPage()
            self.main_page.show()
            self.close()



