# import sys
# from PyQt6.QtWidgets import QApplication, uic

# app = QtWidgets.QApplication(sys.argv)

# window = uic.loadUi("login_page.ui")

# window.show()
# app.exec()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Main()
#     window.show()
#     sys.exit(app.exec())
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsDropShadowEffect, QMessageBox
from PyQt6.QtGui import QColor
from PyQt6.uic import loadUi
from database.database import Database
import sys

class Main(QMainWindow):
    def __init__(self) -> None:
        super(Main, self).__init__()
        loadUi(r"ui_files/login_page.ui", self)
        shadow_effect = QGraphicsDropShadowEffect()
        shadow_effect.setBlurRadius(35)
        shadow_effect.setXOffset(0)
        shadow_effect.setYOffset(0)
        shadow_effect.setColor(QColor(0, 0, 0, 150))

        self.db = Database()

        self.user_name.setGraphicsEffect(shadow_effect)
        self.login_pane.setGraphicsEffect(shadow_effect)
        # self.actionNew.triggered.connect(lambda: self.clicked("New was clicked"))
        # self.actionSave.triggered.connect(lambda: self.clicked("Save was clicked"))
        # self.actionCopy.triggered.connect(lambda: self.clicked("Copy was clicked"))
        # self.actionPaste.triggered.connect(lambda: self.clicked("Paste was clicked"))
        self.login_button.clicked.connect(self.test)
        
    def test(self):
        results = self.db.test()
        for result in results:
            print(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())