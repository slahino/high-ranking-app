import sqlite3

def init_db():
  conn = sqlite3.connect("database.db")
  cursor = conn.cursor()

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS utilisateurs (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nom TEXT NOT NULL,
      prenom TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      role TEXT NOT NULL,
      a_vote BOOLEAN DEFAULT 0
  )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS tokens (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      utilisateur_id INTEGER NOT NULL,
      token TEXT NOT NULL,
      expiration DATETIME NOT NULL,
      actif BOOLEAN DEFAULT 1
  )
  """)

  cursor.execute("""
  CREATE TABLE IF NOT EXISTS projets (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nom TEXT NOT NULL,
      image TEXT NOT NULL,
      description TEXT NOT NULL,
      nb_votes INTEGER DEFAULT 0
  )
  """)
  
  

 
  conn.commit()
  conn.close()

  print("Base initialisée avec succès.")
