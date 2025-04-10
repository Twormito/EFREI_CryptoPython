from cryptography.fernet import Fernet
from flask import Flask, render_template

app = Flask(__name__)  # ✅ Corrigé : __name__ au lieu de name

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Page HTML simple (hello.html)

@app.route('/encrypt/<string:cle>/<string:valeur>')
def encryptage(cle, valeur):
    try:
        f = Fernet(cle.encode())
        valeur_bytes = valeur.encode()
        token = f.encrypt(valeur_bytes)
        return f"Valeur encryptée : {token.decode()}"
    except Exception as e:
        return f"Erreur d'encryption : {str(e)}"

@app.route('/decrypt/<string:cle>/<string:valeur>')
def decryptage(cle, valeur):
    try:
        f = Fernet(cle.encode())
        valeur_bytes = valeur.encode()
        decrypted = f.decrypt(valeur_bytes)
        return f"Valeur décryptée : {decrypted.decode()}"
    except Exception as e:
        return f"Erreur de décryption : {str(e)}"

@app.route('/generate-key')
def generate_key():
    return f"Voici votre clé personnelle : {Fernet.generate_key().decode()}"

if __name__ == "__main__":  # ✅ Corrigé : __name__ == "__main__"
    app.run(debug=True)
