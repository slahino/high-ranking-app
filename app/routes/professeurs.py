from flask import Blueprint
from app.services.database import get_connection
from flask import jsonify

professeurs_bp = Blueprint("professeurs", __name__)

@professeurs_bp.route("/professeurs")
def professeurs():
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute("SELECT * FROM utilisateurs WHERE role = 'Professeurs' AND ORDER BY nom ASC")
  resultats = cur.fetchall()
  
  cur.close()
  conn.close()
  
  return jsonify(resultats)
