# Marian Nguyen
# Steven Chung
# Lab 3 -- RSA File
# April 12, 2018

import os
import json

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hmac import HMAC


def MyencryptMAC(message, EncKey, HMACKey):
    print("test")
    return C, IV, tag


def MyfileEncryptMAC(filepath):
    return c, iv, enckey, hmackey, ext


def MyRSAEncrypt(filepath, RSA_Publickey_filepath):
    return RSACipher, c, iv, tag, ext 