import smtplib
import os
from email.message import EmailMessage

def send_email(subject, content, to_email):
    """
    Sends an email using Gmail's SMTP server.
    
    :param subject: Subject of the email
    :param content: Body content of the email
    :param to_email: Recipient's email address
    """
    # Your email configuration
    your_email = "your_email@gmail.com"
    your_password = os.getenv('PASSWORD')  # Retrieve the password from an environment variable
    
    if not your_password:
        print("Error: Email password not set in environment variable 'PASSWORD'.")
        return
    
    # Create the email message
    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["From"] = your_email
    msg["To"] = to_email

    try:
        # Establish a connection to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Upgrade to a secure connection
        server.login(your_email, your_password)
        server.send_message(msg)
        server.quit()
        print(f"Email successfully sent to {to_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
send_email("Reminder", "Don't forget our meeting tomorrow!", "recipient@example.com")
