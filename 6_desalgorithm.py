s_box = [
    [0b0000, 0b0001, 0b0010, 0b0011],
    [0b0100, 0b0101, 0b0110, 0b0111],
    [0b1000, 0b1001, 0b1010, 0b1011],
    [0b1100, 0b1101, 0b1110, 0b1111]
]
 
# Initial permutation (IP) matrix
initial_permutation = [2, 6, 3, 1, 4, 8, 5, 7]
 
# Expansion permutation (E) matrix
expansion_permutation = [4, 1, 2, 3, 2, 3, 4, 1]
 
# P-box permutation matrix
p_box_permutation = [2, 4, 3, 1]
 
def apply_permutation(block, permutation):
    result = [block[i - 1] for i in permutation]
    print("After permutation:", result)
    return result
 
def split_block(block):
    result = block[:4], block[4:]
    print("After splitting:", result)
    return result
 
def expand(right_half):
    result = apply_permutation(right_half, expansion_permutation)
    print("After expansion:", result)
    return result
 
def substitute(block):
    row = ((block[0] << 1) + block[3])  # Row is formed from first and fourth bits
    col = ((block[1] << 1) + block[2])  # Column is formed from the second and third bits
    result = bin(s_box[row][col])[2:].zfill(4)
    print("After substitution:", result)
    return result
 
def permute(block):
    result = apply_permutation(block, p_box_permutation)
 
    return result
 
def des_round(block, round_key):
    left_half, right_half = split_block(block)
    expanded = expand(right_half)
    xored = [int(expanded[i]) ^ round_key[i] for i in range(8)]
    substituted = substitute(xored)
    permuted = permute([int(bit) for bit in substituted])
    new_right_half = [left_half[i] ^ permuted[i] for i in range(4)]
    print("After DES round:", right_half + new_right_half)
    return right_half + new_right_half
 
# Take user input for plaintext and round key
plaintext_input = input("Enter 8-bit plaintext (e.g., 10100101): ")
round_key_input = input("Enter 8-bit round key (e.g., 10011010): ")
 
# Convert input strings to lists of integers
plaintext = [int(bit) for bit in plaintext_input]
round_key = [int(bit) for bit in round_key_input]
 
# Initial permutation (IP)
plaintext = apply_permutation(plaintext, initial_permutation)
 
# Perform a single round of DES
ciphertext = des_round(plaintext, round_key)
 
print("Final Ciphertext:", ciphertext)
