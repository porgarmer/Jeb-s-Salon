from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Extract Text from QLineEdit")

        # Create a QLineEdit widget
        self.line_edit = QLineEdit(self)
        self.line_edit.setPlaceholderText("Enter text here...")

        # Create a QPushButton widget
        self.button = QPushButton("Get Text", self)

        # Connect the button's clicked signal to the function
        self.button.clicked.connect(self.get_text)

        # Create a layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def get_text(self):
        # Function to extract text from QLineEdit and show it in a message box
        text = self.line_edit.text()
        QMessageBox.information(self, "Extracted Text", f"Text: {text}")

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()