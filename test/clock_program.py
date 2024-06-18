import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer, QTime, Qt

class ClockWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock")

        # Set up the main widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create and configure the QLabel to display the time
        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.time_label)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Set up a QTimer to update the time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)

        # Initial call to update the time label
        self.update_time()



    def update_time(self):
        # Get the current time and format it as a string
        current_time = QTime.currentTime()
        time_string = current_time.toString('hh:mm:ss: AP')
        # Update the QLabel with the formatted time string
        self.time_label.setText(time_string)

# Set up the application and main window
app = QApplication(sys.argv)
window = ClockWindow()
window.show()
# Run the application event loop
sys.exit(app.exec())
