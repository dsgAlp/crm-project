from PyQt6.QtWidgets import QMainWindow, QLineEdit
from PyQt6.uic import loadUi
from PyQt6.QtCore import QCoreApplication
from database import connect_google_sheets

def password_show(self, state):
    if state == 2:
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Normal)
    else:           
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password)

def exit_button(self):
    QCoreApplication.instance().quit()

def login_control(self):
    username = self.txt_username.text().strip()
    password = self.txt_password.text().strip()
    
    try:
        sp = connect_google_sheets()
        sheet = sp.worksheet("Kullanicilar")
        data = sheet.get_all_records() 
        
        login_success = False
        for row in data:
            if str(row['UserName']) == username and str(row['Password']) == str(password):
                login_success = True
                role = str(row['Role']).lower()
                full_name = str(row.get('UserName', username)) 

                if role == "admin":
                    from admin_panel import AdminPanel
                    self.admin_panel = AdminPanel(username)
                    self.admin_panel.show()
                    self.close()
                
                elif role == "user":
                    from user_panel import UserPanel 
                    self.user = UserPanel(full_name) 
                    self.user.show()
                    self.close()  
                
                break 
        
        if not login_success:
            self.lbl_error.setText("Invalid Username or Password!")
            self.lbl_error.setStyleSheet("color: #E74C3C;")

    except Exception as e:
        print(f"Error: {e}")
        self.lbl_error.setText("Connection Error!")