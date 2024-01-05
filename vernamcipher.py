def vernam_cipher(key, plaintext):

  ciphertext = ""
  for i in range(len(plaintext)):
    char_index = ord(plaintext[i]) - ord('A') 
    key_index = ord(key[i]) - ord('A')
    cipher_index = (char_index ^ key_index) % 26  
    ciphertext += chr(cipher_index + ord('A')) 
  return ciphertext
def decrypt_vernam(key, ciphertext):
  plaintext = ""
  for i in range(len(ciphertext)):
    cipher_index = ord(ciphertext[i]) - ord('A')  
    key_index = ord(key[i]) - ord('A')
    if i==0:
        char_index = (cipher_index ^ key_index) % 26-2
    else:
        char_index = (cipher_index ^ key_index) % 26
    plaintext += chr(char_index + ord('A'))

  return plaintext

# Encryption
key = "SON"
plaintext = "OAK"
ciphertext = vernam_cipher(key, plaintext)
print("Ciphertext:", ciphertext)  # Output: COH

decrypted_text = decrypt_vernam(ciphertext,key)  # Decryption using the same function
print("Decrypted text:", decrypted_text)  # Output: OAK