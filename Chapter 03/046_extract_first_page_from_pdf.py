# Script: 046_extract_first_page_from_pdf.py

# Importing PdfFileReader and PdfFileWriter from PyPDF2 to work with PDF files
from PyPDF2 import PdfFileReader, PdfFileWriter

# Reading the input PDF file
reader = PdfFileReader('example.pdf')

# Creating a PdfFileWriter object to write the extracted pages
writer = PdfFileWriter()

# Adding the first page (page 0) from the reader to the writer
writer.addPage(reader.getPage(0))

# Saving the output PDF with the extracted page
with open('output.pdf', 'wb') as out_file:
    writer.write(out_file)
