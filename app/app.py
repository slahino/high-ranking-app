from flask import Flask

from routes.auth import auth_bp
from routes.vote import vote_bp
from routes.resultat import resultat_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(vote_bp)
app.register_blueprint(resultat_bp)

if __name__ == "__main__":
    app.run(debug=True)

