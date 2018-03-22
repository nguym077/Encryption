# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

from rsa import generateRSAKeys, MyRSADecrypt, MyRSAEncrypt
from encrypt import myfileencrypt
from decrypt import myfiledecrypt

# generateRSAKeys()

myfileencrypt("files/TestImage.jpg")
myfiledecrypt("files/encrypted.json")
