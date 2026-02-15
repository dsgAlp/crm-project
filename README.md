# crm-project
This project is a comprehensive Customer Relationship Management (CRM) and Application Tracking System developed using Python and PyQt6. It is designed to streamline the recruitment and advisory process by providing distinct interfaces for Administrators and Users.
🚀 Features
🔐 Multi-Role Access

Admin Panel: Full control over applications, interview scheduling, and mentor-advisor assignments.

User Panel: Personalized dashboard for candidates to track their application status, view mentor details, and upload documents.

📅 Calendar & Email Integration

Google Calendar API: Real-time synchronization of interview dates and events.

Automated Notifications: Integrated SMTP mailer to send automated interview reminders and status updates.

☁️ Cloud Database

Google Sheets API: Uses Google Sheets as a live, centralized database via gspread, allowing for easy data management without a complex SQL setup.

📁 Document Handling

File Management: Integrated QFileDialog for secure document uploading and tracking.

🛠️ Tech Stack
GUI Framework: PyQt6

Language: Python 3.x

APIs: Google Sheets API, Google Calendar API, SMTP

Libraries: gspread, oauth2client, google-api-python-client, python-dotenv

⚙️ Installation & Setup
Clone the Repository:

Bash
git clone https://github.com/yourusername/crm-project.git
cd crm-project
Install Dependencies:

Bash
pip install -r requirements.txt
Environment Variables:
Create a .env file in the root directory and add your credentials:

Codefragment
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password
SPREADSHEET_ID=your-google-sheet-id
Google Credentials:
Place your service_account.json file in the project directory to enable Google API access.

🔒 Security Note
The .env and *.json (credentials) files must be ignored in this repository for security purposes.

Always use App Passwords for SMTP and Service Accounts for Google API access.

👥 Contributors
@alparslan - Lead Developer & Designer
