import psycopg2
import csv
import os 

#DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_URL = "postgresql://vote_condorcet_db_user:ofHxBK0dFwRm0zBZ0GdmYE579FiYzsEj@dpg-d6jvtacr85hc73br6clg-a.oregon-postgres.render.com/vote_condorcet_db"

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

cursor.execute("""
  CREATE TABLE IF NOT EXISTS utilisateurs (
      id SERIAL PRIMARY KEY,
      nom TEXT NOT NULL,
      prenom TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      role TEXT NOT NULL,
      a_vote BOOLEAN DEFAULT FALSE
  )
  """)

cursor.execute("DELETE FROM Utilisateurs")

with open("professeurs.csv", newline="", encoding="utf-8-sig") as file:
  reader = csv.DictReader(file, delimiter=";")
  
  for row in reader:
    cursor.execute("""
    INSERT INTO utilisateurs (id, nom, prenom, email, role, a_vote)
    VALUES (%s,%s,%s,%s,%s,%s)
      """, (
        row["id"],
        row["nom"],
        row["prenom"],
        row["email"],
        row["role"],
        False
      ))

  
print("Table utilisteurs initialisée avec succès.")
  
cursor.execute("""
  CREATE TABLE IF NOT EXISTS tokens (
      id SERIAL PRIMARY KEY,
      utilisateur_id INTEGER NOT NULL,
      token TEXT NOT NULL,
      expiration TIMESTAMP NOT NULL,
      actif BOOLEAN DEFAULT TRUE
  )
  """)
  
cursor.execute("""
  CREATE TABLE IF NOT EXISTS projets (
      id SERIAL PRIMARY KEY,
      nom TEXT NOT NULL,
      image TEXT NOT NULL,
      description TEXT NOT NULL,
      nb_votes INTEGER DEFAULT 0
  )
  """)
  
conn.commit()
conn.close()
  
print("Table créees avec succès.")
