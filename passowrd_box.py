import os
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

current_dir = os.path.dirname(os.path.abspath(__file__))

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(current_dir, "loginDesign.ui"), self)
        self.label_forget.linkActivated.connect(self.open_password_box)

    def open_password_box(self):
        self.password_dialog = uic.loadUi(os.path.join(current_dir, "PasswordBox.ui"))
        self.password_dialog.setModal(True)
        self.password_dialog.buttonApprove.clicked.connect(self.verify_passwords)
        
        self.password_dialog.show()

    def verify_passwords(self):
        new_p = self.password_dialog.lineEdit.text()
        confirm_p = self.password_dialog.lineEdit_2.text()

        if new_p == confirm_p and new_p != "":
            print("Password Changed!")
            self.password_dialog.close()
        else:
            print("Error: Passwords do not match!")

