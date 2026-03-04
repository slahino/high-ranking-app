import requests
import os

def send_email(to_email, token):

    url = "https://api.brevo.com/v3/smtp/email"

    link = f"{os.environ.get('BASE_URL')}/vote/{token}"

    payload = {
        "sender": {
            "name": "Vote Condorcet",
            "email": "vote@condorcet.fr"
        },
        "to": [
            {"email": to_email}
        ],
        "subject": "Lien pour voter",
        "htmlContent": f"""
        <h2>Vote du lycée Condorcet</h2>
        <p>Cliquez sur le lien ci-dessous pour voter :</p>
        <a href="{link}">{link}</a>
        """
    }

    headers = {
        "accept": "application/json",
        "api-key": os.environ.get("BREVO_API_KEY"),
        "content-type": "application/json"
    }

    requests.post(url, json=payload, headers=headers)