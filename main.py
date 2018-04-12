# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

from rsa import generateRSAKeys
from FileEncryptMAC import MyRSAEncrypt
from FileDecryptMAC import MyRSADecrypt

generateRSAKeys()

RSACipher, c, iv, tag, ext = MyRSAEncrypt("files/TestImage.jpg", "rsa_public_key.pem")
MyRSADecrypt(RSACipher, c, iv, tag, ext, "rsa_private_key.pem")
