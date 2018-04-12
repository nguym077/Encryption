# Marian Nguyen
# Steven Chung
# Lab 3 -- RSA File
# April 12, 2018

import os
import json
import sys
import base64

from decrypt import mydecrypt
from constants import KEY_BYTES
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from constants import KEY_BYTES, BLOCK_SIZE, IV_BYTES

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization



def MydecryptMAC(c, tag, iv, key, HMACKey):
    if len(HMACKey) != KEY_BYTES:
        sys.stderr.write('Error: Key length must be 32 bytes.')
    else:
        tagPrime = HMAC(HMACKey, hashes.SHA256(), backend=default_backend())
        tagPrime.update(c)

        tagPrime.verify(tag)

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

        decrypter = cipher.decryptor()

        message = decrypter.update(c) + decrypter.finalize()

        unpadder = padding.PKCS7(BLOCK_SIZE).unpadder()

        message = unpadder.update(message) + unpadder.finalize()

        print('... Finished mydecrypt')


    return message


def MyfileDecryptMAC(filepath):
    if os.path.isfile(filepath):

    return


def MyRSADecrypt(RSACipher, c, iv, tag, ext, RSA_privatekey_filepath):
    return

