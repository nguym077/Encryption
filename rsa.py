# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

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

# openssl(rsa keygen)


def MyRSAEncrypt(filepath, RSA_Publickey_filepath):
    c, iv, key, ext = myfileencrypt("./" + filepath)


fh = open(RSA_Publickey_filepath, "rb")
publicKey = serialization.load_pem_public_key(
    fh.read(),
    backend=default_backend()
)

RSACipher = publicKey.encrypt(
    key,
    asymmetric.padding.OAEP(
        x=asymmetric.padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None

    )
)

return RSACipher, c, iv, ext

