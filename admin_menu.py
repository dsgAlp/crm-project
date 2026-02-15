import sys
import os
from PyQt6 import QtWidgets, uic
from googleapiclient.discovery import build
from google.oauth2 import service_account
import smtplib
from email.mime.text import MIMEText


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class AdminMenu(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        ui_path = os.path.join(BASE_DIR, "AdminMenu.ui")
        uic.loadUi(ui_path, self)
        
        # BUTTON CONNECTIONS
        self.buttonEvent.clicked.connect(self.load_calendar_data)   
        self.buttonExit.clicked.connect(self.exit_app)            
        self.buttonSendMail.clicked.connect(self.send_mail)        
        self.buttonReturn.clicked.connect(self.go_back)           
    
    def exit_app(self):
        """Exits the application."""
        sys.exit()

    def go_back(self):
        """Closes the current window."""
        self.close()

    def send_mail(self):
        """Sends an event reminder email to the selected attendee."""
        try:
            current_row = self.tableWidget.currentRow()
        except Exception as e:
            print(f"Table selection error: {e}")
            return

        if current_row == -1:
            print("Please select a row from the table first!")
            return

        event_name = self.tableWidget.item(current_row, 0).text()
        attendee_email = self.tableWidget.item(current_row, 2).text()

        if attendee_email == "None":
            print("The selected event has no attendee email.")
            return

        sender_email = "xxxxxxxxxxxxxxx"
        app_password = "xxxxxxxxxxxx" 

        # Email Content
        body = f"Hello,\n\nThis is a notification regarding the event: {event_name}.\nDesigned by @alparslan."
        message = MIMEText(body)
        message['Subject'] = 'Event Reminder'
        message['From'] = sender_email
        message['To'] = attendee_email

        # Connect to server and send
        try:
            with smtplib.SMTP_SSL('xxx.gmail.com', xxxx as server:
                server.login(sender_email, app_password)
                server.send_message(message)
            print(f"Email successfully sent to {attendee_email}!")
        except Exception as e:
            print(f"Email Error: {e}")

    def load_calendar_data(self):
        """Fetches events from Google Calendar and populates the table."""
        try:
            # Connect to JSON credentials
            json_path = os.path.join(BASE_DIR, 'xxxxxx.json')
            
            SCOPES = ['https://www.googleapis.com/auth/xxxxxxxxxxxa']
            creds = service_account.Credentials.from_service_account_file(
                    json_path, scopes=SCOPES)
            service = build('calendar', 'v3', credentials=creds)

            # API Call
            events_result = service.events().list(
               # calendarId='xxxxxxxxxxxxxx', 
                timeMin="2025-01-01T00:00:00Z",
                maxResults=20, 
                singleEvents=True,
                orderBy='startTime').execute()
            
            events = events_result.get('items', [])
            self.tableWidget.setRowCount(len(events)) 
            
            for row, event in enumerate(events):
                summary = event.get('summary', 'No Title')
                start = event['start'].get('dateTime', event['start'].get('date'))
                organizer = event.get('organizer', {}).get('email', 'Unknown')
                attendees = event.get('attendees', [])
                attendee_mail = attendees[0].get('email', 'None') if attendees else "None"
                
                # Populating English items into table
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(summary)))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(start)))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(attendee_mail)))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(organizer)))
                
            print(f"System: {len(events)} events loaded successfully.")
                
        except Exception as e:
            print(f"Calendar Error: {e}")

