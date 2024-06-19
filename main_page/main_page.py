import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtCore import Qt, QDateTime, QTimer
from PyQt6.QtWidgets import QMainWindow, QHeaderView, QGraphicsBlurEffect, QMessageBox, QPushButton, QWidget, QHBoxLayout, QGridLayout, QVBoxLayout, QTableWidgetItem
from PyQt6.QtGui import QIcon, QStandardItem, QStandardItemModel, QFont
from PyQt6.uic import loadUi
from main_page import resources
from database.connect_db import Database
from datetime import datetime, date

class MainPage(QMainWindow):
    def __init__(self) -> None:
        super(MainPage, self).__init__()
        loadUi(r"ui_files/main.ui", self)
        
        self.db = Database()
        
        self.side_bar_icon_only.setHidden(True)
        self.switch_to_dashboard_page()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000) 
        
        self.update_date_time()
        
        self.dashboard_button.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_icon_button.clicked.connect(self.switch_to_dashboard_page)
        
        self.delete_all_emp_button.clicked.connect(self.delete_all_employees)
        self.employees_button.clicked.connect(self.switch_to_employees_page)
        self.employees_icon_button.clicked.connect(self.switch_to_employees_page)
        self.populate_employees_table()
        
        self.customers_button.clicked.connect(self.switch_to_customers_page)
        self.customers_icon_button.clicked.connect(self.switch_to_customers_page)
        self.populate_customers_table()
        
        
        self.services_button.clicked.connect(self.switch_to_services_page)
        self.services_icon_button.clicked.connect(self.switch_to_services_page)
        self.refresh_button.clicked.connect(self.filter_by_service)
        self.remove_service_filter_button.clicked.connect(self.remove_service_filter)
        self.set_up_services()
        self.populate_services_table()
        self.populate_available_employees()

        self.transac_history_button.clicked.connect(self.switch_to_transac_history_page)
        self.transac_history_button_2.clicked.connect(self.switch_to_transac_history_page)
        self.populate_transac_table()
        
        self.profile_button.clicked.connect(self.switch_to_profile_page)
        self.profile_icon_button.clicked.connect(self.switch_to_profile_page)

        self.logout_button.clicked.connect(self.logout)
        
        
        
        ### employees tab button links ###
        self.add_emp_button.clicked.connect(self.show_add_employee_dialog)
        # self.delete_all_emp_button.clicked.connect(self.)

        
        
        ### customers tab button links ###
        self.add_cus_button.clicked.connect(self.show_add_customer_dialog)
        # self.delete_all_cus_button.clicked.connect(self.)
        
        ### services tab button links
        self.add_new_service_button.clicked.connect(self.show_add_service_dialog)

    def update_date_time(self):
        # Get the current time and format it as a string
        current_date_time = QDateTime.currentDateTime()
        time_string = current_date_time.toString('MMMM dd, yyyy hh:mm:ss: AP')
        # Update the QLabel with the formatted time string
        self.current_date_time.setText(time_string)

    ### tab switching functions ###
    def switch_to_dashboard_page(self):
        index = self.stackedWidget.indexOf(self.dashboard_page)
        self.stackedWidget.setCurrentIndex(index)
    
    def switch_to_employees_page(self):
        index = self.stackedWidget.indexOf(self.employees_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.emp_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                
    def switch_to_customers_page(self):
        index = self.stackedWidget.indexOf(self.customers_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.cus_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
    def switch_to_services_page(self):
        index = self.stackedWidget.indexOf(self.services_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.services_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header2 = self.available_employees_table.horizontalHeader()
        header2.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
    def switch_to_transac_history_page(self):
        index = self.stackedWidget.indexOf(self.transaction_history_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.transac_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
    def switch_to_profile_page(self):
        index = self.stackedWidget.indexOf(self.profile_page)
        self.stackedWidget.setCurrentIndex(index)
        
    def reset_blur_effect(self):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(0)
        self.setGraphicsEffect(blur_effect)
    
    def logout(self):
        from login_page.login import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()
        
######## Functions for the employees tab#########

    def populate_employees_table(self):
        
        self.employees = self.db.select_all_employees()
        self.emp_table.setRowCount(0)
        self.emp_table.hideColumn(0)
        
        for row, row_data in enumerate(self.employees):
            self.emp_table.insertRow(row)
            for col, cell_data in enumerate(row_data):
                if isinstance(cell_data, date):
                    cell_data = cell_data.strftime("%m-%d-%Y")
                item = QTableWidgetItem(str(cell_data))
           
                self.emp_table.setItem(row, col, item)
            
                #actions buttons
            action_buttons = ActionButtons()
            action_buttons.edit_button.clicked.connect(self.show_edit_employee_dialog)
            action_buttons.delete_button.clicked.connect(self.delete_employee)
            action_buttons.more_details_button.clicked.connect(self.more_emp_details)
            self.emp_table.setCellWidget(row, 8, action_buttons)

    def show_add_employee_dialog(self):
        from main_page.employees_tab import AddEmployee
        
        self.add_employee_dialog = AddEmployee()
        
        #Blur effect for the main window
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
    
        self.add_employee_dialog.finished.connect(self.reset_blur_effect) 
        self.add_employee_dialog.exec()

        self.populate_employees_table()
                
    def show_edit_employee_dialog(self):
        from main_page.employees_tab import EditEmployee
        
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.emp_table.rowCount()):
                widget = self.emp_table.cellWidget(row, 8)
                if widget and widget.edit_button == button:
                    row_index = row
                    break
                
        emp_id = self.emp_table.item(row_index, 0).text()
        
        self.edit_employee_dialog = EditEmployee(emp_id=emp_id)
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
        
        self.edit_employee_dialog.finished.connect(self.reset_blur_effect) 
        self.edit_employee_dialog.exec()
        
        self.populate_employees_table()
   
    def delete_employee(self): 
        
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.emp_table.rowCount()):
                widget = self.emp_table.cellWidget(row, 8)
                if widget and widget.delete_button == button:
                    row_index = row
                    break
                
        reply = QMessageBox.warning(self, 'Message', 'Are you sure you want to delete this employee?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
            emp_id = self.emp_table.item(row_index, 0).text()
            self.db.delete_employee(emp_id=emp_id)
            self.populate_employees_table()
        else:
            print("No button pressed")
        
    def more_emp_details(self):
        from main_page.employees_tab import MoreDetails

        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.emp_table.rowCount()):
                widget = self.emp_table.cellWidget(row, 8)
                if widget and widget.more_details_button == button:
                    row_index = row
                    break
                
        emp_id = self.emp_table.item(row_index, 0).text()
        
        self.more_details_dialog = MoreDetails(emp_id=emp_id)
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
        
        self.more_details_dialog.finished.connect(self.reset_blur_effect) 
        self.more_details_dialog.exec()
            
    def delete_all_employees(self):
        reply = QMessageBox.critical(self, "!!!!", "ARE YOU SURE YOU WANT TO DELETE ALL EMPLOYEES?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel, defaultButton=QMessageBox.StandardButton.Cancel)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_all_employees()
            QMessageBox.information(self, "Successful", "Successfully deleted all employees", 
                                    QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
            
        self.populate_employees_table()
######## Functions for the customers tab#########
    def populate_customers_table(self):
        self.customers = self.db.select_all_customers()
        self.cus_table.setRowCount(0)
        self.cus_table.hideColumn(0)
        self.cus_table.hideColumn(1)

        if self.customers:
            for row, row_data in enumerate(self.customers):
                self.cus_table.insertRow(row)
                for col, cell_data in enumerate(row_data):  
                    if isinstance(cell_data, datetime):
                        cell_data = cell_data.strftime("%m-%d-%Y %I:%M %p")
                    item = QTableWidgetItem(str(cell_data))
            
                        
                    self.cus_table.setItem(row, col, item)
                
                #actions buttons
                action_buttons = CustomerActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_customer_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_customer)
                action_buttons.appointment_done_button.clicked.connect(self.appointment_done)
                self.cus_table.setCellWidget(row, 8, action_buttons)

    def show_add_customer_dialog(self):
        from main_page.customers_tab import AddCustomer
        
        self.add_customer_dialog = AddCustomer()
        
        #Blur effect for the main window
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
    
        self.add_customer_dialog.finished.connect(self.reset_blur_effect) 
        self.add_customer_dialog.exec()

        self.populate_customers_table()
        
    def show_edit_customer_dialog(self):
        from main_page.customers_tab import EditCustomer
        
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.cus_table.rowCount()):
                widget = self.cus_table.cellWidget(row, 8)
                if widget and widget.edit_button == button:
                    row_index = row
                    break
        
        cus_id = self.cus_table.item(row_index, 0).text()
        app_id = self.cus_table.item(row_index, 1).text()
        
        self.edit_customer_dialog = EditCustomer(cus_id=cus_id, app_id=app_id)
        
        #Blur effect for the main window
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
    
        self.edit_customer_dialog.finished.connect(self.reset_blur_effect) 
        self.edit_customer_dialog.exec()
        
        self.populate_customers_table()

    def delete_customer(self): 
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.cus_table.rowCount()):
                widget = self.cus_table.cellWidget(row, 8)
                if widget and widget.delete_button == button:
                    break
                
        cus_id = self.cus_table.item(row, 0).text()
        
        reply = QMessageBox.warning(self, 'Message', 'Are you sure you want to delete this customer?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_customer(cus_id=cus_id)
            print("Yes button pressed")
        else:
            print("No button pressed")

        self.populate_customers_table()
   
    def appointment_done(self):
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.cus_table.rowCount()):
                widget = self.cus_table.cellWidget(row, 8)
                if widget and widget.appointment_done_button == button:
                    break
        cus_id = self.cus_table.item(row, 0).text()
        app_id = self.cus_table.item(row, 1).text()
        reply = QMessageBox.warning(self, 'Message', 'Is this appointment done?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            self.db.complete_cus_app(app_id=app_id, cus_id=cus_id)
            print("Yes button pressed")
            self.populate_transac_table()
        else:
            print("No button pressed")

        self.populate_customers_table()
        
######## Functions for the services tab#########

    def populate_services_table(self):
        self.services = self.db.select_services()
        self.services_table.setRowCount(0)
        self.services_table.hideColumn(0)

        if self.services:
            for row, row_data in enumerate(self.services):
                self.services_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
            
                    self.services_table.setItem(row, col, item)
                
                #actions buttons
                action_buttons = ServicesActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_service_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_service)
                self.services_table.setCellWidget(row, 3, action_buttons)

    def show_add_service_dialog(self):
        from main_page.services_tab import AddService
        
        self.add_service_dialog = AddService()
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
        
        self.add_service_dialog.finished.connect(self.reset_blur_effect) 
        self.add_service_dialog.exec()
        
        self.populate_services_table()
        self.set_up_services()

    def show_edit_service_dialog(self):
        
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.services_table.rowCount()):
                widget = self.services_table.cellWidget(row, 3)
                if widget and widget.edit_button == button:
                    break
                
        from main_page.services_tab import EditService
        
        service_id = self.services_table.item(row,0).text()
        self.edit_service_dialog = EditService(service_id=service_id)
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
        self.edit_service_dialog.service_name.setText(self.services_table.item(row,1).text())
        self.edit_service_dialog.service_price.setValue(float(self.services_table.item(row,2).text()))

        self.edit_service_dialog.finished.connect(self.reset_blur_effect) 
        self.edit_service_dialog.exec()

        self.populate_services_table()
        self.set_up_services()
        
    def delete_service(self):
        
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.services_table.rowCount()):
                widget = self.services_table.cellWidget(row, 3)
                if widget and widget.delete_button == button:
                    break
                
        reply = QMessageBox.warning(self, 'Message', 'Are you sure you want to delete this service?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            
            service_name = self.services_table.item(row, 1).text()
            
            self.db.delete_service(service_name=service_name)
            self.db.delete_service_table(service_name=service_name)
            
            print("Yes button pressed")
        else:
            print("No button pressed")
            
        self.populate_services_table()
        self.set_up_services()
        
    def populate_available_employees(self):
        self.available_employee_header.setText("AVAILABLE EMPLOYEES - ALL")
        all_available_employees = self.db.select_all_available_employees()
        self.available_employees_table.setRowCount(0)
        self.available_employees_table.hideColumn(0)

        if all_available_employees:
            for row, row_data in enumerate(all_available_employees):
                self.available_employees_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
            
                    self.available_employees_table.setItem(row, col, item)
        
    def filter_by_service(self):
        service_filter = self.service_filter.currentText()
        if service_filter:
            self.filter_service_table(service_filter=service_filter)
            self.filter_available_employees_table(service_filter=service_filter)
        
    def filter_service_table(self, service_filter):
        self.services_table.setRowCount(0)
        self.services_table.hideColumn(0)
        
        filtered_service = self.db.select_service_by_name(service_name=service_filter)
        
        if filtered_service:
            for row, row_data in enumerate(filtered_service):
                self.services_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                
                    self.services_table.setItem(row, col, item)
                
                #actions buttons
                action_buttons = ServicesActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_service_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_service)
                self.services_table.setCellWidget(row, 3, action_buttons)
        
    def filter_available_employees_table(self, service_filter):
        
        filtered_available_employees = self.db.select_available_employees_by_service(service_name=service_filter)
        self.available_employee_header.setText(f"AVAILABLE EMPLOYEES - {service_filter.upper()}")
        
        self.available_employees_table.setRowCount(0)
        self.available_employees_table.hideColumn(0)

        if filtered_available_employees:
            for row, row_data in enumerate(filtered_available_employees):
                self.available_employees_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
            
                    self.available_employees_table.setItem(row, col, item)

    def remove_service_filter(self):
        self.populate_services_table()
        self.populate_available_employees()
        self.set_up_services()
        
    def set_up_services(self):
        self.service_filter.clear()
        self.service_filter.setPlaceholderText("FILTER BY SERVICE")
        services = self.db.select_services()
        if services:
            for service in services:
                self.service_filter.addItem(service[1])

######## Functions for the transactions tab#########

    def populate_transac_table(self):
        self.transactions = self.db.select_all_transac()
        self.transac_table.setRowCount(0)
        self.transac_table.hideColumn(0)

        if self.transactions:
            for row, row_data in enumerate(self.transactions):
                self.transac_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, datetime):
                        cell_data = cell_data.strftime("%m-%d-%Y %I:%M %p")
                    item = QTableWidgetItem(str(cell_data))
            
                    self.transac_table.setItem(row, col, item)
                
class ActionButtons(QWidget):
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
        
        self.more_details_button = QPushButton("", self)
        self.more_details_button.setStyleSheet(more_details_style_sheet)
        self.more_details_button.setFixedHeight(20)
        self.more_details_button.setFixedWidth(40)
        self.more_details_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        edit_emp_icon = QIcon(r"static/icons/edit_button_light.svg")
        self.edit_button.setIcon(edit_emp_icon)
        
        delete_emp_icon = QIcon(r"static/icons/delete_button_light.svg")
        self.delete_button.setIcon(delete_emp_icon)
        
        more_details_icon = QIcon(r"static/icons/more_details_button_light.svg")
        self.more_details_button.setIcon(more_details_icon)
        
        
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.more_details_button)
        
class CustomerActionButtons(QWidget):
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
        
        self.appointment_done_button = QPushButton("", self)
        self.appointment_done_button.setStyleSheet(more_details_style_sheet)
        self.appointment_done_button.setFixedHeight(20)
        self.appointment_done_button.setFixedWidth(40)
        self.appointment_done_button.setCursor(Qt.CursorShape.PointingHandCursor)
        
        edit_emp_icon = QIcon(r"static/icons/edit_button_light.svg")
        self.edit_button.setIcon(edit_emp_icon)
        
        delete_emp_icon = QIcon(r"static/icons/delete_button_light.svg")
        self.delete_button.setIcon(delete_emp_icon)
        
        appointment_done_icon = QIcon(r"static/icons/check_light.svg")
        self.appointment_done_button.setIcon(appointment_done_icon)
        
        
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.appointment_done_button)
        
class ServicesActionButtons(QWidget):
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
