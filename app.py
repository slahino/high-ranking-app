from flask import Flask


from app.routes.auth import auth_bp
from app.routes.vote import vote_bp
from app.routes.resultat import resultat_bp


app = Flask(__name__, template_folder="app/templates")

import os
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

app.register_blueprint(auth_bp)
app.register_blueprint(vote_bp)
app.register_blueprint(resultat_bp)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/healthz")
def health():
    return "OK", 200


