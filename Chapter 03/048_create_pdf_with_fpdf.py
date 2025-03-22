# Script: 048_create_pdf_with_fpdf.py

# Importing the FPDF class from the fpdf module to create PDF files
from fpdf import FPDF

# Creating an instance of the FPDF class
pdf = FPDF()

# Adding a page to the PDF document
pdf.add_page()

# Setting the font for the PDF content (Arial, size 12)
pdf.set_font("Arial", size=12)

# Adding a cell with the text "Welcome to FPDF!" in the center of the page
pdf.cell(200, 10, txt="Welcome to FPDF!", ln=True, align='C')

# Saving the PDF to a file named "simple_demo.pdf"
pdf.output("simple_demo.pdf")
