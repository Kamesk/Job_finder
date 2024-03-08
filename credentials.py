from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_credentials(key, username, password):
    cipher_suite = Fernet(key)
    encrypted_username = cipher_suite.encrypt(username.encode())
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_username, encrypted_password

def decrypt_credentials(key, encrypted_username, encrypted_password):
    cipher_suite = Fernet(key)
    username = cipher_suite.decrypt(encrypted_username).decode()
    password = cipher_suite.decrypt(encrypted_password).decode()
    return username, password

# Example usage:
if __name__ == "__main__":
    key = generate_key()
    username = "xxxxxxxxxxx"
    password = "xxxxxxxxxxx"

    encrypted_username, encrypted_password = encrypt_credentials(key, username, password)
    print("Encrypted username:", encrypted_username)
    print("Encrypted password:", encrypted_password)

    decrypted_username, decrypted_password = decrypt_credentials(key, encrypted_username, encrypted_password)
    print("Decrypted username:", decrypted_username)
    print("Decrypted password:", decrypted_password)
    print(key)
