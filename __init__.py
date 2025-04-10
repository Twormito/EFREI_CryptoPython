from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print(f"Votre clé personnelle : {key.decode()}")
    return key

def encrypt_message(key, message):
    try:
        f = Fernet(key.encode())
        token = f.encrypt(message.encode())
        print(f"Message chiffré : {token.decode()}")
    except Exception as e:
        print(f"Erreur de chiffrement : {e}")

def decrypt_message(key, token):
    try:
        f = Fernet(key.encode())
        message = f.decrypt(token.encode())
        print(f"Message déchiffré : {message.decode()}")
    except Exception as e:
        print(f"Erreur de déchiffrement : {e}")

def main():
    print("=== Chiffrement / Déchiffrement avec clé personnelle ===\n")
    print("1. Générer une nouvelle clé")
    print("2. Utiliser une clé existante")
    choix = input("Votre choix (1/2) : ")

    if choix == "1":
        key = generate_key().decode()
    else:
        key = input("Entrez votre clé personnelle : ")

    print("\nQue voulez-vous faire ?")
    print("1. Chiffrer un message")
    print("2. Déchiffrer un message")
    action = input("Votre choix (1/2) : ")

    if action == "1":
        message = input("Entrez le message à chiffrer : ")
        encrypt_message(key, message)
    elif action == "2":
        token = input("Entrez le message chiffré (token) : ")
        decrypt_message(key, token)
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()
