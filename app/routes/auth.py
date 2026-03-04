from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.services.database import get_connection
from app.services.token import generate_token, invalidate_tokens
from app.services.send_email import send_email

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    message = ""
    category = ""

    if request.method == "POST":
        email = request.form.get("email").strip().lower()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM utilisateurs WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            user_id = user[0]
            a_vote = user[5]

            if a_vote:
                message = "Vous avez déjà voté."
                category = "primary"

            else:
                invalidate_tokens(cursor, user_id)

                token = generate_token()

                cursor.execute(
                    "INSERT INTO tokens (utilisateur_id, token, expiration, actif) VALUES (?, ?, datetime('now', '+15 minutes'), 1)",
                    (user_id, token)
                )

                send_email(email, token)

                message = "Lien envoyé par email."
                category = "success"
        else:
            message = "Email non autorisé."
            category = "danger"

        conn.commit()
        conn.close()

    return render_template("login.html", message=message, category=category)


