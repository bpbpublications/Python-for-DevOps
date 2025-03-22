# Script: 042_apply_styles_and_formulas.py

# Importing the Workbook class and Font style from openpyxl
from openpyxl import Workbook
from openpyxl.styles import Font

# Create a new workbook and select the active worksheet
wb = Workbook()
sheet = wb.active

# Applying styles
bold_font = Font(bold=True)
sheet['A1'].font = bold_font  # Applying bold font to cell A1

# Working with formulas
sheet['C1'] = '=SUM(A1:B1)'  # Using the SUM formula to sum the values in A1 and B1

# Save the workbook to a file
wb.save("example.xlsx")
