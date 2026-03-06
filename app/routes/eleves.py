from flask import Blueprint
from app.services.database import get_connection
from flask import jsonify

eleves_bp = Blueprint("eleves", __name__)

@eleves_bp.route("/eleves")
def eleves():
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute("SELECT * FROM utilisateurs role = 'Eleves' AND ORDER BY nom ASC")
  resultats = cur.fetchall()
  
  cur.close()
  conn.close()
  
  return jsonify(resultats)
