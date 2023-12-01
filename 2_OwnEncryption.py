import random

r = random.randint(1,10)
def generate_key():
    key = {}
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .,!?"
    shuffled_characters = list(characters)
    random.shuffle(shuffled_characters)
    
    for char, shuffled_char in zip(characters, shuffled_characters):
        key[char] = shuffled_char
    
    return key

def encrypt(plaintext, key):
    encrypted_text = ""

    for char in plaintext:
        if char in key:
            encrypted_text += key[char]
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, key):
    reversed_key = {v: k for k, v in key.items()}
    decrypted_text = ""

    for char in encrypted_text:
        if char in reversed_key:
            decrypted_text += reversed_key[char]
        else:
            decrypted_text += char

    return decrypted_text

# User Input
plaintext = input("Enter the plaintext: ")
key = generate_key()

encrypted_text = encrypt(plaintext, key)
decrypted_text = decrypt(encrypted_text, key)

print("\nPlaintext:", plaintext)
print("Key:", key)
print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)
