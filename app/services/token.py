import secrets
import sqlite3

def generate_token():
    return secrets.token_urlsafe(32)
  
  

def invalidate_tokens(user_id):
    conn = sqlite3.connect("database.db", timeout=10)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM tokens WHERE utilisateur_id = %s",
        (user_id,)
    )

    conn.commit()
    conn.close()