def playfair_cipher(key, plaintext):
    key = key.replace(" ", "").upper()
    key_square = ""
    for letter in key:
        if letter not in key_square and letter != "J":
            key_square += letter
    for letter in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if letter not in key_square:
            key_square += letter

    plaintext = plaintext.replace(" ", "").upper()
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        if i == len(plaintext) - 1:
            plaintext += "Z"
        elif plaintext[i] == plaintext[i + 1]:
            plaintext = plaintext[:i + 1] + "X" + plaintext[i + 1:]

        row1, col1 = divmod(key_square.index(plaintext[i]), 5)
        row2, col2 = divmod(key_square.index(plaintext[i + 1]), 5)

        if row1 == row2:
            ciphertext += key_square[row1 * 5 + (col1 + 1) % 5]
            ciphertext += key_square[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[((row1 + 1) % 5) * 5 + col1]
            ciphertext += key_square[((row2 + 1) % 5) * 5 + col2]
        else:
            ciphertext += key_square[row1 * 5 + col2]
            ciphertext += key_square[row2 * 5 + col1]

    return ciphertext

def playfair_decipher(key, ciphertext):
    key = key.replace(" ", "").upper()
    key_square = ""
    for letter in key:
        if letter not in key_square and letter != "J":
            key_square += letter
    for letter in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if letter not in key_square:
            key_square += letter

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        row1, col1 = divmod(key_square.index(ciphertext[i]), 5)
        row2, col2 = divmod(key_square.index(ciphertext[i + 1]), 5)

        if row1 == row2:
            plaintext += key_square[row1 * 5 + (col1 - 1) % 5]
            plaintext += key_square[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_square[((row1 - 1) % 5) * 5 + col1]
            plaintext += key_square[((row2 - 1) % 5) * 5 + col2]
        else:
            plaintext += key_square[row1 * 5 + col2]
            plaintext += key_square[row2 * 5 + col1]

    if plaintext[-1] == "Z":
        plaintext = plaintext[:-1]

    return plaintext

key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")
ciphertext = playfair_cipher(key, plaintext)
print("Ciphertext:", ciphertext)
decrypted_text = playfair_decipher(key, ciphertext)
print("Decrypted text:", decrypted_text)
