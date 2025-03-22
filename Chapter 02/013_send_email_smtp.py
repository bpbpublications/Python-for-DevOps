# Script: Send Email Using SMTP
# Purpose: Demonstrates how to send an email with a text body using the `smtplib` and `email.message` modules.

import smtplib
from email.message import EmailMessage

# Create the email message object
msg = EmailMessage()

# Set email subject, sender, and recipient
msg['Subject'] = 'Subject'  # Replace 'Subject' with your email subject
msg['From'] = 'me@example.com'  # Replace with your email address
msg['To'] = 'user@example.com'  # Replace with the recipient's email address

# Set the email body from a text file
try:
    with open('/path/to/body.txt', 'r') as f:  # Replace with the actual path to your text file
        msg.set_content(f.read())
except FileNotFoundError:
    print("Error: The body file was not found.")
    exit(1)

# Send the email
try:
    with smtplib.SMTP('localhost') as s:  # Replace 'localhost' with your SMTP server if different
        s.send_message(msg)
    print("Email sent successfully.")
except smtplib.SMTPException as e:
    print(f"Failed to send email: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
