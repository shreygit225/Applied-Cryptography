import random

def generate_super_increasing_sequence(n):
    sequence = [random.randint(1, 100)]
    while len(sequence) < n:
        next_element = sum(sequence) + random.randint(1, 10)
        sequence.append(next_element)
    return sequence

def generate_private_key(public_key, q, r):
    private_key = [(r * element) % q for element in public_key]
    return private_key

def knapsack_encrypt(plaintext, public_key):
    encrypted_message = sum(public_key[i] for i in range(len(plaintext)) if plaintext[i] == '1')
    return encrypted_message

def knapsack_decrypt(ciphertext, private_key, q, r):
    r_inverse = pow(r, -1, q) 
    decrypted_message = ''
    for element in reversed(private_key):
        if (ciphertext * r_inverse) % q >= element:
            decrypted_message = '1' + decrypted_message
            ciphertext -= element
        else:
            decrypted_message = '0' + decrypted_message
    return decrypted_message

if __name__ == "__main__":
    n = 8 
    q = 103 
    r = 3

    public_key = generate_super_increasing_sequence(n)
    private_key = generate_private_key(public_key, q, r)

    plaintext = input("Enter the text to encrypt: ")
    ciphertext = knapsack_encrypt(plaintext, public_key)
    decrypted_message = knapsack_decrypt(ciphertext, private_key, q, r)

    print("Original Message:", plaintext)
    print("Encrypted Ciphertext:", ciphertext)
    print("Decrypted Message:", decrypted_message)
import random

def generate_super_increasing_sequence(n):
    sequence = [random.randint(1, 100)]
    while len(sequence) < n:
        next_element = sum(sequence) + random.randint(1, 10)
        sequence.append(next_element)
    return sequence

def generate_private_key(public_key, q, r):
    private_key = [(r * element) % q for element in public_key]
    return private_key

def knapsack_encrypt(plaintext, public_key):
    encrypted_message = sum(public_key[i] for i in range(len(plaintext)) if plaintext[i] == '1')
    return encrypted_message

def knapsack_decrypt(ciphertext, private_key, q, r):
    r_inverse = pow(r, -1, q) 
    decrypted_message = ''
    for element in reversed(private_key):
        if (ciphertext * r_inverse) % q >= element:
            decrypted_message = '1' + decrypted_message
            ciphertext -= element
        else:
            decrypted_message = '0' + decrypted_message
    return decrypted_message

if __name__ == "__main__":
    n = 8 
    q = 103 
    r = 3

    public_key = generate_super_increasing_sequence(n)
    private_key = generate_private_key(public_key, q, r)

    plaintext = input("Enter the text to encrypt: ")
    ciphertext = knapsack_encrypt(plaintext, public_key)
    decrypted_message = knapsack_decrypt(ciphertext, private_key, q, r)

    print("Original Message:", plaintext)
    print("Encrypted Ciphertext:", ciphertext)
    print("Decrypted Message:", decrypted_message)
