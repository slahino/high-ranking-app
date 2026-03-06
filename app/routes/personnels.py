from flask import Blueprint
from app.services.database import get_connection
from flask import jsonify

personnels_bp = Blueprint("personnels", __name__)

@personnels_bp.route("/personnels")
def personnels():
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute("SELECT * FROM utilisateurs WHERE role = 'Personnels' AND ORDER BY nom ASC")
  resultats = cur.fetchall()
  
  cur.close()
  conn.close()
  
  return jsonify(resultats)
