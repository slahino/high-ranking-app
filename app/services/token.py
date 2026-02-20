import secrets
from services.database import get_connection

def generate_token():
    return secrets.token_urlsafe(32)

def invalidate_tokens(cursor, utilisateur_id):
    cursor.execute(
        "DELETE FROM tokens WHERE utilisateur_id = ?",
        (utilisateur_id,)
    )

