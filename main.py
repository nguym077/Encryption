# Marian Nguyen
# Steven Chung
# Lab 2 -- File Encryption
# March 15, 2018

import os
from constants import KEY_BYTES, BLOCK_SIZE, IV_BYTES
from encrypt import myencrypt
from decrypt import mydecrypt


key = os.urandom(KEY_BYTES)
ciphertext, iv = myencrypt('hello marian', key)
message = mydecrypt(ciphertext, iv, key)
print(message)
