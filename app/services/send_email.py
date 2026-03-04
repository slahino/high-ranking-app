import resend
import os

resend.api_key = os.environ["RESEND_API_KEY"]

def send_email(to_email, token):

    link = f"{os.environ.get('BASE_URL')}/vote/{token}"

    resend.Emails.send({
        "from": "Vote App <onboarding@resend.dev>",
        "to": [to_email],
        "subject": "Votre lien de vote",
        "html": f"""
        <h2>Lien de vote</h2>
        <p>Cliquez ici pour voter :</p>
        <a href="{link}">{link}</a>
        """
    })