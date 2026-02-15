import os
import sys
import controller # controller.py dosyanın aynı klasörde olması gerekir
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow

current_dir = os.path.dirname(os.path.abspath(__file__))

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(current_dir, "loginDesign.ui"), self)
        
        self.btn_login.clicked.connect(lambda: controller.login_control(self))
        self.btn_exit.clicked.connect(lambda: controller.exit_button(self))
        self.chk_show.stateChanged.connect(lambda state: controller.password_show(self, state))
        self.label_forget.linkActivated.connect(self.open_password_box)

    def open_password_box(self):
        self.password_dialog = uic.loadUi(os.path.join(current_dir, "PasswordBox.ui"))
        self.password_dialog.setModal(True)
        if hasattr(self.password_dialog, 'pushButton'):
            self.password_dialog.pushButton.clicked.connect(self.verify_passwords)
        self.password_dialog.show()

    def verify_passwords(self):
        p1 = self.password_dialog.lineEdit.text()
        p2 = self.password_dialog.lineEdit_2.text()
        if p1 == p2 and p1 != "":
            print("Şifre güncellendi!")
            self.password_dialog.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    sys.exit(app.exec())