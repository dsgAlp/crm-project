import os
import sys
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt6.uic import loadUi
from PyQt6.QtCore import QCoreApplication

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class UserApplication(QMainWindow):
    def __init__(self, username):
        super().__init__()
        loadUi(os.path.join(CURRENT_DIR, "UserApplications.ui"), self)
        self.username = username
        if hasattr(self, 'labelGetName'): self.labelGetName.setText(f"Welcome: {self.username}")
        self.buttonSelect.clicked.connect(self.upload_document)

    def upload_document(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Document")
        if file_path: print(f"File: {file_path}")

class UserInterview(QMainWindow):
    def __init__(self, username):
        super().__init__()
        loadUi(os.path.join(CURRENT_DIR, "UserInterview.ui"), self)
        self.username = username
        if hasattr(self, 'labelGetName'): self.labelGetName.setText(f"Welcome: {self.username}")

class UserMentor(QMainWindow):
    def __init__(self, username):
        super().__init__()
        loadUi(os.path.join(CURRENT_DIR, "UserMentor.ui"), self)
        self.username = username
        if hasattr(self, 'labelGetName'): self.labelGetName.setText(f"Welcome: {self.username}")

class UserPanel(QMainWindow):
    def __init__(self, logged_in_user="Guest"):
        super().__init__()
        loadUi(os.path.join(CURRENT_DIR, "UserPanel.ui"), self)
        self.username = logged_in_user 
        if hasattr(self, 'labelGetName'): self.labelGetName.setText(f"Welcome: {self.username}")
        
        self.buttonMainMenu.clicked.connect(self.main_menu)
        self.buttonUserApplication.clicked.connect(self.open_app)
        self.buttonInterview.clicked.connect(self.open_interview)
        self.buttonMentor.clicked.connect(self.open_mentor)
        self.buttonExit.clicked.connect(QCoreApplication.instance().quit)

    def open_app(self):
        self.app_win = UserApplication(self.username)
        self.app_win.show()

    def open_interview(self):
        self.int_win = UserInterview(self.username)
        self.int_win.show()

    def open_mentor(self):
        self.men_win = UserMentor(self.username)
        self.men_win.show()
    
    def main_menu(self):
        self.close()
        from login_menu import Login
        self.login_window = Login()
        self.login_window.show()

