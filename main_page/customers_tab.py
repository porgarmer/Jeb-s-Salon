from random import randint
import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtCore import Qt, QDate, QDateTime
from PyQt6.QtWidgets import QDialog, QMessageBox, QHeaderView
from PyQt6.uic import loadUi
from database.connect_db import Database
from main_page import resources


class AddCustomer(QDialog):
    def __init__(self) -> None:
        super(AddCustomer, self).__init__()
        loadUi(r"ui_files/add_customer_dialog.ui", self)
        
        self.db = Database()
        
        self.cus_fname.setFocus()
        self.set_up_services()
        self.cus_service_availed.currentIndexChanged.connect(self.set_up_employees)
        
        self.cus_app_date_time.setDateTime(QDateTime.currentDateTime())
        
        self.save_cus_button.clicked.connect(self.save_customer)
        self.cancel_add_cus_button.clicked.connect(self.close)
        
    def save_customer(self):
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this customer?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            cus_values = self.retrieve_all_values()
            self.db.add_customer(cus_data=cus_values["cus_data"], app_data=cus_values["cus_app_data"])
            # self.db.add_customer_appointment(app_data=cus_values["cus_app_data"])
            
            self.close() 
        else:
            print("No button pressed")
            
    def retrieve_all_values(self):
        
        #employee information
        cus_fname = self.cus_fname.text().strip().capitalize()
        cus_minitial = self.cus_minitial.text().strip().capitalize()
        cus_lname = self.cus_lname.text().strip().capitalize()
        cus_sex = self.cus_sex.currentText()
        cus_service_availed = self.cus_service_availed.currentText()
        cus_contact_number = self.cus_contact_number.text().strip()
        
        #appointment data
        cus_app_date = self.cus_app_date_time.date().toString("MM-dd-yyyy")
        cus_app_time = self.cus_app_date_time.time().toString("h:mm AP")
        cus_employee_assigned = self.cus_employee_assigned.currentText()
        
        cus_id = self.generate_cus_id(cus_app_date)
        
        return{"cus_data": [cus_id, cus_fname, cus_minitial, cus_lname, cus_contact_number, cus_sex],
               "cus_app_data": [cus_app_date, cus_app_time, cus_id, cus_service_availed, cus_employee_assigned]
               }
        
    def generate_cus_id(self, cus_app_date):

        while True:
            cus_app_date = cus_app_date.replace("-", "")
            random_number = str(randint(1,1000))
            
            generated_cus_id =  cus_app_date + random_number
            
            #check if generated ID exists
            cus_id_exist = self.db.check_cus_id(generated_cus_id)
            
            if not cus_id_exist:
                return generated_cus_id
            
            
    def set_up_services(self):
        services = self.db.select_services()
        if services:
            for service in services:
                self.cus_service_availed.addItem(service[1])
                
    def set_up_employees(self, index):
        self.cus_employee_assigned.clear()
        selected_service = self.cus_service_availed.itemText(index) 
        available_employees = self.db.select_available_employees_by_service(service_name=selected_service)
        
        if available_employees:
            for employee in available_employees:
                self.cus_employee_assigned.addItem(f"{employee[1]} {employee[3]}")
        
class EditCustomer(QDialog):
    def __init__(self, cus_id, app_id) -> None:
        super(EditCustomer, self).__init__()
        loadUi(r"ui_files/edit_customer_dialog.ui", self)
        
        self.cus_id = cus_id
        self.app_id = app_id
        
        self.db = Database()
        
        self.cus_fname.setFocus()

        customer_data = self.db.select_customer(app_id=app_id)
        
        self.cus_fname.setText(customer_data[0])
        self.cus_minitial.setText(customer_data[1].replace(" ", ""))
        self.cus_lname.setText(customer_data[2])
        self.cus_sex.setCurrentText(customer_data[3])
        self.set_up_services()
        self.cus_service_availed.setCurrentText(customer_data[4])
        self.cus_contact_number.setText(customer_data[5])
        self.cus_app_date_time.setDateTime(customer_data[6])
        self.set_up_employees(self.cus_service_availed.currentIndex())
        self.cus_employee_assigned.setCurrentText(customer_data[7])
        
        self.cus_service_availed.currentIndexChanged.connect(self.set_up_employees)
        self.save_cus_edit_button.clicked.connect(self.save_customer)
        self.cancel_edit_cus_button.clicked.connect(self.close)
        
    def save_customer(self):
        reply = QMessageBox.question(self, 'Message', 'Do you want to edit this customer?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed edit")
            
            cus_values = self.retrieve_all_values()
            self.db.update_customer(cus_id=self.cus_id, cus_data=cus_values["cus_data"], app_id=self.app_id, app_data=cus_values["cus_app_data"])
            # self.db.udpate_customer_appointment()
            self.close() 
        else:
            print("No button pressed edit")
            
            
    def retrieve_all_values(self):
        
        #employee information
        cus_fname = self.cus_fname.text().strip().capitalize()
        cus_minitial = self.cus_minitial.text().strip().capitalize()
        cus_lname = self.cus_lname.text().strip().capitalize()
        cus_sex = self.cus_sex.currentText()
        cus_service_availed = self.cus_service_availed.currentText()
        cus_contact_number = self.cus_contact_number.text().strip()
        
        #appointment data
        cus_app_date = self.cus_app_date_time.date().toString("MM-dd-yyyy")
        cus_app_time = self.cus_app_date_time.time().toString("h:mm AP")
        cus_employee_assigned = self.cus_employee_assigned.currentText()
                
        return{"cus_data": [cus_fname, cus_minitial, cus_lname, cus_contact_number, cus_sex],
               "cus_app_data": [cus_app_date, cus_app_time, cus_service_availed, cus_employee_assigned]
               }
        
    def set_up_services(self):
        services = self.db.select_services()
        if services:
            for service in services:
                self.cus_service_availed.addItem(service[1])
        
        
    def set_up_employees(self, index):
        self.cus_employee_assigned.clear()
        selected_service = self.cus_service_availed.itemText(index) 
        available_employees = self.db.select_available_employees_by_service(service_name=selected_service)
        
        if available_employees:
            for employee in available_employees:
                self.cus_employee_assigned.addItem(f"{employee[1]} {employee[3]}")
                
class MoreDetails(QDialog):
    def __init__(self) -> None:
        super(MoreDetails, self).__init__()
        loadUi(r"ui_files/more_cus_details_dialog.ui", self)
        
        header = self.services_availed_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        self.close_button.clicked.connect(self.close)
