
import sys
import os

# Get the parent directory of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the Python path
sys.path.append(parent_dir)
# from database.connect_db import Database

# db = Database()


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

#         self.setWindowTitle("ComboBox with Styled Drop-down")

#         self.combo_box = QComboBox(self)
#         self.combo_box.addItems(["Option 1", "Option 2", "Option 3"])

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

from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Styled QLineEdit Context Menu")

        # Create central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create layout
        layout = QVBoxLayout(central_widget)

        # Create QLineEdit widgets
        self.line_edit1 = QLineEdit("Right-click me", self)
        self.line_edit2 = QLineEdit("Right-click me too", self)

        # Add QLineEdit widgets to layout
        layout.addWidget(self.line_edit1)
        layout.addWidget(self.line_edit2)

        # Apply style sheet
        self.setStyleSheet("""
            QLineEdit {
                background-color: #f0f0f0;
                color: #333;
                border: 2px solid #6a9fb5;
                border-radius: 5px;
                padding: 5px;
            }
            QMenu {
                background-color: #6a9fb5;
                border: 1px solid #333;
                padding: 5px;
            }
            QMenu::item {
                background-color: transparent;
                padding: 5px 10px;
                color: white;
            }
            QMenu::item:selected {
                background-color: #555;
                color: white;
            }
            QMenu::separator {
                height: 1px;
                background: #333;
                margin: 5px 0;
            }
        """)

if __name__ == "__main__":
    app = QApplication([])

    main_window = MainWindow()
    main_window.show()

    app.exec()