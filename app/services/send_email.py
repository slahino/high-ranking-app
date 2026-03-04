import smtplib
from email.mime.text import MIMEText
import os

def send_email(to_email, token):

    link = f"https://vote-condorcet-belevedere.onrender.com/vote?token={token}"

    message = MIMEText(f"""
Bonjour,

Voici votre lien de vote :

{link}

Ce lien expire dans 10 minutes.
""")

    message["Subject"] = "Lien de vote"
    message["From"] = os.environ["EMAIL_USER"]
    message["To"] = to_email

    try:
        print("Connexion SMTP...")

        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)

        server.starttls()

        print("Login SMTP...")

        server.login(
            os.environ["EMAIL_USER"],
            os.environ["EMAIL_PASSWORD"]
        )

        print("Envoi email...")

        server.sendmail(
            os.environ["EMAIL_USER"],
            to_email,
            message.as_string()
        )

        server.quit()

        print("Email envoyé avec succès")

    except Exception as e:
        print("ERREUR EMAIL :", e)