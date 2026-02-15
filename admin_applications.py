import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.uic import loadUi
from database import connect_google_sheets

class ApplicationsPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("AdminApplications.ui", self)
        
        self.all_data = []  
        self.labelArama.mousePressEvent = lambda event: self.labelArama.clear()
        self.tumBasvurularGetir.clicked.connect(self.load_table_data)
        self.buttonAra.clicked.connect(self.search_function)
        self.buttonTanimlanan.clicked.connect(lambda: self.filter_by_column("assigned"))
        self.buttonTanimlanmayan.clicked.connect(lambda: self.filter_by_column("unassigned"))
        
        self.buttonMukkerrer.clicked.connect(self.filter_duplicates)
        self.buttonOncekiVit.clicked.connect(self.check_previous_vit)
        self.buttonFarkli.clicked.connect(self.filter_different_records)
        self.buttonBasvuru.clicked.connect(self.filter_applications) 
        
        self.buttonTercihler.clicked.connect(self.close) 
        self.buttonExit.clicked.connect(lambda: QApplication.instance().quit())

    def load_table_data(self):
        try:
            ss = connect_google_sheets()
            sheet = ss.worksheet("Basvurular")
            self.all_data = sheet.get_all_records()
            self.display_data(self.all_data)
        except Exception as e:
            print(f"Error: {e}")

    def display_data(self, data_list):
        if not data_list: return
        headers = list(data_list[0].keys())
        self.tableWidget.setColumnCount(len(headers))
        self.tableWidget.setHorizontalHeaderLabels(headers)
        self.tableWidget.setRowCount(len(data_list))

        for row, entry in enumerate(data_list):
            self.tableWidget.setRowHidden(row, False)
            for col, key in enumerate(headers):
                val = str(entry.get(key, ''))
                self.tableWidget.setItem(row, col, QTableWidgetItem(val))
        self.tableWidget.resizeColumnsToContents()

    def search_function(self):
        query = self.labelArama.text().strip().lower()
        if not self.all_data: return

        for r in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(r, 1) # Name column
            hide = not (item and query in item.text().lower())
            self.tableWidget.setRowHidden(r, hide)
        self.labelArama.clear()

    def filter_by_column(self, status):
        if not self.all_data: return
        
        for r in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(r, 8) 
            text = item.text().strip() if item else ""
            
            if status == "assigned":
                self.tableWidget.setRowHidden(r, text == "")
            else:
                self.tableWidget.setRowHidden(r, text != "")

    def filter_duplicates(self):
        row_count = self.tableWidget.rowCount()
        if row_count == 0: return

        all_rows = []
        counter = {}

        for r in range(row_count):
            name = self.tableWidget.item(r, 1).text().strip().lower() if self.tableWidget.item(r, 1) else ""
            mail = self.tableWidget.item(r, 2).text().strip().lower() if self.tableWidget.item(r, 2) else ""
            key = (name, mail)
            all_rows.append(key)
            if name and mail:
                counter[key] = counter.get(key, 0) + 1

        for r in range(row_count):
            current_key = all_rows[r]
            is_duplicate = counter.get(current_key, 0) > 1
            self.tableWidget.setRowHidden(r, not is_duplicate)

    def check_previous_vit(self):
        try:
            ss = connect_google_sheets()
            v1 = {str(d['Mail']).lower() for d in ss.worksheet("VIT1").get_all_records()}
            v2 = {str(d['Mail']).lower() for d in ss.worksheet("VIT2").get_all_records()}
            
            for r in range(self.tableWidget.rowCount()):
                mail = self.tableWidget.item(r, 2).text().lower()
                self.tableWidget.setRowHidden(r, not (mail in v1 or mail in v2))
        except Exception as e:
            print(f"Error checking VIT: {e}")

    def filter_different_records(self):
        try:
            ss = connect_google_sheets()
            v1_mails = {str(d.get('Mail', '')).strip().lower() for d in ss.worksheet("VIT1").get_all_records()}
            v2_mails = {str(d.get('Mail', '')).strip().lower() for d in ss.worksheet("VIT2").get_all_records()}
            
            diff_mails = v1_mails.symmetric_difference(v2_mails)
            
            for r in range(self.tableWidget.rowCount()):
                mail_item = self.tableWidget.item(r, 2)
                if mail_item:
                    mail = mail_item.text().strip().lower()
                    self.tableWidget.setRowHidden(r, mail not in diff_mails)
        except Exception as e:
            print(f"Error: {e}")

    def filter_applications(self):
        visible = set()
        for r in range(self.tableWidget.rowCount()):
            mail = self.tableWidget.item(r, 2).text()
            if mail in visible:
                self.tableWidget.setRowHidden(r, True)
            else:
                visible.add(mail)
                self.tableWidget.setRowHidden(r, False)

