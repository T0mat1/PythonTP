# -*- coding: utf-8 -*-
# TP3 Python - Thomas ROSSI & Emeric PAIN
import os
from Crypto.Cipher import AES
import hashlib

if __name__ == "__main__":
    password = "password"
    print("Choisissez un fichier à chiffrer: ")
    file_to_encrypt = input()
    print()  # print an empty line as a separation
    key = hashlib.sha256(password.encode()).digest()
    iv = os.urandom(16)
    buffer_size = 65536  # 64kb

    # === Encrypt ===

    # Open the input and output files
    input_file = open(file_to_encrypt, 'rb')
    output_file = open(file_to_encrypt + '.encrypted', 'wb')

    # Create the cipher object and encrypt the data
    cipher_encrypt = AES.new(key, AES.MODE_CFB, iv)

    # Initially write the iv to the output file
    output_file.write(iv)

    # Keep reading the file into the buffer, encrypting then writing to the new file
    buffer = input_file.read(buffer_size)
    while len(buffer) > 0:
        ciphered_bytes = cipher_encrypt.encrypt(buffer)
        output_file.write(ciphered_bytes)
        buffer = input_file.read(buffer_size)

    # Close the input and output files
    input_file.close()
    output_file.close()

    # === Decrypt ===

    # Open the input and output files
    input_file = open(file_to_encrypt + '.encrypted', 'rb')
    output_file = open(file_to_encrypt + '.decrypted', 'wb')

    # Read in the iv
    iv = input_file.read(16)

    # Create the cipher object and encrypt the data
    cipher_encrypt = AES.new(key, AES.MODE_CFB, iv)

    # Keep reading the file into the buffer, decrypting then writing to the new file
    buffer = input_file.read(buffer_size)
    while len(buffer) > 0:
        decrypted_bytes = cipher_encrypt.decrypt(buffer)
        output_file.write(decrypted_bytes)
        buffer = input_file.read(buffer_size)

    # Close the input and output files
    input_file.close()
    output_file.close()
