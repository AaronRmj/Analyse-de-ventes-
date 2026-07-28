import sqlite3
from config.database import get_connexion
from utils.security import hash_password

# logique de connexion
def login(mail, password):
    try:
        conn = get_connexion()
        cursor = conn.cursor()

        #hash le pass
        hashed_password = hash_password(password)

        #recuperer mail et pass correspondant
        cursor.execute("SELECT nom, role FROM utilisateur WHERE email=? AND password=?", (mail, hashed_password))
        user = cursor.fetchone()

        #fermer la connexion
        cursor.close()

        return user
    
    except sqlite3.Error as e:
        print("Utilisateur non existant")

    finally: 
        if conn:
            conn.close()



def register(nom, email, password, role="admin"):

    try:
        #creer une connexion
        conn = get_connexion()
        cursor = conn.cursor()

        #hash password
        hashed_password = hash_password(password)

        #insertion
        cursor.execute("""
            INSERT INTO utilisateur(nom, email, password, role)
            VALUES(?,?,?,?)
        """, (nom, email, hashed_password, role))

        conn.commit()

    except sqlite3.Error as e:
        print("Erreur du creation de compte")
        if conn:

            #en cas d'erreur on annule l'operation
            conn.rollback()

    finally:      
        if conn:
            conn.close()