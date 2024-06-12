import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QHeaderView, QGraphicsBlurEffect, QMessageBox
from PyQt6.uic import loadUi
from main_page import resources
from database.connect_db import Database


class MainPage(QMainWindow):
    def __init__(self) -> None:
        super(MainPage, self).__init__()
        loadUi(r"ui_files/main.ui", self)
        
        self.db = Database()
        
        self.side_bar_icon_only.setHidden(True)
        self.switch_to_dashboard_page()
        
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

        self.logout_button.clicked.connect(self.logout)
        
    ### tab switching functions ###
    def switch_to_dashboard_page(self):
        index = self.stackedWidget.indexOf(self.dashboard_page)
        self.stackedWidget.setCurrentIndex(index)
    
    def switch_to_employees_page(self):
        index = self.stackedWidget.indexOf(self.employees_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.emp_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
                                
        ### employees tab button links ###
        self.add_emp_button.clicked.connect(self.show_add_employee_dialog)
        self.edit_emp_button.clicked.connect(self.show_edit_employee_dialog)
        self.delete_emp_button.clicked.connect(self.delete_employee)
        self.select_all_emp_button.clicked.connect(self.select_all_emp_cells) 
        self.deselect_all_emp_button.clicked.connect(self.deselect_all_emp_cells)
        self.more_emp_details_button.clicked.connect(self.more_emp_details)
        
        for row in range(self.emp_table.rowCount()):
            item = self.emp_table.item(row, 0)
            if item is not None:
                item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                item.setCheckState(Qt.CheckState.Unchecked)        
            
        self.emp_table.cellClicked.connect(self.select_all_emp_cells_in_row)    
        
    def switch_to_customers_page(self):
        index = self.stackedWidget.indexOf(self.customers_page)
        self.stackedWidget.setCurrentIndex(index)
        header = self.cus_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
                ### employees tab button links ###
        self.add_cus_button.clicked.connect(self.show_add_customer_dialog)
        self.edit_cus_button.clicked.connect(self.show_edit_customer_dialog)
        self.delete_cus_button.clicked.connect(self.delete_customer)
        self.select_all_cus_button.clicked.connect(self.select_all_cus_cells) 
        self.deselect_all_cus_button.clicked.connect(self.deselect_all_cus_cells)
        # self.more_cus_details_button.clicked.connect(self.)
        
        for row in range(self.cus_table.rowCount()):
            item = self.cus_table.item(row, 0)
            if item is not None:
                item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                item.setCheckState(Qt.CheckState.Unchecked)        
        
        self.cus_table.cellClicked.connect(self.select_all_cus_cells_in_row)    

    def switch_to_services_page(self):
        index = self.stackedWidget.indexOf(self.services_page)
        self.stackedWidget.setCurrentIndex(index)
        
    def switch_to_transac_history_page(self):
        index = self.stackedWidget.indexOf(self.transaction_history_page)
        self.stackedWidget.setCurrentIndex(index)
        
    def switch_to_profile_page(self):
        index = self.stackedWidget.indexOf(self.profile_page)
        self.stackedWidget.setCurrentIndex(index)
        
    
    def logout(self):
        from login_page.login import LoginPage
        self.login_page = LoginPage()
        self.login_page.show()
        self.close()
        
######## Functions for the employees tab#########

    def show_add_employee_dialog(self):
        from main_page.employees_tab import AddEmployee
        
        self.add_employee_dialog = AddEmployee()
        
        #Blur effect for the main window
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
    
        self.add_employee_dialog.finished.connect(self.reset_blur_effect) 
        self.add_employee_dialog.exec()
        
    def show_edit_employee_dialog(self):
        from main_page.employees_tab import EditEmployee
        
        self.edit_employee_dialog = EditEmployee()
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
        
        self.edit_employee_dialog.finished.connect(self.reset_blur_effect) 
        self.edit_employee_dialog.exec()
        
        
    def delete_employee(self): 
        reply = QMessageBox.warning(self, 'Message', 'Are you sure you want to delete this employee?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
        else:
            print("No button pressed")
        
    def select_all_emp_cells(self):
        # Iterate over all cells and select them
        for row in range(self.emp_table.rowCount()):
            item = self.emp_table.item(row, 0)
            if item.checkState() == Qt.CheckState.Unchecked:
                item.setCheckState(Qt.CheckState.Checked)
                for column in range(self.emp_table.columnCount()):
                    item = self.emp_table.item(row, column)
                    if item is not None:
                        item.setSelected(True)
    
    def deselect_all_emp_cells(self):
        # Iterate over all cells and select them
        for row in range(self.emp_table.rowCount()):
            item = self.emp_table.item(row, 0)
            if item.checkState() == Qt.CheckState.Checked:
                item.setCheckState(Qt.CheckState.Unchecked)
                for column in range(self.emp_table.columnCount()):
                    item = self.emp_table.item(row, column)
                    if item is not None:
                        item.setSelected(False)
    
    def select_all_emp_cells_in_row(self):
        for row in range(self.emp_table.rowCount()):
            item = self.emp_table.item(row, 0)
            if item.checkState() == Qt.CheckState.Checked:
                for column in range(self.emp_table.columnCount()):
                    item = self.emp_table.item(row, column)
                    if item is not None:
                        item.setSelected(True)
            else:
                for column in range(self.emp_table.columnCount()):
                    item = self.emp_table.item(row, column)
                    if item is not None:
                        item.setSelected(False)
    
    def more_emp_details(self):
        from main_page.employees_tab import MoreDetails

        self.more_details_dialog = MoreDetails()
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
        
        self.more_details_dialog.finished.connect(self.reset_blur_effect) 
        self.more_details_dialog.exec()
            
    def reset_blur_effect(self):
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(0)
        self.setGraphicsEffect(blur_effect)
        
        
######## Functions for the customers tab#########

    def show_add_customer_dialog(self):
        from main_page.customers_tab import AddCustomer
        
        self.add_customer_dialog = AddCustomer()
        
        #Blur effect for the main window
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
    
        self.add_customer_dialog.finished.connect(self.reset_blur_effect) 
        self.add_customer_dialog.exec()
        
        
    def show_edit_customer_dialog(self):
        from main_page.customers_tab import EditCustomer
        
        self.edit_customer_dialog = EditCustomer()
        
        #Blur effect for the main window
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(3)
        self.setGraphicsEffect(blur_effect)
    
        self.edit_customer_dialog.finished.connect(self.reset_blur_effect) 
        self.edit_customer_dialog.exec()

    def delete_customer(self): 
        reply = QMessageBox.warning(self, 'Message', 'Are you sure you want to delete this customer?', 
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
                                     QMessageBox.StandardButton.No)
        
       # Check which button was pressed
        if reply == QMessageBox.StandardButton.Yes:
            print("Yes button pressed")
        else:
            print("No button pressed")
            
    def select_all_cus_cells(self):
        # Iterate over all cells and select them
        for row in range(self.cus_table.rowCount()):
            item = self.cus_table.item(row, 0)
            if item.checkState() == Qt.CheckState.Unchecked:
                item.setCheckState(Qt.CheckState.Checked)
                for column in range(self.cus_table.columnCount()):
                    item = self.cus_table.item(row, column)
                    if item is not None:
                        item.setSelected(True)
    
    def deselect_all_cus_cells(self):
        # Iterate over all cells and select them
        for row in range(self.cus_table.rowCount()):
            item = self.cus_table.item(row, 0)
            if item.checkState() == Qt.CheckState.Checked:
                item.setCheckState(Qt.CheckState.Unchecked)
                for column in range(self.cus_table.columnCount()):
                    item = self.cus_table.item(row, column)
                    if item is not None:
                        item.setSelected(False)
    
    def select_all_cus_cells_in_row(self):
        for row in range(self.cus_table.rowCount()):
            item = self.cus_table.item(row, 0)
            if item.checkState() == Qt.CheckState.Checked:
                for column in range(self.cus_table.columnCount()):
                    item = self.cus_table.item(row, column)
                    if item is not None:
                        item.setSelected(True)
            else:
                for column in range(self.cus_table.columnCount()):
                    item = self.cus_table.item(row, column)
                    if item is not None:
                        item.setSelected(False)