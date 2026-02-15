import gspread
from oauth2client.service_account import ServiceAccountCredentials

def connect_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("xxxxxxxxxxxxxxxxx", scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") 
    return spreadsheet

def connect_google_sheets():
    # Yetki ayarları
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("xxxxxxxxxxxxxxxx", scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_key("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx") 
    return spreadsheet

def get_all_data():
    try:
        ss = connect_google_sheets()
        sheet = ss.worksheet("xxxxxxxx")
        return sheet.get_all_records()
    except Exception as e:
        print(f"Veri çekme hatası: {e}")
        return []