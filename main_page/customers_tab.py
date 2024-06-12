import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtCore import Qt, QDate
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.uic import loadUi
from database.connect_db import Database
from main_page import resources


class AddCustomer(QDialog):
    def __init__(self) -> None:
        super(AddCustomer, self).__init__()
        loadUi(r"ui_files/add_customer_dialog.ui", self)
        
        self.cus_fname.setFocus()
        
        self.save_cus_button.clicked.connect(self.save_customer)
        self.cancel_add_cus_button.clicked.connect(self.close)
        
    def save_customer(self):
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this customer?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            self.retrieve_all_values()
            
            self.close() 
        else:
            print("No button pressed")
            
    def retrieve_all_values(self):
        
        #employee information
        cus_fname = self.cus_fname.text()
        cus_lname = self.cus_lname.text()
        cus_mname = self.cus_mname.text()
        cus_sex = self.cus_sex.currentText()
        cus_services_avail = ""
        cus_address = self.cus_address.text()
        cus_contact_number = self.cus_contact_number.text()
        cus_app_date_time = self.cus_app_date_time.dateTime().toString("MM-dd-yyyy h:mm AP")
        
class EditCustomer(AddCustomer):
    def __init__(self) -> None:
        super(AddCustomer, self).__init__()
        loadUi(r"ui_files/edit_customer_dialog.ui", self)
        
        self.cus_fname.setFocus()
        
        self.save_cus_edit_button.clicked.connect(self.save_customer)
        self.cancel_edit_cus_button.clicked.connect(self.close)
        
    def save_customer(self):
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this customer?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed edi")
            self.retrieve_all_values()
            
            self.close() 
        else:
            print("No button pressed edit")