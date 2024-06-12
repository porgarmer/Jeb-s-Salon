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

class AddEmployee(QDialog):
    def __init__(self) -> None:
        super(AddEmployee, self).__init__()
        loadUi(r"ui_files/add_employee_dialog.ui", self)
        
        #set focus to employee first name line edit
        self.emp_fname.setFocus()
        
        #set the dates of date edits to the current date
        self.emp_date_hired.setDate(QDate.currentDate())
        self.emp_hist_start_date.setDate(QDate.currentDate())
        self.emp_hist_end_date.setDate(QDate.currentDate())
        
        self.save_emp_button.clicked.connect(self.save_employee)
        self.cancel_add_emp_button.clicked.connect(self.close)
        
    def save_employee(self):
        
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this employee?', 
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
        emp_fname = self.emp_fname.text()
        emp_lname = self.emp_lname.text()
        emp_mname = self.emp_mname.text()
        emp_sex = self.emp_sex.currentText()
        emp_services = ""
        emp_address = self.emp_address.text()
        emp_contact_number = self.emp_contact_number.text()
        emp_date_hired = self.emp_date_hired.date().toString("MM-dd-yyyy")
        emp_email_address = self.emp_email_address.text()
        
        #employee employment history information
        emp_hist_job_desc = self.emp_hist_job_desc.text()
        emp_hist_establishment = self.emp_hist_establishment.text()
        emp_hist_start_date = self.emp_hist_start_date.date().toString("MM-dd-yyyy")
        emp_hist_end_date = self.emp_hist_end_date.date().toString("MM-dd-yyyy")
        
        
#parameter to be added: emp_details
class EditEmployee(AddEmployee):
    
    def __init__(self) -> None:
        super(AddEmployee, self).__init__()
        loadUi(r"ui_files/edit_employee_dialog.ui", self)
        
        #set focus to employee first name line edit
        self.emp_fname.setFocus()
        # self.emp_date_hired.setDate(QDate.currentDate())
        # self.emp_hist_start_date.setDate(QDate.currentDate())
        # self.emp_hist_end_date.setDate(QDate.currentDate())
        
        self.save_emp_edit_button.clicked.connect(self.save_employee)
        self.cancel_edit_emp_button.clicked.connect(self.close)
        
    def save_employee(self):
        
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this employee?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            self.retrieve_all_values()
            
            self.close() 
        else:
            print("No button pressen")
            
#parameter to be added: emp_details
class MoreDetails(QDialog):
    def __init__(self) -> None:
        super(MoreDetails, self).__init__()
        loadUi(r"ui_files/more_emp_details_dialog.ui", self)
        
        self.close_button.clicked.connect(self.close)
