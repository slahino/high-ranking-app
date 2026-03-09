from flask import Blueprint, request, render_template
from config import VOTE_START_DATE
from datetime import datetime

from app.services.database import get_connection

vote_bp = Blueprint("vote", __name__)

@vote_bp.route("/vote/<token>")
def vote(token):   
  
    now = datetime.now()
        
    if now <= VOTE_START_DATE:
        return render_template("ouverture_vote.html",date=VOTE_START_DATE,token=token)
      
    print(now)
    print(VOTE_START_DATE)
  
    if not token:
        return render_template("error.html")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT utilisateur_id
        FROM tokens
        WHERE token = %s
        AND actif = TRUE
        AND expiration > NOW()
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

    cursor.execute("UPDATE projets SET nb_votes = nb_votes + 1 WHERE id = %s",(projet_id,))

    cursor.execute("UPDATE utilisateurs SET a_vote = TRUE WHERE id = %s",(user_id,))

    cursor.execute("UPDATE tokens SET actif = FALSE WHERE utilisateur_id = %s",(user_id,))
    
    conn.commit()
    conn.close()

    return render_template("success.html")