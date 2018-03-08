# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018


# (C, IV)= Myencrypt(message, key):
# In this method, you will generate a 16 Bytes IV, and encrypt
# the message using the key and IV in CBC mode (AES).
# You return an error if the len(key) < 32 (i.e., the key has
# to be 32 bytes= 256 bits).


def myencrypt(message, key):
    print("test 1")

# (C, IV, key, ext)= MyfileEncrypt (filepath):
# In this method, you'll generate a 32Byte key. You open and
# read the file as a string. You then call the above method to
# encrypt your file using the key you generated. You return the
# cipher C, IV, key and the extension of the file (as a string).


def myfileencrypt(filepath):
    print("test 2")


# You'll have to write the inverse of the above methods. **

# (RSACipher, C, IV, ext)= MyRSAEncrypt(filepath, RSA_Publickey_filepath):
# In this method, you first call MyfileEncrypt (filepath) which will
# return (C, IV, key, ext). You then will initialize an RSA public
# key encryption object and load pem publickey from the RSA_publickey
# filepath. Lastly, you encrypt the key variable ("key") using the RSA
# publickey in OAEP padding mode. The result will be RSACipher. You then
# return (RSACipher, C, IV, ext). Remember to do the inverse
# (MyRSADecrypt (RSACipher, C, IV, ext, RSA_Privatekey_filepath)) which
# does the exactly inverse of the above and generate the decrypted
# file using your previous decryption methods.


def myrsaencrypt(filepath, RSA_Publickey_filepath):
    print("test 3")

