def initial_key_permutation(key):
    pc1 = [
        57, 49, 41, 33, 25, 17, 9, 1,
        58, 50, 42, 34, 26, 18, 10, 2,
        59, 51, 43, 35, 27, 19, 11, 3,
        60, 52, 44, 36, 63, 55, 47, 39,
        31, 23, 15, 7, 62, 54, 46, 38,
        30, 22, 14, 6, 61, 53, 45, 37,
        29, 21, 13, 5, 28, 20, 12, 4,
    ]

    permuted_key = [key[bit - 1] for bit in pc1]
    return permuted_key

def circular_left_shift(bits, shift_amount):
    return bits[shift_amount:] + bits[:shift_amount]

def compression_permutation(key56):
    pc2 = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32,
    ]

    permuted_key = [key56[bit - 1] for bit in pc2]
    return permuted_key

input_key = "0001001100110100010101110111100110011011101111001101111111110001"

key = [int(bit) for bit in input_key]

key56 = initial_key_permutation(key)

left_half = key56[:28]
right_half = key56[28:]

shift_amount = 1  
left_half = circular_left_shift(left_half, shift_amount)
right_half = circular_left_shift(right_half, shift_amount)

key56 = left_half + right_half

final_key48 = compression_permutation(key56)

final_key = ''.join(map(str, final_key48))

print("Generated 48-bit DES key:")
print(final_key)
