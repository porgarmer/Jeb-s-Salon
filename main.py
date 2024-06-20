from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGraphicsDropShadowEffect, QMessageBox
import sys
from login_page.login import LoginPage
from main_page.main_page import MainPage
def main():
    app = QApplication(sys.argv)
    window = LoginPage()

    window.show()
    app.exec()


if __name__ == "__main__":
    main()  