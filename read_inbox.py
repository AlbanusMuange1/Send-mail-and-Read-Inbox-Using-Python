#!/usr/bin/env python3
import os
import imaplib
import email
from email.header import decode_header
from dotenv import load_dotenv

# Function to decode email subject
def decode_subject(raw_subject):
    decoded_subject, encoding = decode_header(raw_subject)[0]
    if isinstance(decoded_subject, bytes):
        decoded_subject = decoded_subject.decode(encoding or 'utf-8')
    return decoded_subject

# Load environment variables from config.env
load_dotenv("config.env")

# Retrieve environment variables
username = os.getenv("EMAIL_USERNAME")
password = os.getenv("EMAIL_PASSWORD")

# Gmail IMAP server configuration
imap_server = "imap.gmail.com"
imap_port = 993

try:
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(imap_server, imap_port)

    # Log in to the email account
    mail.login(username, password)

    # Select the mailbox (in this case, the inbox)
    mail.select("inbox")

    # Search for all emails in the inbox
    status, messages = mail.search(None, "ALL")

    if status == "OK":
        # Get the list of email IDs
        email_ids = messages[0].split()

        # Number of emails to retrieve (change as needed)
        num_emails_to_fetch = 5

        # Fetch and print the latest emails
        for email_id in email_ids[-num_emails_to_fetch:]:
            _, msg_data = mail.fetch(email_id, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            # Extract email information
            sender = msg.get("From")
            subject = decode_subject(msg.get("Subject"))
            date = msg.get("Date")

            print(f"From: {sender}\nSubject: {subject}\nDate: {date}\n")

    else:
        print(f"Failed to retrieve emails. Status: {status}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    try:
        # Logout and close the connection
        mail.logout()
    except NameError:
        pass
/root/python/sendMail/Send-mail-and-Read-Inbox-Using-Python