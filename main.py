# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

from constants import KEY_SIZE, FERMAT_PRIME
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

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
