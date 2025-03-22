# Script: 047_extract_text_from_pdf.py

# Importing the extract_text function from pdfminer.high_level to extract text from PDF files
from pdfminer.high_level import extract_text

# Extracting text from the specified PDF file
text = extract_text('example.pdf')

# Printing the extracted text
print(text)
