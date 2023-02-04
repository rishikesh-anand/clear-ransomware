# clear-ransomware

*We the clear team have made a Ransomware and a Ransomware Decrypter by using python libraries such as :-*
- `pycryptodome`
- `cryptography`
- `crypto`
- `base64`

*Ransomware.py code is a script that implements a ransomware attack. Here's what it does, step by step:

List all files in the current directory: The script uses the os.listdir() method to get a list of all files in the current working directory. It then filters the list to exclude itself and another script file, and appends the remaining files to a list named files.

Generate an encryption key: The code generates a symmetric encryption key using the Fernet.generate_key() method from the cryptography library.

Encrypt the key using RSA: The code imports a public key using the RSA.import_key() method from the Crypto library. It then uses the PKCS1_OAEP encryption method to encrypt the symmetric key generated in step 2.

Send the encrypted key to a specified URL: The code encodes the encrypted key in base64 format and appends it to a URL, then uses the requests.get() method to send a GET request to that URL.

Encrypt all listed files: The code reads the contents of each file in the files list and encrypts it using the symmetric key generated in step 2. The encrypted contents are then written back to the same file, effectively overwriting the original data.*


*This code is a sample ransomware script. It first looks for all the files in the current directory and stores it in a list files, excluding the files "ransomware.py" and "decrypt.py".

The private RSA key is stored in the variable private_key and is used to encrypt the files. The encryption is done using the PyCryptodome library, which is a self-contained Python package of low-level cryptographic primitives that supports both Python 3.6 and newer.

The code then uses the Fernet module of the cryptography library to decrypt the contents of the files*

**This Project for Hackthefall event is done by**:-

- `Yash Mehta`
- `Rishikesh Anand`
- `Utsav Kachhadiya `
- `Uttam Makwana`
