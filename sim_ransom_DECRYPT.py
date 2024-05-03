import time
import random

import sys
sys.path.append('C:\\Users\\Admin\\AppData\\Roaming\\Python\\Python311\\site-packages')
import rsa

# == read and load the private-key
private_key_file_path = 'D:\\private_key.pem'
# Read the private key from the PEM file
with open(private_key_file_path, 'rb') as file: # read as binary
    private_key_data = file.read()

# Decode the private key from PEM format
private_key = rsa.PrivateKey.load_pkcs1(private_key_data)
print(private_key)

# == decrypt files
file_paths = [
    'D:\\input1.txt',
    'D:\\input2.txt',
    'D:\\input3.txt',
    'D:\\input4.txt',
    'D:\\input5.txt',
    'D:\\input6.txt',
    'D:\\input7.txt',
    'D:\\input8.txt',
    'D:\\input9.txt',
    'D:\\input10.txt'
    # Add more file paths as needed
]


for file_path in file_paths:
  # random sleep for detecting

  with open(file_path, 'rb') as file: # read as binary
    file_contents = file.read()
    
    plaintext = rsa.decrypt(file_contents, private_key)
    print(plaintext)


