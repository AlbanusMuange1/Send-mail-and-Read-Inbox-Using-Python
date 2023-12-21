#!/usr/bin/env python3
import smtplib
import ssl
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables from config.env
load_dotenv("config.env")

def send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, username, password):
    # Create a MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the MIME object
    msg.attach(MIMEText(message, 'plain'))

    # Establish a secure connection with the SMTP server
    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            # Log in to the SMTP server
            server.login(username, password)

            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Retrieve environment variables
sender_email = os.getenv("EMAIL_USERNAME")
receiver_email = "albanusmuangemutunga@gmail.com"
subject = "Test Email"
message = "This is a test email sent from Python."

# Gmail SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 465

# Retrieve password securely from environment variable
password = os.getenv("EMAIL_PASSWORD")

# Send the email
send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, sender_email, password)
