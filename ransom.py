# Marian Nguyen
# Steven Chung
# Lab 3 -- RSA File
# April 12, 2018

import os

from rsa import generateRSAKeys
from FileEncryptMAC import MyRSAEncrypt

private_filepath = 'rsa_private_key.pem'
public_filepath = 'rsa_public_key.pem'

# checks to see if public/private key exists
public_exists = os.path.isfile(public_filepath)
private_exists = os.path.isfile(private_filepath)

# if they don't exists, create them
if public_exists == False and private_exists == False:
    generateRSAKeys()

cwd = os.getcwd()
files_in_directory = os.listdir(cwd)
for f in files_in_directory:
    print(f)
    RSACipher, c, iv, tag, ext = MyRSAEncrypt(f, "rsa_public_key.pem")
