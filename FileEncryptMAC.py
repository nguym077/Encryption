# Marian Nguyen
# Steven Chung
# Lab 3 -- RSA File
# April 12, 2018

import os
import json
import sys
import base64

from encrypt import myencrypt, myfileencrypt
from constants import KEY_BYTES

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def MyencryptMAC(message, EncKey, HMACKey):
    c, iv = myencrypt(message, EncKey)

    if len(HMACKey) != KEY_BYTES:
        # prints error message
        sys.stderr.write('Error: HMAC key length must be 32 bytes.')
    else:
        # generates tag from HMAC
        tag = HMAC(HMACKey, hashes.SHA256(), backend=default_backend())
        tag.update(c)
        tag.finalize()

        return c, iv, tag


def MyfileEncryptMAC(filepath):
    if os.path.isfile(filepath):
        # grabs extension to return
        filename, ext = os.path.splitext(filepath)

        # generates keys
        enckey = os.urandom(KEY_BYTES)
        hmackey = os.urandom(KEY_BYTES)

        # converts an image to a string
        fh = open(filepath, "rb")  # opens binary file in read mode
        message = base64.b64encode(fh.read())
        fh.close()

        c, iv, tag = MyencryptMAC(message, enckey, hmackey)

        # writes to json file
        jsonFile = dict()
        jsonFile['c'] = base64.b64encode(c).decode('utf-8')
        jsonFile['iv'] = base64.b64encode(iv).decode('utf-8')
        jsonFile['tag'] = base64.b64encode(tag).decode('utf-8')
        jsonFile['enckey'] = base64.b64encode(enckey).decode('utf-8')
        jsonFile['hmackey'] = base64.b64encode(hmackey).decode('utf-8')
        jsonFile['ext'] = base64.b64encode(ext).decode('utf-8')

        fh = open("files/encrypted.json", "wb")
        json.dump(jsonFile, fh)
        fh.close()

        print('... Finished myfileencrypt (MAC)')
        return c, iv, tag, enckey, hmackey, ext
    else:
        sys.stderr.write('File does not exist')


def MyRSAEncrypt(filepath, RSA_Publickey_filepath):
    c, iv, tag, enckey, hmackey, ext = MyfileEncryptMAC(filepath)

    # loads public key
    fh = open(RSA_Publickey_filepath, "rb")
    public_key = serialization.load_pem_public_key(
        fh.read(),
        backend=default_backend()
    )
    fh.close()

    # encrypts "key" (enckey + hmackey)
    RSACipher = public_key.encrypt(
        enckey + hmackey,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    print("... Finished myrsaencrypt (with hmac)")

    return RSACipher, c, iv, tag, ext
