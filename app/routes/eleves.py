from flask import Blueprint
from app.services.database import get_connection
from flask import jsonify

debug_bp = Blueprint("eleves", __name__)

@debug_bp.route("/eleves")
def eleves(email):
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute("SELECT * FROM utilisateurs WHERE LOWER(email) = LOWER(%s) AND WHERE role = 'Eleves' AND ORDER BY nom ASC", (email,))
  resultats = cur.fetchone()
  
  cur.close()
  conn.close()
  
  return jsonify(resultats)
