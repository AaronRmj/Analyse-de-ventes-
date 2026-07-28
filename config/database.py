# Liaison entre py et BD

# en py, quand un fichier est executé, le point de repere est la racine du projet
DATABASE = "database/ventes.db"
import sqlite3

def get_connexion():
    return sqlite3.connect(DATABASE)