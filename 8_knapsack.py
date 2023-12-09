# Helper functions
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def is_superincreasing_sequence(seq):
    for i in range(1, len(seq)):
        if seq[i] <= sum(seq[:i]):
            return False
    return True

# Encryption functions
def generate_superincreasing_sequence(private_key, n, m):
    return [(si * n) % m for si in private_key]

def generate_public_key(private_key, n, m):
    return generate_superincreasing_sequence(private_key, n, m)

def encrypt(binary_input, public_key):
    if len(binary_input) % len(public_key) != 0:
        raise ValueError("Length of binary input must be a multiple of the length of the public key")

    chunk_size = len(public_key)
    ciphertext = []

    for i in range(0, len(binary_input), chunk_size):
        chunk = binary_input[i:i + chunk_size]
        encrypted_value = sum(int(bit) * public_key[j] for j, bit in enumerate(chunk))
        ciphertext.append(encrypted_value)

        # Show intermediate calculations in output
        print(f"Encrypting chunk {chunk} using public key {public_key}: {chunk} * {public_key} = {encrypted_value}")

    return ciphertext

def main():
    # Take user input for private key
    private_key = [int(bit) for bit in input("Enter the private key as a space-separated superincreasing sequence (e.g., 2 3 7 14): ").split()]

    # Validate superincreasing sequence
    while not is_superincreasing_sequence(private_key):
        print("Error: The input is not a superincreasing sequence. Please enter a valid superincreasing sequence.")
        private_key = [int(bit) for bit in input("Enter the private key as a space-separated superincreasing sequence (e.g., 2 3 7 14): ").split()]

    # Take user input for m (greater than the combined value of the private key)
    combined_value = sum(private_key)
    m = int(input(f"Enter the value of m (greater than {combined_value}): "))
    while m <= combined_value:
        print("Error: m must be greater than the combined value of the private key.")
        m = int(input(f"Enter the value of m (greater than {combined_value}): "))

    # Take user input for n (gcd(n, m) should be 1)
    n = int(input("Enter the value of n (gcd(n, m) should be 1): "))
    while gcd(n, m) != 1:
        print("Error: gcd(n, m) must be 1.")
        n = int(input("Enter the value of n (gcd(n, m) should be 1): "))

    # Generate public key
    public_key = generate_public_key(private_key, n, m)
    print("Public Key:", public_key)

    # Take user input for binary message
    binary_input = input("Enter the binary message to encrypt (e.g., 11010101): ")

    # Encrypt the message
    ciphertext = encrypt(binary_input, public_key)
    print("Encrypted Ciphertext:", ciphertext)

if __name__ == "__main__":
    main()
