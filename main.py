# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

from rsa import generateRSAKeys, MyRSADecrypt, MyRSAEncrypt

# generateRSAKeys()

RSACipher, c, iv, ext = MyRSAEncrypt("files/TestImage.jpg", "files/rsa_public_key.pem")
MyRSADecrypt(RSACipher, c, iv, ext, "files/rsa_private_key.pem")
