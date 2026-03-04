from flask import Blueprint, render_template
from services.database import get_connection
from datetime import datetime

resultat_bp = Blueprint("resultat", __name__)

@resultat_bp.route("/resultats")
def resultats():

    date_resultats = datetime(2026, 3, 3, 23, 21) 
    
    if datetime.now() <= date_resultats:
        return render_template("compte_a_rebours.html",
                               date=date_resultats.strftime("%Y-%m-%d %H:%M:%S"))
        
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute( """  
        SELECT nom, nb_votes
        FROM projets
        ORDER BY nb_votes DESC  
   """ )
   
    projets = cursor.fetchall()
    conn.close()

    total_votes = sum(p[1] for p in projets) if projets else 0
         
      
    return render_template("results.html", projets=projets, total_votes=total_votes)
    

  