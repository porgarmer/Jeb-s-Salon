
from datetime import date, datetime, time
from random import randint
import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)
from database.connect_db import Database

db = Database()


#error message
# QMessageBox.warning(self, " ", "Failed to connect to database. Please check your internet connection.")


# from PyQt6.QtCore import Qt, QAbstractTableModel
# from PyQt6.QtWidgets import QApplication, QTableView, QVBoxLayout, QWidget
# from database.connect_db import Database
# class MyTableModel(QAbstractTableModel):
#     def __init__(self, data):
#         super().__init__()
#         self._data = data
#     def data(self, index, role):
#         if role == Qt.ItemDataRole.DisplayRole:
#             return self._data[index.row()][index.column()]

#     def rowCount(self, index):
#         return len(self._data)

#     def columnCount(self, index):
#         return len(self._data[0])

# class TableViewExample(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.db = Database()
#         self.setWindowTitle("QTableView Example")

#         layout = QVBoxLayout()
#         self.table = QTableView()
#         layout.addWidget(self.table)

#         # Sample data
#         data = self.db.test()
        
#         # Create and set the model
#         self.model = MyTableModel(data)
#         self.table.setModel(self.model)

#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication([])
#     window = TableViewExample()
#     window.show()
#     app.exec()

# from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton

# class CustomDialog(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Custom Dialog with Border Radius")

#         # Set the border radius using a stylesheet
#         self.setStyleSheet("""
#             QDialog {
#                 border: 2px solid #8f8f8f;
#                 border-radius: 20px;
#                 background-color: #f0f0f0;
#             }
#         """)

#         # Set up the layout and add some widgets
#         layout = QVBoxLayout()
#         label = QLabel("This is a custom dialog with a border radius.")
#         close_button = QPushButton("Close")
#         close_button.clicked.connect(self.accept)  # Close the dialog when the button is clicked

#         layout.addWidget(label)
#         layout.addWidget(close_button)
#         self.setLayout(layout)

# if __name__ == "__main__":
#     app = QApplication([])

#     dialog = CustomDialog()
#     dialog.exec()  # Show the dialog

#     app.exec()


##### Select all cells method ############

#   def select_all_cells(self):
#         # Iterate over all cells and select them
#         for row in range(self.tableWidget.rowCount()):
#             for column in range(self.tableWidget.columnCount()):
#                 item = self.tableWidget.item(row, column)
#                 if item is not None:
#                     item.setSelected(True)

##### Retrieve the cell values

    # def get_cell_values(self):
    #     for row in range(self.emp_table.rowCount()):
    #         item = self.emp_table.item(row, 0)
    #         if item.checkState() == Qt.CheckState.Checked:
    #             print([self.emp_table.item(row, column).text() for column in range(self.emp_table.columnCount()) if self.emp_table.item(row, column)])


#### Message Box ####

# from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QVBoxLayout, QMessageBox


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.openDialogButton = QPushButton("Open Dialog", self)
#         self.openDialogButton.clicked.connect(self.open_dialog)
#         self.setCentralWidget(self.openDialogButton)

#     def open_dialog(self):
#         self.dialog = CustomDialog(self)
#         self.dialog.show()


# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.setWindowTitle("Dialog")

#         self.messageButton = QPushButton("Show Message Box", self)
#         self.messageButton.clicked.connect(self.show_message_box)

#         layout = QVBoxLayout()
#         layout.addWidget(self.messageButton)
#         self.setLayout(layout)

#     def show_message_box(self):
#         # Create a message box with "Yes" and "No" buttons
#         reply = QMessageBox.question(self, 'Message', 'Do you want to proceed?',
#                                      QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
#                                      QMessageBox.StandardButton.No)

#         # Check which button was pressed
#         if reply == QMessageBox.StandardButton.Yes:
#             print("Yes button pressed")
#         else:
#             print("No button pressed")


# if __name__ == "__main__":
#     app = QApplication([])

#     window = MainWindow()
#     window.show()

#     app.exec()


#### Customize combo box ####

# from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.db = Database()
#         self.setWindowTitle("ComboBox with Styled Drop-down")

#         self.combo_box = QComboBox(self)
#         self.combo_box.setPlaceholderText("oten")
#         services = self.db.select_services()
#         if services:
#             for service in services:
#                 self.combo_box.addItem(service[1])            
#             self.combo_box.setPlaceholderText("FILTER BY ")

#         layout = QVBoxLayout()
#         layout.addWidget(self.combo_box)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         self.setStyleSheet("""
#             QComboBox::drop-down {
#                 background-color: #6a9fb5; /* Change the background color of the drop-down arrow */
#             }
#             QComboBox QAbstractItemView {
#                 background-color: #6a9fb5; /* Change the background color of the drop-down list */
#                 color: white; /* Change the text color of the drop-down list */
#             }
#         """)


# if __name__ == "__main__":
#     app = QApplication([])

#     window = MainWindow()
#     window.show()

#     app.exec()

# from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QDateEdit, QLabel

# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.setWindowTitle("Styled QDateEdit with Calendar Popup")

#         # Create widgets
#         self.date_edit = QDateEdit(self)
#         self.label = QLabel("This is a label", self)

#         # Set layout
#         layout = QVBoxLayout()
#         layout.addWidget(self.date_edit)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         # Apply style sheet
#         self.setStyleSheet("""
#             QDateEdit {
#                 background-color: #f0f0f0;
#                 color: #333;
#                 border: 2px solid #6a9fb5;
#                 border-radius: 5px;
#                 padding: 5px;
#             }
#             QDateEdit::drop-down {
#                 subcontrol-origin: padding;
#                 subcontrol-position: top right;
#                 width: 20px;
#                 border-left: 1px solid #6a9fb5;
#             }
#             QDateEdit::down-arrow {
#                 image: url(down_arrow.png);  /* Use your own arrow image */
#                 width: 12px;
#                 height: 12px;
#             }
#             QDateEdit QAbstractItemView {
#                 selection-background-color: #6a9fb5;
#                 selection-color: white;
#                 background-color: #f0f0f0;
#             }
#             QCalendarWidget QWidget#qt_calendar_navigationbar {
#                 background-color: #6a9fb5; /* Navigation bar background */
#             }
#             QCalendarWidget QToolButton {
#                 height: 30px;
#                 width: 100px;
#                 color: white;
#                 font-size: 14px;
#                 icon-size: 20px, 20px;
#                 background-color: #6a9fb5;
#             }
#             QCalendarWidget QMenu {
#                 width: 100px;
#                 color: white;
#                 background-color: #6a9fb5;
#             }
#             QCalendarWidget QMenu::item {
#                 padding: 5px;
#             }
#             QCalendarWidget QMenu::item:selected {
#                 background-color: #333;  /* Background color when an item is selected */
#                 color: white;  /* Text color when an item is selected */
#             }
#             QCalendarWidget QMenu::item:hover {
#                 background-color: #555;  /* Background color when an item is hovered */
#                 color: white;  /* Text color when an item is hovered */
#             }
#             QCalendarWidget QSpinBox {
#                 width: 50px;
#                 font-size: 14px;
#                 color: white;
#                 background-color: #6a9fb5;
#                 selection-background-color: #333;
#                 selection-color: white;
#             }
#             QCalendarWidget QSpinBox::up-button {
#                 subcontrol-origin: border;
#                 subcontrol-position: top right;
#                 width: 16px;
#                 height: 16px;
#             }
#             QCalendarWidget QSpinBox::down-button {
#                 subcontrol-origin: border;
#                 subcontrol-position: bottom right;
#                 width: 16px;
#                 height: 16px;
#             }
#             QCalendarWidget QAbstractItemView:enabled {
#                 font-size: 14px;
#                 color: black;
#                 background-color: white;
#                 selection-background-color: #6a9fb5;
#                 selection-color: white;
#             }
#         """)

# if __name__ == "__main__":
#     app = QApplication([])

#     dialog = CustomDialog()
#     dialog.show()

#     app.exec()

# from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QMenu

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Styled QLineEdit Context Menu")

#         # Create central widget
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)

#         # Create layout
#         layout = QVBoxLayout(central_widget)

#         # Create QLineEdit widgets
#         self.line_edit1 = QLineEdit("Right-click me", self)
#         self.line_edit2 = QLineEdit("Right-click me too", self)

#         # Add QLineEdit widgets to layout
#         layout.addWidget(self.line_edit1)
#         layout.addWidget(self.line_edit2)

#         # Apply style sheet
#         self.setStyleSheet("""
#             QLineEdit {
#                 background-color: #f0f0f0;
#                 color: #333;
#                 border: 2px solid #6a9fb5;
#                 border-radius: 5px;
#                 padding: 5px;
#             }
#             QMenu {
#                 background-color: #6a9fb5;
#                 border: 1px solid #333;
#                 padding: 5px;
#             }
#             QMenu::item {
#                 background-color: transparent;
#                 padding: 5px 10px;
#                 color: white;
#             }
#             QMenu::item:selected {
#                 background-color: #555;
#                 color: white;
#             }
#             QMenu::separator {
#                 height: 1px;
#                 background: #333;
#                 margin: 5px 0;
#             }
#         """)

# if __name__ == "__main__":
#     app = QApplication([])

#     main_window = MainWindow()
#     main_window.show()

#     app.exec()

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("Table with Action Buttons")
        
#         # Create central widget
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
        
#         # Create layout
#         layout = QVBoxLayout(central_widget)
        
#         # Create table
#         self.table = QTableWidget(3, 3)  # 3 rows, 3 columns
#         layout.addWidget(self.table)
        
#         # Set headers
#         self.table.setHorizontalHeaderLabels(["Name", "Age", "Actions"])
        
#         # Populate table with data and action buttons
#         self.populate_table()
    
#     def populate_table(self):
#         data = [
#             {"name": "John Doe", "age": 28},
#             {"name": "Jane Smith", "age": 34},
#             {"name": "Mike Johnson", "age": 45},
#         ]
        
#         for row, entry in enumerate(data):
#             self.table.setItem(row, 0, QTableWidgetItem(entry["name"]))
#             self.table.setItem(row, 1, QTableWidgetItem(str(entry["age"])))
            
#             # Add action button
#             action_button = QPushButton("Action")
#             action_button.clicked.connect(lambda _, r=row: self.handle_action(r))
#             self.table.setCellWidget(row, 2, action_button)
    
#     def handle_action(self, row):
#         name_item = self.table.item(row, 0)
#         age_item = self.table.item(row, 1)
        
#         name = name_item.text() if name_item else "N/A"
#         age = age_item.text() if age_item else "N/A"
        
#         print(f"Action button clicked for: {name}, Age: {age}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec())


# from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLineEdit, QLabel
# from PyQt6.QtCore import pyqtSignal, Qt

# class FirstDialog(QDialog):
#     send_data = pyqtSignal(str)  # Custom signal to send data

#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("First Dialog")

#         # Layout
#         layout = QVBoxLayout()

#         # Input field
#         self.input_field = QLineEdit(self)
#         layout.addWidget(self.input_field)

#         # Button to send data to second dialog
#         self.send_button = QPushButton("Send to Second Dialog", self)
#         self.send_button.clicked.connect(self.send_data_to_second_dialog)
#         layout.addWidget(self.send_button)

#         self.setLayout(layout)

#     def send_data_to_second_dialog(self):
#         text = self.input_field.text()
#         self.send_data.emit(text)  # Emit the custom signal with the input text
#         self.accept()  # Close the dialog
        
# class SecondDialog(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Second Dialog")

#         # Layout
#         layout = QVBoxLayout()

#         # Label to display received data
#         self.display_label = QLabel("Data from First Dialog will appear here", self)
#         layout.addWidget(self.display_label)

#         # Set layout
#         self.setLayout(layout)

#     def set_data(self, text):
#         self.display_label.setText(text)
        
# class MainWindow(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Main Window")

#         # Layout
#         layout = QVBoxLayout()

#         # Button to open first dialog
#         self.open_first_dialog_button = QPushButton("Open First Dialog", self)
#         self.open_first_dialog_button.clicked.connect(self.open_first_dialog)
#         layout.addWidget(self.open_first_dialog_button)

#         self.setLayout(layout)

#     def open_first_dialog(self):
#         first_dialog = FirstDialog()
#         second_dialog = SecondDialog()

#         # Connect the signal from the first dialog to the method of the second dialog
#         first_dialog.send_data.connect(second_dialog.set_data)

#         if first_dialog.exec() == QDialog.DialogCode.Accepted:
#             second_dialog.exec()
            
            
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec())

# mylist = []

# list1 = [["oten", "bilat", "tae"], ["dsffd", "dssad", "sflkls"]]

# for i, row_data in enumerate(list1):
 
#         print(row_data)

# from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout

# class ActionWidget(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         layout = QHBoxLayout()
#         self.delete_button = QPushButton("Delete")
#         layout.addWidget(self.delete_button)
#         self.setLayout(layout)
        
# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QTableWidget with Custom Action Widgets")

#         # Set up the layout
#         layout = QVBoxLayout()

#         # Create a QTableWidget
#         self.table_widget = QTableWidget()
#         self.table_widget.setRowCount(5)
#         self.table_widget.setColumnCount(4)
#         self.table_widget.setHorizontalHeaderLabels(["Column 1", "Column 2", "Column 3", "Actions"])

#         # Fill the table with some data and custom action widgets
#         for row in range(5):
#             for column in range(3):
#                 item = QTableWidgetItem(f"Item {row+1}, {column+1}")
#                 self.table_widget.setItem(row, column, item)

#             # Create the custom action widget
#             action_widget = ActionWidget()
#             action_widget.delete_button.clicked.connect(self.delete_row)

#             # Add the custom action widget to the actions column
#             self.table_widget.setCellWidget(row, 3, action_widget)

#         layout.addWidget(self.table_widget)

#         # Set up the main window
#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def delete_row(self):
#         # Get the button that was clicked
#         button = self.sender()
#         if button:
#             # Find the index of the button
#             for row in range(self.table_widget.rowCount()):
#                 widget = self.table_widget.cellWidget(row, 3)
#                 if widget and widget.delete_button == button:
#                     print(row)
#                     self.table_widget.removeRow(row)
#                     break

# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()

# sys.exit(app.exec())
# import sys
# from PyQt6.QtWidgets import QApplication, QComboBox, QVBoxLayout, QMainWindow, QWidget, QPushButton, QLabel
# from PyQt6.QtCore import Qt
# from PyQt6.QtGui import QStandardItemModel, QStandardItem
# class CheckableComboBox(QComboBox):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setModel(QStandardItemModel(self))
#         self.view().pressed.connect(self.handle_item_pressed)
#         self.setEditable(True)
#         self.lineEdit().setReadOnly(True)
#         self.lineEdit().setAlignment(Qt.AlignmentFlag.AlignLeft)

#     def handle_item_pressed(self, index):
#         item = self.model().itemFromIndex(index)
#         if item.checkState() == Qt.CheckState.Checked:
#             item.setCheckState(Qt.CheckState.Unchecked)
#         else:
#             item.setCheckState(Qt.CheckState.Checked)

#     def add_checkable_item(self, text, checked=False):
#         item = QStandardItem(text)
#         item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
#         item.setData(Qt.CheckState.Checked if checked else Qt.CheckState.Unchecked, Qt.ItemDataRole.CheckStateRole)
#         self.model().appendRow(item)

#     def checked_items(self):
#         checked_items = []
#         for index in range(self.model().rowCount()):
#             item = self.model().item(index)
#             if item.checkState() == Qt.CheckState.Checked:
#                 checked_items.append(item.text())
#         return checked_items

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Checkable ComboBox Example")

#         layout = QVBoxLayout()

#         self.combo = CheckableComboBox()
#         services = db.select_services()
#         for service in services:
            
#             self.combo.add_checkable_item(service[1])

#         self.button = QPushButton("Get Checked Items")
#         self.button.clicked.connect(self.show_checked_items)

#         self.label = QLabel("Checked items will be shown here")

#         layout.addWidget(self.combo)
#         layout.addWidget(self.button)
#         layout.addWidget(self.label)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         # Set default text
#         self.set_combobox_default_text()

#     def set_combobox_default_text(self):
#         # Method 1: Using setCurrentText
#         self.combo.setCurrentText("Select an oten...")
#         # Method 2: Adding a placeholder item
#         # placeholder_item = QStandardItem("Select an option...")
#         # placeholder_item.setFlags(Qt.ItemFlag.NoItemFlags)
#         # self.combo.model().insertRow(0, placeholder_item)
#         # self.combo.setCurrentIndex(0)

#     def show_checked_items(self):
#         checked_items = self.combo.checked_items()
#         self.label.setText("Checked items: " + ", ".join(checked_items))

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())

# def update_info(self, student_id, student_first_name, student_last_name, student_city, student_state, student_email_address):
        
#         self.connect_db()
        
#         sql = f"""
#             update student 
#                 set stu_first_name='{student_first_name}', stu_last_name='{student_last_name}', stu_state='{student_state}',
#                     stu_city='{student_city}', stu_email_address='{student_email_address}'
#                 where stu_id='{student_id}';
#         """
        
#         try:
#             self.cursor.execute(sql)
#             self.conn.commit()
#         except Exception as e:
#             self.conn.rollback()
#             return e
#         finally:
#             self.conn.close()
#             self.cursor.close()


# for i, data in enumerate(db.select_employee_services(emp_id=67890)):
#     print(data)
    

# for i, data in enumerate(db.select_services()):
#     print(data[0])
    
# services = db.select_services()
# employee_services = db.select_employee_services(emp_id="F20240615997")
        
# for i, service in enumerate(services):
    
#     if service[0] in employee_services:
#         print(service[0])

# print(db.select_employee_services(emp_id=1))
# db.update_service("6", ("oten bilat", 20))

# print("test".upper())

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHeaderView
# from PyQt6.QtCore import Qt
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QTableWidget Sorting Example")

#         # Setup UI components
#         layout = QVBoxLayout()

#         self.table_widget = QTableWidget()
#         self.table_widget.setColumnCount(2)
#         self.table_widget.setHorizontalHeaderLabels(["Name", "Age"])

#         self.populate_table()

#         self.sort_button = QPushButton("Sort by Age")
#         self.sort_button.clicked.connect(self.sort_by_age)

#         layout.addWidget(self.table_widget)
#         layout.addWidget(self.sort_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def populate_table(self):
#         # Dummy data for the table
#         data = [
#             ("Alice", 25),
#             ("Bob", 30),
#             ("Charlie", 28),
#             ("David", 22),
#             ("Eve", 35)
#         ]

#         self.table_widget.setRowCount(len(data))

#         for row, (name, age) in enumerate(data):
#             item_name = QTableWidgetItem(name)
#             item_age = QTableWidgetItem(str(age))

#             self.table_widget.setItem(row, 0, item_name)
#             self.table_widget.setItem(row, 1, item_age)

#     def sort_by_age(self):
#         # Sort the table by the second column (Age)
#         self.table_widget.sortItems(0, order=Qt.SortOrder.DescendingOrder)

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QDateTimeEdit, QPushButton, QLabel
# from PyQt6.QtCore import QDate, QTime, QDateTime

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QDateTimeEdit Example")

#         # Setup UI components
#         layout = QVBoxLayout()

#         self.datetime_edit = QDateTimeEdit()
#         self.datetime_edit.setDateTime(QDateTime.currentDateTime())

#         self.date_label = QLabel()
#         self.time_label = QLabel()

#         self.button = QPushButton("Retrieve Date and Time")
#         self.button.clicked.connect(self.retrieve_datetime)

#         layout.addWidget(self.datetime_edit)
#         layout.addWidget(self.button)
#         layout.addWidget(self.date_label)
#         layout.addWidget(self.time_label)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#     def retrieve_datetime(self):
#         datetime = self.datetime_edit.dateTime()

#         date = datetime.date()
#         time = datetime.time().toString("h:mm AP")

#         self.date_label.setText(f"Date: {date.toString()}")
#         self.time_label.setText(f"Time: {time}")

# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# sys.exit(app.exec())

# # mydict = {"oten": [1,2,3]}

# # print(mydict["oten"][0])

# print(db.select_service_by_name("massage")[0][0])

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
# from PyQt6.QtCore import QTimer, QTime, Qt

# class ClockWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Clock")

#         # Set up the main widget and layout
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Create and configure the QLabel to display the time
#         self.time_label = QLabel()
#         self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(self.time_label)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#         # Set up a QTimer to update the time every second
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_time)
#         self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

#         # Initial call to update the time label
#         self.update_time()

#     def update_time(self):
#         # Get the current time and format it as a string
#         current_time = QTime.currentTime()
#         time_string = current_time.toString('hh:mm:ss: AP')
#         # Update the QLabel with the formatted time string
#         self.time_label.setText(time_string)

# # Set up the application and main window
# app = QApplication(sys.argv)
# window = ClockWindow()
# window.show()
# # Run the application event loop
# sys.exit(app.exec())

# employees = db.select_available_employees_by_service("manicure")

# for data in employees:
#     print(data[1] + " " + data[3])

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QComboBox Selected Slot Example")

#         # Set up the main widget and layout
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Create and configure the QComboBox
#         self.combo_box = QComboBox()
#         employees = db.select_available_employees_by_service("manicure")
#         for employee in employees:
#             self.combo_box.addItem(f"{employee[1]} {employee[3]}")
#         self.combo_box.currentIndexChanged.connect(self.on_selection_change)

#         # Create a QLabel to display the selected item
#         self.label = QLabel("Selected: None")

#         layout.addWidget(self.combo_box)
#         layout.addWidget(self.label)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def on_selection_change(self, index):
#         # Get the selected text from the QComboBox
#         selected_text = self.combo_box.itemText(index)
#         # Update the QLabel with the selected text
#         self.label.setText(f"Selected: {selected_text}")

# # Set up the application and main window
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# # Run the application event loop
# sys.exit(app.exec())

# def generate_cus_id(cus_app_date):

#         while True:
#             cus_app_date = cus_app_date.replace("-", "")
#             random_number = str(randint(1,1000))
            
#             generated_cus_id =  cus_app_date + random_number
            
#             #check if generated ID exists
#             cus_id_exist = db.check_cus_id(generated_cus_id)
            
#             if not cus_id_exist:
#                 return generated_cus_id

# results = db.select_all_customers()
# for result in results:
#     print(result)

# date_time =  "2024-08-05 14:00:00".split(" ")
# date_time = datetime.strptime(date_time[0], "%Y-%m-%d").date() 
# date_time = date_time.strftime("%m-%d-%y")

# date_time = datetime.strptime(date_time[1], "%I:%M:%S")
# print(date_time)


# current_time = datetime.datetime.now().time()

# # Format the time using strftime
# formatted_time = current_time.strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
# # formatted_time = current_time.strftime('%H:%M:%S')  # 24-hour format
# # formatted_time = current_time.strftime('%H:%M')  # Hours and minutes only
# # formatted_time = current_time.strftime('%I:%M %p')  # 12-hour format with AM/PM, hours and minutes only

# print("Formatted Time:", formatted_time)

# from PyQt6.QtCore import QTime, QDate, QDateTime
# date_time = "2024-08-05 14:00:00".split(" ")
# time = QTime.fromString(date_time[1]).toString("hh:mm AP")

# date = datetime.strptime(date_time[0], "%Y-%m-%d")
# date = date.strftime("%m-%d-%Y")

# print(date, time)

# results = db.select_all_customers()
# for result in results:
#     print(result)



# ['01-01-2000', '12:00 AM', '01012000360', 'massage', 'Rolino Ongco']
# db.add_customer_appointment(['01-02-2000', '12:00 AM', '01022000257', 'manicure', 'Shane Johnson Agbon'])

# import sys
# from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QLabel

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Remove Whitespace Example")

#         # Set up the main widget and layout
#         central_widget = QWidget()
#         layout = QVBoxLayout()

#         # Create and configure the QLineEdit
#         self.line_edit = QLineEdit()
#         self.line_edit.setPlaceholderText("Enter text")
#         self.line_edit.textEdited.connect(self.trim_whitespace)
#         layout.addWidget(self.line_edit)

#         # Create and configure a QLabel to display the input text
#         self.label = QLabel()
#         layout.addWidget(self.label)

#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

#     def trim_whitespace(self, text):
#         # Remove leading and trailing whitespace from the text
#         trimmed_text = text.strip()
        
#         # Update the QLineEdit's text only if it has changed after trimming
#         if self.line_edit.text() != trimmed_text:
#             self.line_edit.setText(trimmed_text)
        
#         # Update the label to show the current text in the QLineEdit
#         self.label.setText(f"Current Text: '{trimmed_text}'")

# # Set up the application and main window
# app = QApplication(sys.argv)
# window = MainWindow()
# window.show()
# # Run the application event loop
# sys.exit(app.exec())

# string = "rolinO b oNgco"
# print(string.title())

