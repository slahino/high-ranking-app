from flask import Blueprint, request, render_template
from config import VOTE_END_DATE

from app.services.database import get_connection

vote_bp = Blueprint("vote", __name__)

@vote_bp.route("/vote/<token>")
def vote(token):
  
    print("TOKEN =", token)
  
    #token = request.args.get("token")

    print("USER_ID =", id)
    print("PROJET_ID =", id)

    if not token:
        return render_template("error.html")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT utilisateur_id
        FROM tokens
        WHERE token = ?
        AND actif = 1
        AND expiration > datetime('now')
    """, (token,))

    token_data = cursor.fetchone()

    if not token_data:
        conn.close()
        return render_template("error.html")

    utilisateur_id = token_data[0]

    # RECUPERATION DES PROJETS
    cursor.execute("SELECT * FROM projets")
    projets = cursor.fetchall()

    conn.close()

    return render_template(
        "votes.html",
        user_id=utilisateur_id,
        projets=projets
    )



@vote_bp.route("/submit-vote", methods=["POST"])
def submit_vote():

    user_id = request.form.get("user_id")
    projet_id = request.form.get("projet_id")

    print("USER_ID =", user_id)
    print("PROJET_ID =", projet_id)

    if not user_id or not projet_id:
        return render_template("error.html")

    user_id = int(user_id)
    projet_id = int(projet_id)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE projets SET nb_votes = nb_votes + 1 WHERE id = ?",
        (projet_id,)
    )

    cursor.execute(
        "UPDATE utilisateurs SET a_vote = 1 WHERE id = ?",
        (user_id,)
    )

    cursor.execute(
    "UPDATE tokens SET actif = 0 WHERE utilisateur_id = ?",
    (user_id,)
    )
    
    conn.commit()
    conn.close()

    return render_template("success.html")