import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.uic import loadUi
from database.connect_db import Database
from main_page import resources

class AddService(QDialog):
    def __init__(self) -> None:
        super(AddService, self).__init__()
        loadUi(r"ui_files/add_service_dialog.ui", self)
        
        self.db = Database()

        self.service_name.setFocus()
        
        
        self.save_service_button.clicked.connect(self.save_service)
        self.cancel_add_service_button.clicked.connect(self.close)
        
    def save_service(self):
        
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this service?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            service_data = self.retrieve_all_values()
            if service_data:
                self.db.add_service(service_data=service_data)
                self.db.create_service_table(service_name=service_data[0])
                self.close() 
        else:
            print("No button pressed")
            
    def retrieve_all_values(self):
        
        service_name = self.service_name.text().lower().strip()
        service_price = self.service_price.value()

        if service_name == "":
            QMessageBox.warning(self, "Warning", "Please fill out the service name.")
        else:
            return [service_name, service_price]

class EditService(QDialog):
    
    def __init__(self, service_id, old_service_name) -> None:
        super(EditService, self).__init__()
        loadUi(r"ui_files/edit_service_dialog.ui", self)
        
        self.db = Database()
        self.service_id = service_id
        self.old_service_name = old_service_name
        
        self.save_service_button.clicked.connect(self.save_employee)
        self.cancel_edit_service_button.clicked.connect(self.close)
        
    def save_employee(self):
        
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this service?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed edit")
            service_data = self.retrieve_all_values()
            if service_data:
                self.db.update_service(old_service_name=self.old_service_name, service_id=self.service_id, service_data=service_data)
                
                self.close() 
        else:
            print("No button pressen edit")
            
            
    def retrieve_all_values(self):
        
        service_name = self.service_name.text().lower().strip()
        service_price = self.service_price.value()
        
        if service_name == "":
            QMessageBox.warning(self, "Warning", "Please fill out the service name.")
        else:
            return [service_name, service_price]