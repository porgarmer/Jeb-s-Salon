import sys
import os

from httpx import delete

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtCore import Qt, QDateTime, QTimer, QDate, QPropertyAnimation, QEasingCurve
from PyQt6.QtWidgets import QMainWindow, QHeaderView, QGraphicsBlurEffect, QMessageBox, QPushButton, QWidget, QHBoxLayout, QTableWidgetItem
from PyQt6.QtGui import QIcon
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
        self.side_bar.setMaximumWidth(217)  
        self.animation = QPropertyAnimation(self.side_bar, b"maximumWidth")

        self.toggle_side_bar_btn.clicked.connect(self.toggle_side_bar)  
        
        self.switch_to_dashboard_page()
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start(1000) 
        
        self.update_date_time()
        
        self.dashboard_button.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_icon_button.clicked.connect(self.switch_to_dashboard_page)
        self.populate_app_today_table()
        self.set_num_app_today()
        self.set_num_emp_avail()
        
        self.filter_emp_date.setDate(QDate.currentDate())
        self.filter_emp_date.userDateChanged.connect(self.filter_emp_by_date)
        self.filter_emp_available.currentIndexChanged.connect(self.filter_emp_by_available)
        self.reset_emp_filters_btn.clicked.connect(self.reset_emp_filters)
        self.emp_search_bar.textChanged.connect(self.search_employee)
        self.delete_all_emp_button.clicked.connect(self.delete_all_employees)
        self.employees_button.clicked.connect(self.switch_to_employees_page)
        self.employees_icon_button.clicked.connect(self.switch_to_employees_page)
        self.populate_employees_table()
        
        self.delete_all_cus_button.clicked.connect(self.delete_all_customers)
        self.customers_button.clicked.connect(self.switch_to_customers_page)
        self.customers_icon_button.clicked.connect(self.switch_to_customers_page)
        self.filter_app_date.setDate(QDate.currentDate())
        self.filter_app_date.userDateChanged.connect(self.filter_app_by_date)
        self.cust_search_bar.textChanged.connect(self.search_customer)
        self.reset_app_filter_btn.clicked.connect(self.reset_app_filter)
        self.populate_customers_table()
        
        self.delete_all_service.clicked.connect(self.delete_all_services)
        self.services_button.clicked.connect(self.switch_to_services_page)
        self.services_icon_button.clicked.connect(self.switch_to_services_page)
        self.reset_service_filter_btn.clicked.connect(self.reset_service_filter)
        self.service_filter.currentIndexChanged.connect(self.filter_by_service)
        self.set_up_services()
        self.populate_services_table()
        self.populate_available_employees()


        self.delete_all_transac_btn.clicked.connect(self.delete_all_transac)
        self.transac_history_button.clicked.connect(self.switch_to_transac_history_page)
        self.transac_history_button_2.clicked.connect(self.switch_to_transac_history_page)
        self.filter_transac_date.setDate(QDate.currentDate())
        self.filter_transac_date.userDateChanged.connect(self.filter_transac_by_date)
        self.reset_transac_filter_btn.clicked.connect(self.reset_transac_filter)
        self.transac_search_bar.textChanged.connect(self.seach_transac)
        self.populate_transac_table()
        

        self.logout_btn.clicked.connect(self.logout)
        self.logout_btn_icon.clicked.connect(self.logout)

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
        time_string = current_date_time.toString('MMMM dd, yyyy | hh:mm:ss AP')
        # Update the QLabel with the formatted time string
        self.current_date_time.setText(time_string)

    def toggle_side_bar(self):
        if self.side_bar.maximumWidth() == 217:
            self.animation.setDuration(250)
            self.animation.setStartValue(217)
            self.animation.setEndValue(65)
            self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animation.start()

        else:
            self.animation.setDuration(250)
            self.animation.setStartValue(65)
            self.animation.setEndValue(217)
            self.animation.setEasingCurve(QEasingCurve.Type.InOutQuart)
            self.animation.start()
        
    ### tab switching functions ###
    def switch_to_dashboard_page(self):
        index = self.stackedWidget.indexOf(self.dashboard_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.app_today_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.ResizeToContents) 
        header.setMinimumSectionSize(120)

    def switch_to_employees_page(self):
        index = self.stackedWidget.indexOf(self.employees_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.emp_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.Fixed)   
        header.setMinimumSectionSize(150)

    def switch_to_customers_page(self):
        index = self.stackedWidget.indexOf(self.customers_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.cus_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)   
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.ResizeToContents)   
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.ResizeToContents)   
        header.setSectionResizeMode(10, QHeaderView.ResizeMode.Fixed)   
        header.setMinimumSectionSize(150)
        
    def switch_to_services_page(self):
        index = self.stackedWidget.indexOf(self.services_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.services_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed) 
        self.services_table.setColumnWidth(3, 120)
        header2 = self.available_employees_table.horizontalHeader()
        header2.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
    def switch_to_transac_history_page(self):
        index = self.stackedWidget.indexOf(self.transaction_history_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.transac_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents) 
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents) 

        header.setMinimumSectionSize(150)

    def reset_blur_effect(self):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(0)
        self.setGraphicsEffect(blur_effect)
    
    def logout(self):
        from login_page.login import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()
        
        
######## Functoins fror dashboard #########
    def populate_app_today_table(self):
        self.app_today = self.db.select_customer_today()
        
        self.app_today_table.setRowCount(0)
        self.app_today_table.hideColumn(0)
        self.app_today_table.hideColumn(1)

        if self.app_today:
            for row, row_data in enumerate(self.app_today):
                self.app_today_table.insertRow(row)
                for col, cell_data in enumerate(row_data):  
                    if isinstance(cell_data, datetime):
                        cell_data = cell_data.strftime("%I:%M %p")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    
                    self.app_today_table.setItem(row, col, item)
                
    def set_num_emp_avail(self):
        self.numer_available_employees.setText(str(self.db.num_of_avail_emp()))

    def set_num_app_today(self):
        num_app_today = self.app_today_table.rowCount()
        self.number_app_today.setText(str(num_app_today))
######## Functions for the employees tab#########

    def populate_employees_table(self):
        
        self.employees = self.db.select_all_employees()
        self.emp_table.setRowCount(0)
        self.emp_table.hideColumn(0)
        
        if self.employees:
            for row, row_data in enumerate(self.employees):
                self.emp_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, date):
                        cell_data = cell_data.strftime("%B %d, %Y")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.populate_available_employees()
        self.set_num_emp_avail()

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
        self.populate_available_employees()
        self.set_num_emp_avail()

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
            self.populate_available_employees()
            self.set_num_emp_avail()

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
            self.populate_available_employees()
            self.set_num_emp_avail()
            
    def search_employee(self):
        search_param = self.emp_search_bar.text()
        
        result = self.db.search_employee(search_param)       
        
        self.emp_table.setRowCount(0)
        self.emp_table.hideColumn(0)
        
        if result:
            for row, row_data in enumerate(result):
                self.emp_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, date):
                        cell_data = cell_data.strftime("%B %d, %Y")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.emp_table.setItem(row, col, item)
                
                    #actions buttons
                action_buttons = ActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_employee_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_employee)
                action_buttons.more_details_button.clicked.connect(self.more_emp_details)
                self.emp_table.setCellWidget(row, 8, action_buttons)

    def filter_emp_by_date(self, date_param):
  
        result = self.db.select_emp_by_date(date_param=date_param.toString("yyyy-MM-dd"))
    
        self.emp_table.setRowCount(0)
        self.emp_table.hideColumn(0)
        
        if result:
            for row, row_data in enumerate(result):
                self.emp_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, date):
                        cell_data = cell_data.strftime("%B %d, %Y")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.emp_table.setItem(row, col, item)
                
                    #actions buttons
                action_buttons = ActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_employee_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_employee)
                action_buttons.more_details_button.clicked.connect(self.more_emp_details)
                self.emp_table.setCellWidget(row, 8, action_buttons)
    
    def reset_emp_filters(self):
        self.filter_emp_date.setDate(QDate.currentDate())
        self.filter_emp_available.clear()
        self.filter_emp_available.setPlaceholderText("All")
        self.filter_emp_available.addItems(["True", "False"])
        self.emp_search_bar.clear()
        self.populate_employees_table()
        
    def filter_emp_by_available(self):
        availability = self.filter_emp_available.currentText()
        result = self.db.filter_emp_available(availability=availability)
        self.emp_table.setRowCount(0)
        self.emp_table.hideColumn(0)
        
        if result:
            for row, row_data in enumerate(result):
                self.emp_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, date):
                        cell_data = cell_data.strftime("%B %d, %Y")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.emp_table.setItem(row, col, item)
                
                    #actions buttons
                action_buttons = ActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_employee_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_employee)
                action_buttons.more_details_button.clicked.connect(self.more_emp_details)
                self.emp_table.setCellWidget(row, 8, action_buttons)
        
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
                        cell_data = cell_data.strftime("%B %d, %Y | %I:%M %p")
    
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.cus_table.setItem(row, col, item)
                
                #actions buttons
                action_buttons = CustomerActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_customer_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_customer)
                action_buttons.appointment_done_button.clicked.connect(self.appointment_done)
                self.cus_table.setCellWidget(row, 10, action_buttons)
        
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
        self.populate_app_today_table()
        self.set_num_app_today()
        
    def show_edit_customer_dialog(self):
        from main_page.customers_tab import EditCustomer
        
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.cus_table.rowCount()):
                widget = self.cus_table.cellWidget(row, 10)
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
        self.populate_app_today_table()
        self.set_num_app_today()
        
    def delete_customer(self): 
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.cus_table.rowCount()):
                widget = self.cus_table.cellWidget(row, 10)
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
            self.populate_customers_table()
            self.populate_app_today_table()
            self.set_num_app_today()
        else:
            print("No button pressed")
    
    def appointment_done(self):
        button = self.sender()
        if button:
                # Find the index of the button
            for row in range(self.cus_table.rowCount()):
                widget = self.cus_table.cellWidget(row, 10)
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
            self.populate_customers_table()
            self.populate_app_today_table()
            self.set_num_app_today()
        else:
            print("No button pressed")
        
    def delete_all_customers(self):
        reply = QMessageBox.critical(self, "!!!!", "ARE YOU SURE YOU WANT TO DELETE ALL CUSTOMERS?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel, defaultButton=QMessageBox.StandardButton.Cancel)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_all_customers()
            QMessageBox.information(self, "Successful", "Successfully deleted all customers", 
                                    QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
            
            self.populate_customers_table()
            self.populate_app_today_table()
            self.set_num_app_today()

    def search_customer(self):
        
        search_param = self.cust_search_bar.text()
        result = self.db.search_customer(search_param=search_param)

        self.cus_table.setRowCount(0)
        self.cus_table.hideColumn(0)
        self.cus_table.hideColumn(1)

        if result:
            for row, row_data in enumerate(result):
                self.cus_table.insertRow(row)
                for col, cell_data in enumerate(row_data):  
                    if isinstance(cell_data, datetime):
                        cell_data = cell_data.strftime("%B %d, %Y | %I:%M %p")
                        
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                        
                    self.cus_table.setItem(row, col, item)
                
                #actions buttons
                action_buttons = CustomerActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_customer_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_customer)
                action_buttons.appointment_done_button.clicked.connect(self.appointment_done)
                self.cus_table.setCellWidget(row, 10, action_buttons)

    def filter_app_by_date(self, date_param):
        result = self.db.filter_cus_by_date(date_param=(date_param.toString("yyyy-MM-dd"),))
        self.cus_table.setRowCount(0)
        self.cus_table.hideColumn(0)
        self.cus_table.hideColumn(1)

        if result:
            for row, row_data in enumerate(result):
                self.cus_table.insertRow(row)
                for col, cell_data in enumerate(row_data):  
                    if isinstance(cell_data, datetime):
                        cell_data = cell_data.strftime("%B %d, %Y | %I:%M %p")
                        
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                        
                    self.cus_table.setItem(row, col, item)
                
                #actions buttons
                action_buttons = CustomerActionButtons()
                action_buttons.edit_button.clicked.connect(self.show_edit_customer_dialog)
                action_buttons.delete_button.clicked.connect(self.delete_customer)
                action_buttons.appointment_done_button.clicked.connect(self.appointment_done)
                self.cus_table.setCellWidget(row, 10, action_buttons)
             
    def reset_app_filter(self):
        self.cust_search_bar.clear()
        self.filter_app_date.setDate(QDate.currentDate())   
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
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

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
        old_service_name =  self.services_table.item(row,1).text()
        self.edit_service_dialog = EditService(service_id=service_id, old_service_name=old_service_name)
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
        self.edit_service_dialog.service_name.setText(self.services_table.item(row,1).text())
        self.edit_service_dialog.service_price.setValue(float(self.services_table.item(row,2).text()))

        self.edit_service_dialog.finished.connect(self.reset_blur_effect) 
        self.edit_service_dialog.exec()
        
        self.populate_customers_table()
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
            self.populate_services_table()
            self.set_up_services()            
            
            print("Yes button pressed")
        else:
            print("No button pressed")
        
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
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

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
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

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
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.available_employees_table.setItem(row, col, item)

    def reset_service_filter(self):
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

    def delete_all_services(self):
        reply = QMessageBox.critical(self, "!!!!", "ARE YOU SURE YOU WANT TO DELETE ALL SERVICES?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel, defaultButton=QMessageBox.StandardButton.Cancel)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_all_services()
            QMessageBox.information(self, "Successful", "Successfully deleted all services", 
                                    QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
            
            self.populate_services_table()
            self.populate_available_employees()
            self.service_filter.clear()
            self.service_filter.setPlaceholderText("FILTER BY SERVICE")

        
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
                        cell_data = cell_data.strftime("%B %d, %Y | %I:%M %p")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.transac_table.setItem(row, col, item)
                
    def delete_all_transac(self):
        reply = QMessageBox.critical(self, "!!!!", "ARE YOU SURE YOU WANT TO DELETE ALL TRANSACTIONS?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel, defaultButton=QMessageBox.StandardButton.Cancel)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.db.delete_all_transac()
            QMessageBox.information(self, "Successful", "Successfully deleted all transactions", 
                                    QMessageBox.StandardButton.Ok, defaultButton=QMessageBox.StandardButton.Ok)
            self.populate_transac_table()
        
    def filter_transac_by_date(self):
        self.transactions = self.db.select_transac_by_date(self.filter_transac_date.date().toString("yyyy-MM-dd"))
        self.transac_table.setRowCount(0)
        self.transac_table.hideColumn(0)

        if self.transactions:
            for row, row_data in enumerate(self.transactions):
                self.transac_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, datetime):
                        cell_data = cell_data.strftime("%B %d, %Y | %I:%M %p")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                    self.transac_table.setItem(row, col, item)

    def reset_transac_filter(self):
        self.transac_search_bar.clear()
        self.filter_transac_date.setDate(QDate.currentDate())
        self.populate_transac_table()
        
    def seach_transac(self, search_param):
        results = self.db.search_transac(search_param=search_param)
        self.transac_table.setRowCount(0)
        self.transac_table.hideColumn(0)

        if results:
            for row, row_data in enumerate(results):
                self.transac_table.insertRow(row)
                for col, cell_data in enumerate(row_data):
                    if isinstance(cell_data, datetime):
                        cell_data = cell_data.strftime("%B %d, %Y | %I:%M %p")
                    item = QTableWidgetItem(str(cell_data))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

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

