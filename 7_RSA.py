import math

# Step 1: Take user input for prime numbers p and q
p = int(input("Enter a prime number (p): "))
q = int(input("Enter another prime number (q): "))

# Step 2: Calculate n

n = p * q
print("n =", n)

# Step 3: Calculate phi(n)
phi = (p - 1) * (q - 1)
print("phi(n) =", phi)

# Step 4: Choose e (public key)
e = int(input(f"Choose a number e such that 1 < e < {phi} and gcd(e, {phi}) = 1: "))
while math.gcd(e, phi) != 1:
    e = int(input("Invalid e. Choose another e: "))

# Step 5: Calculate d (private key) using modular multiplicative inverse
d = pow(e, -1, phi)
print("d =", d)
print(f'Public key: ({e}, {n})')
print(f'Private key: ({d}, {n})')

# Step 6: Take user input for the plaintext message
msg = int(input("Enter the message you want to encrypt (as an integer): "))
print(f'Original message: {msg}')

# Step 7: Encryption
C = pow(msg, e, n)
print(f'Encrypted message: C ≡ {msg}^{e} (mod {n}) = {C}')

# Step 8: Decryption
M = pow(C, d, n)
print(f'Decrypted message: M ≡ {C}^{d} (mod {n}) = {M}')
