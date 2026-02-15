import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from PyQt6.uic import loadUi
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class UserMentor(QMainWindow):
    def __init__(self, logged_in_user):
        super().__init__()
        loadUi("UserMentor.ui", self)
        self.username = logged_in_user
        
        # Load data automatically upon initialization
        self.load_mentor_data()

    def load_mentor_data(self):
        try:
            scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
          
            creds = ServiceAccountCredentials.from_json_keyfile_name("xxxxxxxxxx", scope)
            client = gspread.authorize(creds)
            
            sheet_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Update with your actual sheet ID
            spreadsheet = client.open_by_key(sheet_id)
            
            sheet = spreadsheet.worksheet("xxxxxxxxxx") 
            
            all_data = sheet.get_all_records()
            search_name = str(self.username).strip().lower()
            filtered_results = []

           
            for row in all_data:
               
                if str(row.get("Isim Soyisim", "")).strip().lower() == search_name:
                    filtered_results.append(row)
            
            self.tableWidget.setRowCount(len(filtered_results))

            for row_idx, row_data in enumerate(filtered_results):
                # Updating terminology: Mentor -> Advisor
                advisor = str(row_data.get("Mentoru", "Not Assigned"))
                date = str(row_data.get("Date", ""))
                email = str(row_data.get("Mentor Email", ""))

                self.tableWidget.setItem(row_idx, 0, QTableWidgetItem(advisor))
                self.tableWidget.setItem(row_idx, 1, QTableWidgetItem(date))
                self.tableWidget.setItem(row_idx, 2, QTableWidgetItem(email))
            
            print(f"System: {len(filtered_results)} records loaded for {self.username}.")

        except Exception as e:
            print(f"Error loading mentor data: {e}")

