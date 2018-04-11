# Marian Nguyen
# Steven Chung
# Lab 3 -- RSA File
# April 12, 2018

import os
import json
import sys

from encrypt import myencrypt
from constants import KEY_BYTES

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC


def MyencryptMAC(message, EncKey, HMACKey):
    c, iv = myencrypt(message, EncKey)

    if len(HMACKey) != KEY_BYTES:
        # prints error message
        sys.stderr.write('Error: HMAC key length must be 32 bytes.')
    else:
        tag = HMAC(HMACKey, hashes.SHA256(), backend=default_backend())
        tag.update(c)
        tag.finalize()

        return c, iv, tag


def MyfileEncryptMAC(filepath):
    return c, iv, enckey, hmackey, ext


def MyRSAEncrypt(filepath, RSA_Publickey_filepath):
    return RSACipher, c, iv, tag, ext