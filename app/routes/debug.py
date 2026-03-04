from flask import Blueprint, render_template
from app.services.database import get_connection
from flask import jsonify

debug_bp = Blueprint("debug", __name__)

@debug_bp.route("/debug")
def debug():
  conn = get_connection()
  cur = conn.cursor()
  
  cur.execute("SELECT * FROM utilisateurs")
  utilisateurs = cur.fetchall()
  
  cur.close()
  conn.close()
  
  return jsonify(utilisateurs)
