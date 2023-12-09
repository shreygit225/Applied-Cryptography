
def mod_exp(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result
 
# Diffie-Hellman Key Exchange
def diffie_hellman(prime, base):
    # Alice's private key
    a_private = int(input("Alice: Enter private key (a): "))
    # Bob's private key
    b_private = int(input("Bob: Enter private key (b): "))
 
    # Calculate public keys
    a_public = mod_exp(base, a_private, prime)
    b_public = mod_exp(base, b_private, prime)
 
    # Calculate shared secret
    alice_shared_secret = mod_exp(b_public, a_private, prime)
    bob_shared_secret = mod_exp(a_public, b_private, prime)
 
    # Print shared secrets
    print("\nShared Secret (Alice):", alice_shared_secret)
    print("Shared Secret (Bob):", bob_shared_secret)
 
# Example usage
if __name__ == "__main__":
    prime = int(input("Enter the prime number (p): "))
    base = int(input("Enter the base/generator (g): "))
    diffie_hellman(prime, base)
