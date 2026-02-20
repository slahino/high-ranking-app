import smtplib
from email.mime.text import MIMEText
from config import BASE_URL, EMAIL_SENDER, EMAIL_PASSWORD

def send_email(to_email, token):
    link = f"{BASE_URL}/vote?token={token}"

    body = f"""
Bonjour,

Cliquez sur ce lien pour voter :

{link}

Ce lien est personnel et utilisable une seule fois.
"""

    msg = MIMEText(body)
    msg["Subject"] = "Vote Lycée"
    msg["From"] = EMAIL_SENDER
    msg["To"] = to_email

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
