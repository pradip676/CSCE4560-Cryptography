from Cryptodome.Cipher import AES
import math

key = bytes ([0x81] * 16)

pseudor_sequence = bytes()
for i in range(16):
    block_input = i.to_bytes(16,'big')
    cipher = AES.new(key, AES.MODE_ECB)
    pseudor_sequence +=cipher.encrypt(block_input)   

bit_string = ""
for byte in pseudor_sequence:
    bit_string += f"{byte:08b}" 

n = len(bit_string)  
S_n = sum(1 if bit == '1' else -1 for bit in bit_string)

s_obs = abs(S_n) / math.sqrt(n)

p_value = math.erfc(s_obs / math.sqrt(2))  

print(f"(input) ε : {bit_string[:100]}")
print(f"n: {n}")
print(f"S_{n}: {S_n}")
print(f"S_obs:{s_obs:.1f}")
print(f"P-value:{p_value:.6f}")

if p_value < 0.01:
    print("Conclusion: Since P-value < 0.01, accept the sequence as non-random.")
else:
    print("Conclusion: Since P-value >= 0.01, accept the sequence as random.")

