# Script: 035_send_email_alert.py
# Purpose: Demonstrates how to send an email alert using `smtplib` and `email.mime.text`.

import smtplib
from email.mime.text import MIMEText

def send_alert(email_subject, email_body):
    """
    Sends an email alert with the given subject and body.

    Args:
        email_subject (str): The subject of the email.
        email_body (str): The body content of the email.
    """
    # Create a MIMEText object to represent the email
    msg = MIMEText(email_body)
    msg['Subject'] = email_subject
    msg['From'] = 'from@example.com'  # Replace with the sender's email
    msg['To'] = 'to@example.com'  # Replace with the recipient's email
    
    # Connect to the SMTP server and send the message
    try:
        with smtplib.SMTP('localhost') as server:
            server.send_message(msg)
        print("Alert email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
# send_alert('Test Subject', 'This is the body of the email.')
