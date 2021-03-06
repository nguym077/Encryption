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

# (C, IV)= Myencrypt(message, key):
# In this method, you will generate a 16 Bytes IV, and encrypt
# the message using the key and IV in CBC mode (AES).
# You return an error if the len(key) < 32 (i.e., the key has
# to be 32 bytes = 256 bits).


def myencrypt(message, key):
    if len(key) != KEY_BYTES:
        # prints error message
        sys.stderr.write('Error: Encryption key length must be 32 bytes.')
    else:
        # generates random iv for specified length
        iv = os.urandom(IV_BYTES)

        # cipher objects combine an algorithm with a mode
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        # block ciphers require plaintext or ciphertext always be a
        # multiple of their block size (256)
        # paddings is required to make message the correct size
        padder = padding.PKCS7(BLOCK_SIZE).padder()

        # call 'update' with data until you have fed everything
        # call 'finalize' to finish operation
        c = padder.update(message) + padder.finalize()

        # returns an encrypting instance
        encrypter = cipher.encryptor()

        # encrypts padded message
        c = encrypter.update(c) + encrypter.finalize()

        print('... Finished myencrypt')
        return c, iv


# (C, IV, key, ext)= MyfileEncrypt (filepath):
# In this method, you'll generate a 32Byte key. You open and
# read the file as a string. You then call the above method to
# encrypt your file using the key you generated. You return the
# cipher C, IV, key and the extension of the file (as a string).


def myfileencrypt(filepath):    # 'filepath' should be 'files/name.extension'
    if os.path.isfile(filepath):
        # grabs extension to return
        filename, fileext = os.path.splitext(filepath)

        # generates key
        key = os.urandom(KEY_BYTES)

        # converts an image to a string
        fh = open(filepath, "rb")       # opens binary file in read mode
        imageBytes = base64.b64encode(fh.read())
        fh.close()

        c, iv = myencrypt(imageBytes, key)

        jsonFile = dict()
        jsonFile['c'] = base64.b64encode(c).decode('utf-8')
        jsonFile['iv'] = base64.b64encode(iv).decode('utf-8')
        jsonFile['key'] = base64.b64encode(key).decode('utf-8')
        jsonFile['fileext'] = base64.b64encode(fileext).decode('utf-8')

        fh = open("files/encrypted.json", "wb")
        json.dump(jsonFile, fh)
        fh.close()

        print('... Finished myfileencrypt')
        return c, iv, key, fileext
    else:
        sys.stderr.write('File does not exist.')
