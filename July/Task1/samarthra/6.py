def caesar_cipher(text, key):
    encrypted_text = ""

    for char in text:
        if char.isalpha():
            ascii_code = ord(char)
            
            if char.isupper():
               encrypted_code = (ascii_code - 65 + key) % 26 + 65
            else:
               encrypted_code = (ascii_code - 97 + key) % 26 + 97

               encrypted_char = chr(encrypted_code)
            encrypted_text += encrypted_char
        else:
            
            encrypted_text += char

    return encrypted_text


# Example usage
plaintext = input("enetr the word or sentence")
encryption_key = int(input("enter the count"))

# Encrypt the plaintext
encrypted_text = caesar_cipher(plaintext, encryption_key)
print("Encrypted :", encrypted_text)

# Decrypt the encrypted text
decrypted_text = caesar_cipher(encrypted_text, -encryption_key)
print("Decrypted :", decrypted_text)
