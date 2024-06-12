import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsDropShadowEffect, QMessageBox
from PyQt6.uic import loadUi
from database.connect_db import Database
import resourcs_rc

class MainPage(QMainWindow):
    def __init__(self) -> None:
        super(MainPage, self).__init__()
        loadUi(r"test/main_test.ui", self)


        self.db = Database()
        
        self.side_bar_icon_only.setHidden(True)
        
        self.dashboard_button.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_icon_button.clicked.connect(self.switch_to_dashboard_page)
        
        self.employees_button.clicked.connect(self.switch_to_employees_page)
        self.employees_icon_button.clicked.connect(self.switch_to_employees_page)
        
        self.customers_button.clicked.connect(self.switch_to_customers_page)
        self.customers_icon_button.clicked.connect(self.switch_to_customers_page)
        
        self.services_button.clicked.connect(self.switch_to_services_page)
        self.services_icon_button.clicked.connect(self.switch_to_services_page)
        
        self.transac_history_button.clicked.connect(self.switch_to_transac_history_page)
        self.transac_history_button_2.clicked.connect(self.switch_to_transac_history_page)
        
        self.profile_button.clicked.connect(self.switch_to_profile_page)
        self.profile_icon_button.clicked.connect(self.switch_to_profile_page)

    def switch_to_dashboard_page(self):
        index = self.stackedWidget.indexOf(self.dashboard_page)
        self.stackedWidget.setCurrentIndex(0)
    
    def switch_to_employees_page(self):
        index = self.stackedWidget.indexOf(self.employees_page)
        self.stackedWidget.setCurrentIndex(1)
        
    def switch_to_customers_page(self):
        index = self.stackedWidget.indexOf(self.customers_page)
        self.stackedWidget.setCurrentIndex(2)
        
    def switch_to_services_page(self):
        index = self.stackedWidget.indexOf(self.services_page)
        self.stackedWidget.setCurrentIndex(3)
        
    def switch_to_transac_history_page(self):
        index = self.stackedWidget.indexOf(self.transaction_history_page)
        self.stackedWidget.setCurrentIndex(index)
        
    def switch_to_profile_page(self):
        index = self.stackedWidget.indexOf(self.profile_page)
        self.stackedWidget.setCurrentIndex(4)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainPage()
    
    window.show()
    app.exec()