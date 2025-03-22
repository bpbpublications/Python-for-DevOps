# Script: 040_create_and_save_excel.py

# Importing the Workbook class from openpyxl to work with Excel files
from openpyxl import Workbook

# Create a new workbook and select the active worksheet
wb = Workbook()
sheet = wb.active

# Writing to specific cells
sheet['A1'] = 'Hello'
sheet['B1'] = 'World'

# Writing a row of data
sheet.append([1, 2, 3])

# Save the workbook to a file
wb.save("example.xlsx")
