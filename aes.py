from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import (Cipher, algorithms, modes)

def encrypt(p_text, iv, key):
    backend = default_backend()

    cipher = Cipher(algorithms.AES(key),modes.CFB(iv),backend=backend)
    padder = padding.PKCS7(128).padder() # 128 bit
    text = padder.update(p_text) + padder.finalize()
    encryptor = cipher.encryptor()
    c_text = encryptor.update(text) + encryptor.finalize()
    return c_text


def decrypt(p_text, iv, key):
    backend = default_backend()

    cipher = Cipher(algorithms.AES(key),modes.CFB(iv),backend=backend)
    padder = padding.PKCS7(128).padder() # 128 bit
    text = padder.update(p_text) + padder.finalize()
    decryptor = cipher.decryptor()
    c_text = decryptor.update(text) + decryptor.finalize()
    return c_text


if __name__ == "__main__":
    plaintext = "Testing AES encryption/decryption in techieshouts.com"
    iv = "TestMeInitVector"
    key = "YourSampleEncKey"
    print("Plain text: ",plaintext)
    print("Calling encryption library")
    encryptedtext = encrypt(plaintext,iv,key)
    print("Encrypted text")
    print(encryptedtext)
    decryptedtext = decrypt(encryptedtext,iv,key)
    print("Decrypted text")