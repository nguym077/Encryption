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



def MydecryptMAC(c, tag, iv, enckey, HMACKey):
    if len(HMACKey) != KEY_BYTES:
        sys.stderr.write('Error: Key length must be 32 bytes.')
    else:
        # generates new tag
        tagPrime = HMAC(HMACKey, hashes.SHA256(), backend=default_backend())
        tagPrime.update(c)

        # verifies tags match
        # errors if false
        tagPrime.verify(tag)

        # decrypts message after tag verification
        message = mydecrypt(c, iv, enckey)

        print('... Finished mydecrypt (mac')
        return message


def MyfileDecryptMAC(filepath):
    if os.path.isfile(filepath):
        jr = open(filepath, "rb")
        jsonData = json.load(jr)
        jr.close()

        c = base64.b64decode(jsonData["c"])
        iv = base64.b64decode(jsonData["iv"])
        tag = base64.b64decode(jsonData["tag"])
        enckey = base64.b64decode(jsonData["enckey"])
        hmackey = base64.b64decode(jsonData["hmackey"])

        m = MydecryptMAC(c, tag, iv, enckey, hmackey)

        fh = open("files/decryptedImage.jpg", "wb")
        fh.write(base64.b64decode(m))
        fh.close()

        print('... Finished myfiledecrypt (mac)')


def MyRSADecrypt(RSACipher, c, iv, tag, ext, RSA_privatekey_filepath):
    fh = open(RSA_privatekey_filepath, "rb")

    # loads private key
    private_key = serialization.load_pem_private_key(
        fh.read(),
        password=None,
        backend=default_backend()
    )
    fh.close()

    # decrypts "RSACipher"
    key = private_key.decrypt(
        RSACipher,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # saves data into json file
    jsonFile = dict()
    jsonFile['c'] = base64.b64encode(c).decode('utf-8')
    jsonFile['iv'] = base64.b64encode(iv).decode('utf-8')
    jsonFile['tag'] = base64.b64encode(tag).decode('utf-8')
    jsonFile['key'] = base64.b64encode(key).decode('utf-8')
    jsonFile['ext'] = base64.b64encode(ext).decode('utf-8')

    fh = open("files/encryptedRSA.json", "wb")
    json.dump(jsonFile, fh)
    fh.close()

    # decrypts json file to return original image
    MyfileDecryptMAC("files/encryptedRSA.json")
    print('... Finished myrsadecrypt (mac)')

