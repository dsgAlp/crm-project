from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic import loadUi
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtGui import QIcon  # Eksik olan buydu, ekledim.
from admin_interview import InterviewPage
from admin_applications import ApplicationsPage
from admin_menu import AdminMenu
from admin_advisor import AdvisorPage


class AdminPanel(QMainWindow):
    def __init__(self,username):
        super().__init__()
        loadUi("AdministratorPanel.ui", self)
        self.current_user = username
        
        first_name = self.current_user.split()[0] if self.current_user else "Admin"
        self.labelGetName.setText(f"Welcome: {first_name}")
        self.buttonInterview.clicked.connect(self.open_interview)
        self.buttonAdvisor.clicked.connect(self.open_advisor)
        self.buttonApplications.clicked.connect(self.open_applications)
        self.buttonAdmin.clicked.connect(self.open_admin_menu)
        self.buttonExit.clicked.connect(self.exit_application)
        self.buttonMainMenu.clicked.connect(self.back_to_main_menu)
        
        self.buttonApplications.setIcon(QIcon("icons/resume.png"))
        self.buttonInterview.setIcon(QIcon("icons/interview.png"))
        self.buttonAdvisor.setIcon(QIcon("icons/advisory.png"))
        self.buttonAdmin.setIcon(QIcon("icons/admin.png"))
        self.buttonMainMenu.setIcon(QIcon("icons/mainmenu.png"))
        self.buttonExit.setIcon(QIcon("icons/exit.png"))
        
    
    def open_interview(self):
        self.inter_win = InterviewPage()
        self.inter_win.show()

    def open_advisor(self):  
        self.mentor_win = AdvisorPage()
        self.mentor_win.show()

    def open_applications(self):
        self.apps_win = ApplicationsPage()
        self.apps_win.show()

    def open_admin_menu(self):
        self.admin_menu_win = AdminMenu()
        self.admin_menu_win.show()

    def exit_application(self):
        QCoreApplication.instance().quit()

    def back_to_main_menu(self):
        try:
            from login_menu import Login
            self.main_menu = Login()
            self.main_menu.show()
            self.close()
        except Exception as e:
            print(f"Error occurred: {e}")