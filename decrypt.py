# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

<<<<<<< HEAD
# You'll have to write the inverse of the methods in Encrypt.py **
#print("Hello World")

=======
import sys
import os
import base64
from constants import KEY_BYTES, BLOCK_SIZE, IV_BYTES
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Write the inverse of the methods in Encrypt.py **
>>>>>>> d3a5fb149d701d213cef8d2c0abceb710c64237d


def mydecrypt(c, iv, key):
    if len(key) != KEY_BYTES:
        # prints error message
        sys.stderr.write('Error: Key length must be 32 bytes.')
    else:
        print('... Begin mydecrypt with CBC mode (AES)')

        # cipher objects combine an algorithm with a mode
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        # returns an decrypting instance
        decrypter = cipher.decryptor()

        # decrypts ciphertext
        message = decrypter.update(c) + decrypter.finalize()

        # upadding instance
        unpadder = padding.PKCS7(BLOCK_SIZE).unpadder()

        # unpads decrypted message
        message = unpadder.update(message) + unpadder.finalize()

        print('... Finished mydecrypt')
        return message


def myfiledecrypt(filepath, c, iv, key):    # 'filepath' should be 'files/name.extension'
    if os.path.isfile(filepath):
        print('... Begin myfiledecrypt')

        m = mydecrypt(c, iv, key)

        fh = open("files/decryptedImage.jpg", "wb")
        fh.write(base64.b64decode(m))
        fh.close()

        print('... Finish myfiledecrypt')
    else:
        sys.stderr.write('File does not exist.')
