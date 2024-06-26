from PyQt6.QtWidgets import QApplication
import sys
from login_page.login import LoginPage
from main_page.main_page import MainPage
def main():
    app = QApplication(sys.argv)
    window = MainPage()

    window.show()
    app.exec()


if __name__ == "__main__":
    main()  