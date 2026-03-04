import secrets
import sqlite3

def invalidate_tokens(user_id):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tokens WHERE utilisateur_id = ?",
        (user_id,)
    )

    conn.commit()
    conn.close()
    

def generate_token():
    return secrets.token_urlsafe(32)
