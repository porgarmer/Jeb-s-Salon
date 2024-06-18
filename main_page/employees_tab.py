from datetime import date
import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtCore import Qt, QDate, pyqtSignal
from PyQt6.QtGui import QIcon, QStandardItem, QStandardItemModel, QFont
from PyQt6.QtWidgets import QDialog, QMessageBox, QHeaderView, QTableWidgetItem, QPushButton, QWidget, QHBoxLayout
from PyQt6.uic import loadUi
from database.connect_db import Database 
from main_page import resources
from random import randint

class AddEmployee(QDialog):
    def __init__(self) -> None:
        super(AddEmployee, self).__init__()
        loadUi(r"ui_files/add_employee_dialog.ui", self)
    
        self.db = Database()
        
        
        #set focus to employee first name line edit
        self.emp_fname.setFocus()
        
        #set up services drop box
        self.set_up_services()
 
        self.emp_date_hired.setDate(QDate.currentDate())


        #employee history table
        header = self.emp_hist_table.horizontalHeader()
        self.emp_hist_table.setRowCount(0)
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.add_emp_hist_button.clicked.connect(self.show_add_emp_hist_dialog)
        self.save_emp_button.clicked.connect(self.save_employee)
        self.cancel_add_emp_button.clicked.connect(self.close)
        
    def set_up_services(self):

        self.emp_services.setModel(QStandardItemModel(self.emp_services))
        self.emp_services.view().pressed.connect(self.handle_item_pressed)
        self.emp_services.setEditable(True)
        self.emp_services.lineEdit().setReadOnly(True)
        self.emp_services.lineEdit().setAlignment(Qt.AlignmentFlag.AlignLeft)
    
    
        font = QFont("JetBrains Mono", 12)
        font.setBold(True)
        self.emp_services.lineEdit().setFont(font)
        
        placeholder_item = QStandardItem("Select services...")
        placeholder_item.setFlags(Qt.ItemFlag.NoItemFlags)
        self.emp_services.model().insertRow(0, placeholder_item)
        self.emp_services.setCurrentIndex(0)

        services = self.db.select_services()
        if services:
            for service in services:
                self.add_item(service[1])

    def handle_item_pressed(self, index):
        item = self.emp_services.model().itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)
            
    def add_item(self, service_name, checked=False):
        item = QStandardItem(service_name)
        item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        item.setData(Qt.CheckState.Checked if checked else Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        self.emp_services.model().appendRow(item)
        
    def checked_services(self):
        checked_items = []
        for index in range(self.emp_services.model().rowCount()):
            item = self.emp_services.model().item(index)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
                
        return checked_items
    
    def show_add_emp_hist_dialog(self):
        self.add_emp_hist_dialog = AddEmpHist()
        self.add_emp_hist_dialog.send_data.connect(self.display_emp_history)
        self.add_emp_hist_dialog.exec()
        

    def display_emp_history(self, emp_hist_data):
        
        self.emp_hist_table.setRowCount(self.emp_hist_table.rowCount()+1)
            
        for col, data in enumerate(emp_hist_data):
            item = QTableWidgetItem(str(data))
            self.emp_hist_table.setItem(self.emp_hist_table.rowCount()-1, col, item)
                
            action_buttons = EmpHistActionButtons()
            action_buttons.edit_button.clicked.connect(self.show_edit_emp_history)
            action_buttons.delete_button.clicked.connect(self.delete_emp_hist_value)
            
            
            self.emp_hist_table.setCellWidget(self.emp_hist_table.rowCount()-1, 4, action_buttons)
                    
    def save_employee(self):
        
        reply = QMessageBox.question(self, 'Message', 'Do you want to save this employee?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            emp_data = self.retrieve_emp_values()
            emp_hist_data = self.retrieve_emp_hist_values()
            
            self.db.add_employee(emp_data=emp_data)
            self.db.add_employee_history(emp_id=emp_data["emp_id"],emp_hist_data=emp_hist_data)
            self.db.add_employee_services(emp_id=emp_data["emp_id"], emp_services=emp_data["emp_services"])
            
            self.close() 
        else:
            print("No button pressed")
            
    def retrieve_emp_values(self):
        
        #employee information
        
        emp_fname = self.emp_fname.text().strip().capitalize()
        emp_lname = self.emp_lname.text().strip().capitalize()
        emp_minitial = self.emp_minitial.text().capitalize()
        emp_sex = self.emp_sex.currentText()
        emp_services = self.checked_services()
        emp_address = self.emp_address.text().strip()
        emp_contact_num = self.emp_contact_number.text().strip()
        emp_date_hired = self.emp_date_hired.date().toString("yyyy-MM-dd")
        emp_email_address = self.emp_email_address.text().strip()
        emp_available = self.emp_available.currentText()
        emp_id = self.generate_emp_id(emp_sex, emp_date_hired)
        
        return {"emp_id": emp_id,
                "emp_fname": emp_fname, 
                "emp_lname": emp_lname, 
                "emp_minitial": emp_minitial, 
                "emp_sex": emp_sex,
                "emp_services": emp_services,
                "emp_address": emp_address,
                "emp_contact_num": emp_contact_num,
                "emp_date_hired": emp_date_hired,
                "emp_email_address":emp_email_address,
                "emp_available": emp_available
                }
        
        
    def generate_emp_id(self, emp_sex, emp_date_hired):
  
        while True:
            if emp_sex == "Male":
                id_start_value = "M"
            else:
                id_start_value = "F"
                
            emp_date_hired = emp_date_hired.replace("-", "")
            random_number = str(randint(1,1000))
            
            generated_emp_id = id_start_value + emp_date_hired + random_number
            
            #check if generated ID exists
            emp_id_exist = self.db.check_emp_id(generated_emp_id)
            
            if not emp_id_exist:
                return generated_emp_id
            
    def retrieve_emp_hist_values(self):
        
        emp_row_data = []
        emp_hist_data = []
        
        for row in range(self.emp_hist_table.rowCount()):
            item = self.emp_hist_table.item(row, 0)
            if item:
                for col in range(self.emp_hist_table.columnCount()-1):
                    item = self.emp_hist_table.item(row, col)
                
                    emp_row_data.append(item.text())
                emp_hist_data.append(emp_row_data)
                emp_row_data = []
            
        
        return emp_hist_data
    
    def show_edit_emp_history(self):
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.emp_hist_table.rowCount()):
                widget = self.emp_hist_table.cellWidget(row, 4)
                if widget and widget.edit_button == button:
                    row_index = row
                    break
        
        self.edit_emp_hist_dialog = AddEmpHist(row=row_index)
        self.edit_emp_hist_dialog.setWindowTitle("Edit Employment History")
        self.edit_emp_hist_dialog.window_label.setText("EDIT EMPLOYMENT HISTORY")
        self.edit_emp_hist_dialog.send_data.connect(self.edit_emp_hist_value)

        
        self.edit_emp_hist_dialog.emp_hist_job_desc.setText(self.emp_hist_table.item(row, 0).text())
        self.edit_emp_hist_dialog.emp_hist_establishment.setText(self.emp_hist_table.item(row, 1).text())
        
        date_string1 = self.emp_hist_table.item(row, 2).text()
        date_format1 = "MM-dd-yyyy"
        
        date_string2 = self.emp_hist_table.item(row, 3).text()
        date_format2 = "MM-dd-yyyy"

        date_started = QDate.fromString(date_string1, date_format1)
        date_ended = QDate.fromString(date_string2, date_format2)
        
        self.edit_emp_hist_dialog.emp_hist_date_started.setDate(date_started)
        self.edit_emp_hist_dialog.emp_hist_date_ended.setDate(date_ended)

        
        self.edit_emp_hist_dialog.exec() 
        
    def edit_emp_hist_value(self, emp_hist_data, row):
        for col, data in enumerate(emp_hist_data):
            item = QTableWidgetItem(str(data))
            self.emp_hist_table.setItem(row, col, item)
                
    def delete_emp_hist_value(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to remove this row?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            
            button = self.sender()
            if button:
                # Find the index of the button
                for row in range(self.emp_hist_table.rowCount()):
                    widget = self.emp_hist_table.cellWidget(row, 4)
                    if widget and widget.delete_button == button:
                        print(row)
                        self.emp_hist_table.removeRow(row)
                        break
           
        else:
            print("No button pressen")
               
class EditEmployee(QDialog):
    
    def __init__(self, emp_id) -> None:
        super(EditEmployee, self).__init__()
        loadUi(r"ui_files/edit_employee_dialog.ui", self)

        self.db = Database()
        self.emp_id = emp_id
        
        self.setWindowTitle("Edit Employee")
        self.window_label.setText("EDIT EMPLOYEE")
        
        emp_data = self.db.select_employee(emp_id=emp_id)
        
        self.emp_fname.setText(emp_data[0])
        self.emp_minitial.setText(emp_data[1])
        self.emp_lname.setText(emp_data[2])
        self.emp_sex.setCurrentText(emp_data[3])
        self.set_up_services(emp_id=emp_id)
        self.emp_address.setText(emp_data[4])
        self.emp_contact_number.setText(emp_data[5])
        date_hired = emp_data[6].strftime("%m-%d-%Y")
        date_format = "MM-dd-yyyy"
        date_hired = QDate.fromString(date_hired, date_format)
        self.emp_date_hired.setDate(date_hired)
        self.emp_email_address.setText(emp_data[7])
        self.emp_available.setCurrentText(str(emp_data[8]))
        
        #employee history table
        header = self.emp_hist_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.populate_emp_hist_table(emp_id=emp_id)

        self.add_emp_hist_button.clicked.connect(self.show_add_emp_hist_dialog)
        self.save_emp_edit_button.clicked.connect(lambda: self.save_employee_edit(emp_id=emp_id))
        self.cancel_edit_emp_button.clicked.connect(self.close)
        
    def set_up_services(self, emp_id=None):

        self.emp_services.setModel(QStandardItemModel(self.emp_services))
        self.emp_services.view().pressed.connect(self.handle_item_pressed)
        self.emp_services.setEditable(True)
        self.emp_services.lineEdit().setReadOnly(True)
        self.emp_services.lineEdit().setAlignment(Qt.AlignmentFlag.AlignLeft)
    
    
        font = QFont("JetBrains Mono", 12)
        font.setBold(True)
        self.emp_services.lineEdit().setFont(font)
        
        placeholder_item = QStandardItem("Select services...")
        placeholder_item.setFlags(Qt.ItemFlag.NoItemFlags)
        self.emp_services.model().insertRow(0, placeholder_item)
        self.emp_services.setCurrentIndex(0)

        services = self.db.select_services()
        employee_services = self.db.select_employee_services(emp_id=emp_id, services=services)

        if services:
            for service in services:
                if service[1] in employee_services:
                    self.add_item(service[1], True)
                else:  
                    self.add_item(service[1])

    def handle_item_pressed(self, index):
        item = self.emp_services.model().itemFromIndex(index)
        if item.checkState() == Qt.CheckState.Checked:
            item.setCheckState(Qt.CheckState.Unchecked)
        else:
            item.setCheckState(Qt.CheckState.Checked)
            
    def add_item(self, service_name, checked=False):
        item = QStandardItem(service_name)
        item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
        item.setData(Qt.CheckState.Checked if checked else Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
        self.emp_services.model().appendRow(item)
        
    def checked_services(self):
        checked_items = []
        for index in range(self.emp_services.model().rowCount()):
            item = self.emp_services.model().item(index)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item.text())
                
        return checked_items
    
    def populate_emp_hist_table(self, emp_id):
        self.emp_hist_table.setRowCount(0)
        self.emp_hist_table.hideColumn(0)
        emp_hist_data = self.db.select_employment_history(emp_id=emp_id)
        
        if emp_hist_data:
            for row, row_data in enumerate(emp_hist_data):
                self.emp_hist_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, date):
                        cell_data = cell_data.strftime("%m-%d-%Y")
                    item = QTableWidgetItem(str(cell_data))
                    self.emp_hist_table.setItem(row, col, item)
                    
                action_buttons = EmpHistActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_emp_history)
                action_buttons.delete_button.clicked.connect(self.delete_emp_hist)
            
                self.emp_hist_table.setCellWidget(row, 5, action_buttons)

    def show_add_emp_hist_dialog(self):
        self.add_emp_hist_dialog = AddEmpHist()
        self.add_emp_hist_dialog.send_data.connect(self.add_emp_history)
        self.add_emp_hist_dialog.exec()
        self.populate_emp_hist_table(emp_id=self.emp_id)
        
    def add_emp_history(self, emp_hist_data):
        self.db.add_employee_history(emp_id=self.emp_id, emp_hist_data=emp_hist_data)
             
    def retrieve_emp_hist_values(self):
        
        emp_row_data = []
        emp_hist_data = []
        
        for row in range(self.emp_hist_table.rowCount()):
            item = self.emp_hist_table.item(row, 0)
            if item:
                for col in range(self.emp_hist_table.columnCount()-1):
                    item = self.emp_hist_table.item(row, col)
                
                    emp_row_data.append(item.text())
                emp_hist_data.append(emp_row_data)
                emp_row_data = []
            
        
        return emp_hist_data
    
    def show_edit_emp_history(self):
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.emp_hist_table.rowCount()):
                widget = self.emp_hist_table.cellWidget(row, 5)
                if widget and widget.edit_button == button:
                    row_index = row
                    break
        
        emp_hist_id = self.emp_hist_table.item(row_index, 0).text()
        self.edit_emp_hist_dialog = EditEmpHistDb(emp_hist_id)

        self.edit_emp_hist_dialog.emp_hist_job_desc.setText(self.emp_hist_table.item(row, 1).text())
        self.edit_emp_hist_dialog.emp_hist_establishment.setText(self.emp_hist_table.item(row, 2).text())
        
        date_string1 = self.emp_hist_table.item(row, 3).text()
        date_format1 = "MM-dd-yyyy"
        
        date_string2 = self.emp_hist_table.item(row, 4).text()
        date_format2 = "MM-dd-yyyy"

        date_started = QDate.fromString(date_string1, date_format1)
        date_ended = QDate.fromString(date_string2, date_format2)
        
        self.edit_emp_hist_dialog.emp_hist_date_started.setDate(date_started)
        self.edit_emp_hist_dialog.emp_hist_date_ended.setDate(date_ended)

        
        self.edit_emp_hist_dialog.exec() 
        
        self.populate_emp_hist_table(self.emp_id)
    
    def delete_emp_hist(self):
        reply = QMessageBox.question(self, 'Message', 'Are you sure you want to remove this record?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            
            button = self.sender()
            if button:
                # Find the index of the button
                for row in range(self.emp_hist_table.rowCount()):
                    widget = self.emp_hist_table.cellWidget(row, 5)
                    if widget and widget.delete_button == button:
                        break
            emp_hist_id = self.emp_hist_table.item(row, 0).text()
            self.db.delete_employee_history(emp_hist_id=emp_hist_id)

        else:
            print("No button pressen")
            
        self.populate_emp_hist_table(self.emp_id)
    
    def retrieve_emp_values(self):
        
        #employee information
        
        emp_fname = self.emp_fname.text().strip().capitalize()
        emp_lname = self.emp_lname.text().strip().capitalize()
        emp_minitial = self.emp_minitial.text().strip().capitalize()
        emp_sex = self.emp_sex.currentText()
        emp_services = self.checked_services()
        emp_address = self.emp_address.text().strip()
        emp_contact_num = self.emp_contact_number.text().strip()
        emp_date_hired = self.emp_date_hired.date().toString("yyyy-MM-dd")
        emp_email_address = self.emp_email_address.text().strip()
        emp_available = self.emp_available.currentText()
        return {"emp_fname": emp_fname, 
                "emp_lname": emp_lname, 
                "emp_minitial": emp_minitial, 
                "emp_sex": emp_sex,
                "emp_services": emp_services,
                "emp_address": emp_address,
                "emp_contact_num": emp_contact_num,
                "emp_date_hired": emp_date_hired,
                "emp_email_address":emp_email_address,
                "emp_available": emp_available}
        
    def save_employee_edit(self, emp_id):
        
        reply = QMessageBox.question(self, 'Message', 'Do you want to edit this employee?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            emp_data = self.retrieve_emp_values()
                
            self.db.update_employee(emp_id=emp_id, emp_data=emp_data)
            self.db.update_employee_services(emp_id=emp_id, emp_services=emp_data["emp_services"])
            
            self.close() 
        else:
            print("No button pressed")       

class MoreDetails(QDialog):
    def __init__(self, emp_id,) -> None:
        super(MoreDetails, self).__init__()
        loadUi(r"ui_files/more_emp_details_dialog.ui", self)
        
        self.db = Database()
        
        emp_data = self.db.select_employee(emp_id=emp_id)
        emp_hist_data = self.db.select_employment_history(emp_id=emp_id)
        
        self.emp_fname.setText(f"FIRST NAME: {emp_data[0]}")
        self.emp_minitial.setText(f"MIDDLE INITIAL: {emp_data[1]}")
        self.emp_lname.setText(f"LAST NAME: {emp_data[2]}")
        
        self.emp_sex.setText(f"SEX: {emp_data[3]}")
        services = self.db.select_services()
        emp_services = self.db.select_employee_services(emp_id=emp_id, services=services)

        self.emp_services.setText("SERVICES: "+ ", ".join(emp_services))
        self.emp_address.setText(f"ADDRESS: {emp_data[4]}")
        self.emp_contact_num.setText(f"CONTACT NUMBER: {emp_data[5]}")
        date_hired = emp_data[6].strftime("%m-%d-%Y")
        self.emp_date_hired.setText(f"DATE HIRED: {date_hired}")
        self.emp_email_address.setText(f"EMAIL ADDRESS: {emp_data[7]}")
        self.emp_available.setText(f"AVAILABLE: {emp_data[8]}")
        
        header = self.employment_history_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.employment_history_table.hideColumn(0)
        
        self.employment_history_table.setRowCount(0)
        for row, row_data in enumerate(emp_hist_data):
            self.employment_history_table.insertRow(row)
            for col, cell_data in enumerate(row_data):
                if isinstance(cell_data, date):
                    cell_data = cell_data.strftime("%m-%d-%Y")
                item = QTableWidgetItem(str(cell_data))
           
                self.employment_history_table.setItem(row, col, item)
            
        self.close_button.clicked.connect(self.close)

class AddEmpHist(QDialog):
    
    send_data = pyqtSignal(list, int)  # Custom signal to send data

    def __init__(self, row=None) -> None:
        super(AddEmpHist, self).__init__()
        loadUi(r"ui_files/add_employee_history_dialog.ui", self)

        self.row = row
        
        self.emp_hist_date_started.setDate(QDate.currentDate())
        self.emp_hist_date_ended.setDate(QDate.currentDate())
        
        self.save_emp_hist_button.clicked.connect(self.save_emp_hist)
        self.cancel_add_emp_hist_button.clicked.connect(self.close)
        
        
    def save_emp_hist(self):
        
        if self.row:
            reply = QMessageBox.question(self, 'Message', 'Do you want to edit this employee\'s history?', 
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                        QMessageBox.StandardButton.No)
        else: 
                                       
            
            reply = QMessageBox.question(self, 'Message', 'Do you want to add to this employee\'s history?', 
                                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                            QMessageBox.StandardButton.No)
        # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            emp_hist_data = self.retrieve_all_values()
            row = self.row
            self.send_data.emit(emp_hist_data, row)
            self.close()            
             
        else:
            print("No button pressen")
            
    def retrieve_all_values(self):
        
        emp_hist_job_desc = self.emp_hist_job_desc.text()
        emp_hist_establishment = self.emp_hist_establishment.text()
        emp_hist_date_started = self.emp_hist_date_started.date().toString("MM-dd-yyyy")
        emp_hist_date_ended = self.emp_hist_date_ended.date().toString("MM-dd-yyyy")
        
        emp_hist_data = [emp_hist_job_desc, emp_hist_establishment, emp_hist_date_started, emp_hist_date_ended]
        
        return emp_hist_data
    
class EditEmpHistDb(QDialog):
    def __init__(self, emp_hist_id=None) -> None:
        super(EditEmpHistDb, self).__init__()
        loadUi(r"ui_files/edit_employee_history_dialog.ui", self)


        self.db = Database()
        self.emp_hist_id = emp_hist_id
        
        self.emp_hist_date_started.setDate(QDate.currentDate())
        self.emp_hist_date_ended.setDate(QDate.currentDate())
        
        self.save_emp_hist_button.clicked.connect(self.save_emp_hist)
        self.cancel_add_emp_hist_button.clicked.connect(self.close)
        
        
    def save_emp_hist(self):
        
       
        reply = QMessageBox.question(self, 'Message', 'Do you want to edit this employee\'s history?', 
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                        QMessageBox.StandardButton.No)
        # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            emp_hist_data = self.retrieve_all_values()
            self.edit_emp_hist(emp_hist_data=emp_hist_data, emp_hist_id=self.emp_hist_id)
            self.close()            
             
        else:
            print("No button pressen")
            
    def retrieve_all_values(self):
        
        emp_hist_job_desc = self.emp_hist_job_desc.text()
        emp_hist_establishment = self.emp_hist_establishment.text()
        emp_hist_date_started = self.emp_hist_date_started.date().toString("MM-dd-yyyy")
        emp_hist_date_ended = self.emp_hist_date_ended.date().toString("MM-dd-yyyy")
        
        emp_hist_data = [emp_hist_job_desc, emp_hist_establishment, emp_hist_date_started, emp_hist_date_ended]
        
        return emp_hist_data
    
    def edit_emp_hist(self, emp_hist_data, emp_hist_id):
        self.db.update_employee_history(emp_hist_id=emp_hist_id, emp_hist_data=emp_hist_data)
    
class EmpHistActionButtons(QWidget):
    def __init__(self) -> None:
        super().__init__()
        
        
        layout = QHBoxLayout(self)
        
        edit_style_sheet = """QPushButton {
                background-color: #314641;  /* Background color of the buttons */
                color: #E2CFEA;              /* Text color of the buttons */
                border: none;               /* Remove button border */
                border-radius: 10px;         /* Border radius of the buttons */
                padding: 5px 15px;          /* Padding inside the buttons */
                font-size: 14px;            /* Font size of the button text */
				font-weight: bold;
}

QPushButton:hover {
                background-color: #4d5b57;  /* Background color on hover */
}
QPushButton:pressed {
                background-color: #303d39;  /* Background color on press */
}"""

        delete_style_sheet = """QPushButton {
                background-color: #820747;  /* Background color of the buttons */
                color: #E2CFEA;              /* Text color of the buttons */
                border: none;               /* Remove button border */
                border-radius: 10px;         /* Border radius of the buttons */
                padding: 5px 15px;          /* Padding inside the buttons */
                font-size: 14px;            /* Font size of the button text */
				font-weight: bold;
}

QPushButton:hover {
                background-color: #9E1966;  /* Background color on hover */
}
QPushButton:pressed {
                background-color: #601138;  /* Background color on press */
}"""

        more_details_style_sheet = """QPushButton {
                background-color: #3300cc;  /* Background color of the buttons */
                color: #E2CFEA;              /* Text color of the buttons */
                border: none;               /* Remove button border */
                border-radius: 10px;         /* Border radius of the buttons */
                padding: 5px 15px;          /* Padding inside the buttons */
                font-size: 14px;            /* Font size of the button text */
				font-weight: bold;
}

QPushButton:hover {
                background-color: #431ee2;  /* Background color on hover */
}
QPushButton:pressed {
                background-color: #381ab7;  /* Background color on press */
}"""


        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet(edit_style_sheet)
        self.edit_button.setFixedHeight(20)
        self.edit_button.setFixedWidth(40)
        self.edit_button.setCursor(Qt.CursorShape.PointingHandCursor)

        
        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet(delete_style_sheet)
        self.delete_button.setFixedHeight(20)
        self.delete_button.setFixedWidth(40)
        self.delete_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        edit_emp_icon = QIcon(r"static/icons/edit_button_light.svg")
        self.edit_button.setIcon(edit_emp_icon)
        
        delete_emp_icon = QIcon(r"static/icons/delete_button_light.svg")
        self.delete_button.setIcon(delete_emp_icon)
        
        
        
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
