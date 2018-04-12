# Marian Nguyen
# Steven Chung
# Lab 3 -- RSA File
# April 12, 2018

import os

from rsa import generateRSAKeys
from FileEncryptMAC import MyRSAEncrypt
from FileDecryptMAC import MyRSADecrypt

private_filepath = 'rsa_private_key.pem'
public_filepath = 'rsa_public_key.pem'

# checks to see if public/private key exists
public_exists = os.path.isfile(public_filepath)
private_exists = os.path.isfile(private_filepath)

# if they don't exists, create them
if public_exists == False and private_exists == False:
    generateRSAKeys()

cwd = os.getcwd()
test_directory = cwd + '/files/'

files_in_directory = os.listdir(test_directory)
for f in files_in_directory:
    print(test_directory + f)
    RSACipher, c, iv, tag, ext = MyRSAEncrypt(test_directory + f, "rsa_public_key.pem")


#RSACipher, c, iv, tag, ext = MyRSAEncrypt("files/TestImage.jpg", "rsa_public_key.pem")
#MyRSADecrypt(RSACipher, c, iv, tag, ext, "rsa_private_key.pem")
