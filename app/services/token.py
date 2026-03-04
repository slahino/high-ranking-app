import secrets
import psycopg2
import os 

DATABASE_URL = os.environ.get("DATABASE_URL")



def generate_token():
    return secrets.token_urlsafe(32)
  
  

def invalidate_tokens(user_id):
  conn = psycopg2.connect(DATABASE_URL,timeout=10)
  cursor = conn.cursor()
  
  cursor.execute(
      "DELETE FROM tokens WHERE utilisateur_id = %s",
      (user_id,)
  )

  conn.commit()
  conn.close()