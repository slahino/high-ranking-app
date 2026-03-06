from flask import Flask
import os

from app.routes.auth import auth_bp
from app.routes.vote import vote_bp
from app.routes.resultat import resultat_bp
from app.routes.professeurs import professeurs_bp
from app.routes.eleves import eleves_bp
from app.routes.personnels import personnels_bp
from init_db import init_db 

app = Flask(__name__,template_folder="app/templates")

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


with app.app_context():
    init_db()

app.register_blueprint(auth_bp)
app.register_blueprint(vote_bp)
app.register_blueprint(resultat_bp)
app.register_blueprint(professeurs_bp)
app.register_blueprint(eleves_bp)
app.register_blueprint(personnels_bp)

@app.route("/healthz")
def health():
    return "OK", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)