# Script: 045_generate_pdf.py

# Importing the canvas module from reportlab to create PDF files
from reportlab.pdfgen import canvas

# Creating a new PDF canvas and setting the output file to "hello.pdf"
c = canvas.Canvas("hello.pdf")

# Drawing a string on the PDF at position (100, 750)
c.drawString(100, 750, "Hello, World!")

# Saving the PDF to finalize the document
c.save()
