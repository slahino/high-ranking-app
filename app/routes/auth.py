from flask import Blueprint, request, render_template, redirect, url_for, flash
from app.services.database import get_connection
from app.services.token import generate_token, invalidate_tokens

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    message = ""
    category = ""

    if request.method == "POST":
        email = request.form.get("email").strip().lower()

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, a_vote FROM utilisateurs WHERE LOWER(email) = %s", (email,))
        user = cursor.fetchone()

        if user:
            #user_id = user[0]
            #a_vote = user[5]
            user_id, a_vote = user

            if a_vote:
                message = "Vous avez déjà voté."
                category = "primary"

            else:
                invalidate_tokens(user_id)

                token = generate_token()

                cursor.execute(
                    "INSERT INTO tokens (utilisateur_id, token, expiration, actif) VALUES (%s, %s, NOW() + INTERVAL '15 minutes', TRUE)",
                    (user_id, token)
                )
                
                conn.commit()
                conn.close()

                return redirect(url_for("vote.vote", token=token))
                #print("TOKEN:", token)
                
        else:
            message = "Email non autorisé."
            category = "danger"
      
        print("Resultat requte:", user)

        conn.commit()
        conn.close()

    return render_template("login.html", message=message, category=category)


