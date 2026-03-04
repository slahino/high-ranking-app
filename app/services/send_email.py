import smtplib
from email.mime.text import MIMEText
import os

def send_email(to_email, token):

    sender = os.environ.get("EMAIL_USER")
    password = os.environ.get("EMAIL_PASSWORD")

    link = f"{os.environ.get('BASE_URL')}/vote/{token}"

    message = MIMEText(f"Voici votre lien de vote : {link}")
    message["Subject"] = "Lien de vote"
    message["From"] = sender
    message["To"] = to_email

    # Connexion Gmail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(sender, password)

    server.sendmail(sender, to_email, message.as_string())

    server.quit()