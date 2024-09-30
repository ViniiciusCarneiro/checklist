import openpyxl
from datetime import datetime

def log_to_excel(file_name, table_name, rows_inserted):
    if rows_inserted == 0:
        return
    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sheet.append([current_time, table_name, rows_inserted])

    workbook.save(file_name)