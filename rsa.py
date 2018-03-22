# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

import base64
import json

from encrypt import myfileencrypt
from decrypt import myfiledecrypt
from constants import FERMAT_PRIME, KEY_SIZE

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def generateRSAKeys():
    # generates new RSA private key
    # value used for public_exponent is default
    private_key = rsa.generate_private_key(
        public_exponent=FERMAT_PRIME,
        key_size=KEY_SIZE,
        backend=default_backend()
    )

    # generates public key from private key
    public_key = private_key.public_key()

    # serializes (private) key
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    # serializes (public) key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # writes keys to file
    fh = open("files/rsa_private_key.pem", "wb")
    fh.write(private_pem)
    fh.close()

    fh = open("files/rsa_public_key.pem", "wb")
    fh.write(public_pem)
    fh.close()


def MyRSAEncrypt(filepath, RSA_Publickey_filepath):
    c, iv, key, ext = myfileencrypt(filepath)

    # loads public key
    fh = open(RSA_Publickey_filepath, "rb")
    public_key = serialization.load_pem_public_key(
        fh.read(),
        backend=default_backend()
    )
    fh.close()

    # encrypts "key"
    RSACipher = public_key.encrypt(
        key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return RSACipher, c, iv, ext

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


def MyRSADecrypt(RSACipher, c, iv, ext, RSA_privatekey_filepath):
    fh = open(RSA_privatekey_filepath, "rb")

    # loads private key
    private_key = serialization.load_pem_private_key(
        fh.read(),
        password=None,
        backend=default_backend()
    )
    fh.close()

    # decrypts "RSACipher"
    key = private_key.decrypt(
        RSACipher,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # saves data into json file
    jsonFile = dict()
    jsonFile['c'] = base64.b64encode(c).decode('utf-8')
    jsonFile['iv'] = base64.b64encode(iv).decode('utf-8')
    jsonFile['key'] = base64.b64encode(key).decode('utf-8')
    jsonFile['ext'] = base64.b64encode(ext).decode('utf-8')

    fh = open("files/encryptedRSA.json", "wb")
    json.dump(jsonFile, fh)
    fh.close()

    # decrypts json file to return original image
    myfiledecrypt("files/encryptedRSA.json")