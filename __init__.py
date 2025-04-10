from cryptography.fernet import Fernet
from flask import Flask, render_template_string, render_template, jsonify
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  
                                                                                                                                       
@app.route('/')
def hello_world():
    return render_template('hello.html') #Comm2

key = Fernet.generate_key()
f = Fernet(key)

@app.route('/encrypt/<key>/<string:valeur>')
def encryptage_cle_perso(key, valeur):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        token = f.encrypt(valeur.encode())  # Chiffre la valeur
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"

@app.route('/decrypt/<key>/<token>')
def decryptage_cle_perso(key, token):
    try:
        f = Fernet(key.encode())  # Crée un objet Fernet avec la clé fournie
        valeur = f.decrypt(token.encode())  # Déchiffre le token
        return f"Valeur décryptée : {valeur.decode()}"
    except Exception as e:
        return f"Erreur : {str(e)}"
  
if __name__ == "__main__":
  app.run(debug=True)
