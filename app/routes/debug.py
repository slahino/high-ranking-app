from flask import Blueprint, render_template
from app.services.database import get_connection
from flask import jsonify

debug_bp = Blueprint("debug", __name__)

@debug_bp.route("/debug/<email>")
def debug(email):
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute("SELECT * FROM utilisateurs WHERE LOWER(email) = LOWER(%s)", (email,))
  resultats = cur.fetchone()
  
  cur.close()
  conn.close()
  
  return jsonify(resultats)
