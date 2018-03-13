# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

import sys
import os
import base64
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding




REQUIRED_KEY_BYTE_LENGTH = 32
REQUIRED_IV_BYTE_LENGTH = 16
BLOCK_SIZE = 256

# (C, IV)= Myencrypt(message, key):
# In this method, you will generate a 16 Bytes IV, and encrypt
# the message using the key and IV in CBC mode (AES).
# You return an error if the len(key) < 32 (i.e., the key has
# to be 32 bytes = 256 bits).


def myencrypt(message, key):
    if len(key) != REQUIRED_KEY_BYTE_LENGTH:
        # prints error message
        sys.stderr.write('Error: Key length must be 32 bytes.')
    else:
        print('... Begin myencrypt with CBC mode (AES)')

        # generates random iv for specified length
        iv = os.urandom(REQUIRED_IV_BYTE_LENGTH)

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
        print('... Begin myfileencrypt')

        # grabs extension to return
        filename, fileext = os.path.splitext(filepath)
        key = os.urandom(REQUIRED_KEY_BYTE_LENGTH)

        # converts an image to a string
        fh = open(filepath, "rb")       # opens binary file in read mode
        imageBytes = base64.b64encode(fh.read())
        fh.close()

        c, iv = myencrypt(imageBytes, key)

        # fh = open("files/output.JPEG", "wb")
        # fh.write(base64.b64decode(c))
        # fh.close()

        print('... Finished myfileencrypt')
        return c, iv, key, fileext
    else:
        sys.stderr.write('File does not exist.')


myfileencrypt('files/TestImage.JPEG')