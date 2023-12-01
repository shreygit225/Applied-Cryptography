


ip = [2, 4, 6, 8, 1, 3, 5, 7]


expansion_p_box = [1, 2, 3, 4, 4]



plaintext = input("Enter 8 bit Plain text: ")


plaintext = [int(bit) for bit in plaintext]


permuted_plaintext = [plaintext[i - 1] for i in ip]
print("Initial Permuted plain text: ",permuted_plaintext)


left_half = permuted_plaintext[:4]
right_half = permuted_plaintext[4:] 
print("Left half and Right half: ",left_half,right_half)


round_key = "10011"
round_key = [int(bit) for bit in round_key]

print("Round Key:",round_key)

# round xor right half

expanded_right_half = [right_half[i - 1] for i in expansion_p_box]
expanded_left_half = [left_half[i - 1] for i in expansion_p_box]


print("5 bit left half:", expanded_left_half)
print("5 bit right half:", expanded_right_half)

key_right = [r^k for r,k in zip(expanded_right_half,round_key)]

print("F(Right,Key): ",key_right)


xor_result = [left_bit ^ round_key_bit for left_bit, round_key_bit in zip(expanded_left_half, key_right)]
print("after key operation with left half:" , xor_result)

straight_p_box = [2, 4, 3, 1]
new_left_half = [xor_result[i - 1] for i in straight_p_box]
print("P box operation:", new_left_half)


new_plaintext = right_half + new_left_half


print("Cipher text (8 bits) after swapping:", ''.join(map(str, new_plaintext)))
