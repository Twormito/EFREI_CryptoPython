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

@app.route('/encrypt/<string:valeur>')
def encryptage(valeur):
    valeur_bytes = valeur.encode()  # Conversion str -> bytes
    token = f.encrypt(valeur_bytes)  # Encrypt la valeur
    return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str

# 🔓 Nouvelle route de décryptage avec clé personnalisée
@app.route('/decrypt/', methods=['POST'])
def decrypt():
    try:
        data = request.get_json()
        encrypted = data['encrypted']
        key = data['key']

        f_custom = Fernet(key.encode())
        decrypted = f_custom.decrypt(encrypted.encode())
        return jsonify({'decrypted': decrypted.decode()})
    except InvalidToken:
        return jsonify({'error': 'Clé invalide ou texte corrompu'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
      
if __name__ == "__main__":
  app.run(debug=True)
