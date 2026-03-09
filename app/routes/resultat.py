from flask import Blueprint, render_template
from app.services.database import get_connection
from datetime import datetime, timedelta
from config import RESULT_START_DATE

resultat_bp = Blueprint("resultat", __name__)


@resultat_bp.route("/resultats")
def resultats():
  
  resultats = datetime(2026, 3, 9, 6, 0, 0) 
  
  now = datetime.now() + timedelta(hours=1)
  
  if now < resultats:
   return render_template("compte_a_rebours.html",target=resultats.timestamp(),server_time=now.timestamp())
        
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
    

  