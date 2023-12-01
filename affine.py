def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(plaintext, a, b):
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                x = ord(char) - ord('A')
                encrypted_char = chr((a * x + b) % 26 + ord('A'))
            elif char.islower():
                x = ord(char) - ord('a')
                encrypted_char = chr((a * x + b) % 26 + ord('a'))
        else:
            encrypted_char = char
        
        ciphertext += encrypted_char

    return ciphertext

def decrypt(ciphertext, a, b):
    m = 26  

    a_inverse = mod_inverse(a, m)
    if a_inverse is None:
        raise ValueError("a and m must be coprime for decryption to be possible.")

    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                y = ord(char) - ord('A')
                decrypted_char = chr((a_inverse * (y - b)) % 26 + ord('A'))
            elif char.islower():
                y = ord(char) - ord('a')
                decrypted_char = chr((a_inverse * (y - b)) % 26 + ord('a'))
        else:
            decrypted_char = char
        
        plaintext += decrypted_char

    return plaintext

def main():
    a = int(input("Enter the value of 'a': "))
    b = int(input("Enter the value of 'b': "))
    plaintext = input("Enter the plaintext: ")

    ciphertext = encrypt(plaintext, a, b)
    decrypted_text = decrypt(ciphertext, a, b)

    print("\nPlaintext:", plaintext)
    print("Key (a, b):", (a, b))
    print("Encrypted:", ciphertext)
    print("Decrypted:", decrypted_text)

if __name__ == '__main__':
    main()
