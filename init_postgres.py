import psycopg2
import os 

conn = psycopg2.connect("postgresql://vote_condorcet_db_user:ofHxBK0dFwRm0zBZ0GdmYE579FiYzsEj@dpg-d6jvtacr85hc73br6clg-a.oregon-postgres.render.com/vote_condorcet_db")
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
