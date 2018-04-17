# Marian Nguyen
# Steven Chung
# Lab 3 -- RSA File
# April 12, 2018

import os

from rsa import generateRSAKeys
from FileEncryptMAC import MyRSAEncrypt
from FileDecryptMAC import MyRSADecrypt

generateRSAKeys()

RSACipher, c, iv, tag, ext = MyRSAEncrypt("files/TestImage.jpg", "rsa_public_key.pem")
MyRSADecrypt(RSACipher, c, iv, tag, ext, "rsa_private_key.pem")
