from cryptography.fernet import Fernet
 from flask import Flask, render_template_string, render_template, jsonify
 from flask import render_template
 from flask import json
 from urllib.request import urlopen
 import sqlite3
                                                                                                                                        
 app = Flask(__name__)                                                                                                                  
                                                                                                                                        
 from flask import Flask, render_template
 
 app = Flask(name)
 
 @app.route('/')
 def hello_world():
     return render_template('hello.html') #Comm2
     return render_template('hello.html')  # Comm2
 
 @app.route('/encrypt/<string:cle>/<string:valeur>')
 def encryptage(cle, valeur):
     try:
         f = Fernet(cle.encode())
         valeur_bytes = valeur.encode()
         token = f.encrypt(valeur_bytes)
         return f"Valeur encryptée : {token.decode()}"
     except Exception as e:
         return f"Erreur d'encryption : {str(e)}"
 
 key = Fernet.generate_key()
 f = Fernet(key)
 @app.route('/decrypt/<string:cle>/<string:valeur>')
 def decryptage(cle, valeur):
     try:
         f = Fernet(cle.encode())
         valeur_bytes = valeur.encode()
         decrypted = f.decrypt(valeur_bytes)
         return f"Valeur décryptée : {decrypted.decode()}"
     except Exception as e:
         return f"Erreur de décryption : {str(e)}"
 
 @app.route('/encrypt/<string:valeur>')
 def encryptage(valeur):
     valeur_bytes = valeur.encode()  # Conversion str -> bytes
     token = f.encrypt(valeur_bytes)  # Encrypt la valeur
     return f"Valeur encryptée : {token.decode()}"  # Retourne le token en str
 @app.route('/generate-key')
 def generate_key():
     return f"Voici votre clé personnelle : {Fernet.generate_key().decode()}"
 
 @app.route('/decrypt/<string:token>')
 def decryptage(token):
     token_bytes = token.encode()  # Conversion str -> bytes
     valeur = f.decrypt(token_bytes)  # Décryptage
     return f"Valeur décryptée : {valeur.decode()}"  # Retourne la valeur en str
   
 if __name__ == "__main__":
   app.run(debug=True)
 if name == "main":
     app.run(debug=True)
