# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

import sys
import os
import base64
import json
from constants import KEY_BYTES, BLOCK_SIZE, IV_BYTES
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def mydecrypt(c, iv, key):
    if len(key) != KEY_BYTES:
        # prints error message
        sys.stderr.write('Error: Key length must be 32 bytes.')
    else:
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


def myfiledecrypt(filepath):    # 'filepath' should be 'files/name.extension'
    if os.path.isfile(filepath):
        jr = open(filepath, "rb")
        jsonData = json.load(jr)
        jr.close()

        c = base64.b64decode(jsonData["c"])
        key = base64.b64decode(jsonData["key"])
        iv = base64.b64decode(jsonData["iv"])

        m = mydecrypt(c, iv, key)

        fh = open("files/decryptedImage.jpg", "wb")
        fh.write(base64.b64decode(m))
        fh.close()

        print('... Finish myfiledecrypt')
    else:
        sys.stderr.write('File does not exist.')
