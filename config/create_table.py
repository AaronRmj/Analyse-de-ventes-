# on importe la fonction get_connexion pour l'utiliser afin de creer des tables
from database import get_connexion
import sqlite3
conn = get_connexion()
cursor = conn.cursor() 
try:


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilisateur (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT,
            email TEXT,
            password TEXT,
            role TEXT
        )
    """
    )

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vente(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_vente TEXT NOT NULL,
            numero_facture TEXT UNIQUE,
            client TEXT,
            ville TEXT,
            categorie TEXT,
            produit TEXT,
            mode_paiement TEXT,
            vendeur TEXT,
            prix_unitaire INTEGER,
            quantite INTEGER
        )
    """)
    print("Base crée avec succès")
    conn.commit()

except sqlite3.Error as e:
    print("Erreur lors de la creation")

finally:
    if conn:
        conn.close()
