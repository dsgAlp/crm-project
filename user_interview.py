import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt6.uic import loadUi
from database import connect_google_sheets

class UserInterview(QMainWindow):
    def __init__(self, logged_in_user): 
        super().__init__()
        loadUi("UserInterview.ui", self)
        self.username = logged_in_user.strip().lower()
        
        if hasattr(self, 'tableWidget'):
            self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            
        self.load_user_specific_data()

    def load_user_specific_data(self):
        """Fetches interview records and filters them by the logged-in username."""
        try:
            ss = connect_google_sheets()
            sheet = ss.worksheet("Interviews")
            all_rows = sheet.get_all_records()
            
            filtered_data = []
            for entry in all_rows:
                sheets_name = str(entry.get('FULL-NAME', '')).strip().lower()
                if sheets_name == self.username:
                    filtered_data.append(entry)

            self.display_filtered_data(filtered_data)
        except Exception as e:
            print(f"Error fetching data: {e}")

    def display_filtered_data(self, data_list):
        """Populates the table with the user's project status."""
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(data_list))
        self.tableWidget.setHorizontalHeaderLabels(["Project Sent Date", "Full Name", "Project Status"])

        for row, entry in enumerate(data_list):
            date_sent = str(entry.get('PROJECT-SENT-DATE', '')).strip()
            date_received = str(entry.get('PROJECT-RECEIVED-DATE', '')).strip()

            self.tableWidget.setItem(row, 0, QTableWidgetItem(date_sent))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.username.title()))

            # Status Message Update
            status_text = f"Received - {date_received}" if date_received and date_received.lower() not in ["nan", "", "none"] else "Awaiting Project Delivery"
            self.tableWidget.setItem(row, 2, QTableWidgetItem(status_text))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

