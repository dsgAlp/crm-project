import os
import sys
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication
from PyQt6.uic import loadUi

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

class UserApplication(QMainWindow):
    def __init__(self, username="Guest"):
        super().__init__()
        ui_path = os.path.join(CURRENT_DIR, "UserApplications.ui")
        if os.path.exists(ui_path):
            loadUi(ui_path, self)
        
        self.current_user = username
        if hasattr(self, 'buttonSelect'):
            self.buttonSelect.clicked.connect(self.upload_document)
        
        if hasattr(self, 'pushButton'):
            self.pushButton.clicked.connect(self.send_application)

    def upload_document(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Document")
        if file_path:
            print(f"File: {file_path}")

    def send_application(self):
        if hasattr(self, 'lineEdit'):
            email = self.lineEdit.text()
            print(f"Sent: {email}")

class UserPanel(QMainWindow):
    def __init__(self, logged_in_user="Guest"):
        super().__init__()
        ui_path = os.path.join(CURRENT_DIR, "UserPanel.ui")
        if os.path.exists(ui_path):
            loadUi(ui_path, self)
        self.username = logged_in_user

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserApplication("oliver")
    window.show()
    sys.exit(app.exec())