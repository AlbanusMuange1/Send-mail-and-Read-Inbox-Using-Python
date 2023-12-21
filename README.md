# Email Automation Scripts

This repository contains Python scripts for sending emails and reading inbox messages using Gmail. The two main scripts are `send_email.py` and `read_inbox.py`.

## Send Email Script

### Overview

The `send_email.py` script allows you to send emails using your Gmail account. It utilizes the `smtplib` library to establish a secure connection with the Gmail SMTP server.

### Prerequisites

- Python 3.x
- `secure-smtplib` library (`pip install secure-smtplib`)

### Configuration

1. Replace the placeholder values in the script with your own email addresses, subject, and message.
2. Configure the Gmail SMTP server settings.
3. **Note:** Using an "App Password" or other secure authentication methods for Gmail is recommended.

### Usage

Run the script:

```bash
python send_email.py
```

## Read Inbox Script

### Overview

The `read_inbox.py` script allows you to read emails from your Gmail inbox using the IMAP protocol. It utilizes the `imaplib` library to connect to the Gmail IMAP server.

### Prerequisites

- Python 3.x
- `python-dotenv` library (`pip install python-dotenv`)

### Configuration

1. Create a `config.env` file with your Gmail username and password:

    ```env
    EMAIL_USERNAME=your_email@gmail.com
    EMAIL_PASSWORD=your_gmail_password
    ```

2. Configure the Gmail IMAP server settings.
3. **Note:** Using environment variables and secure authentication methods for Gmail is recommended.

### Usage

Run the script:

```bash
python read_inbox.py
```

## Security Considerations

- Keep your email credentials secure.
- Consider using environment variables for sensitive information.
- For Gmail, enable "Less secure app access" or use App Passwords.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
