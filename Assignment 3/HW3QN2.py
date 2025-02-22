from Cryptodome.Cipher import ChaCha20
import math

key = bytes([0x81] * 32)  
nonce = bytes([0x18] * 12)  

cipher = ChaCha20.new(key=key, nonce=nonce)
keystream = cipher.encrypt(bytes([0x00] * 256)) 

with open("keystream.txt", "w") as f:
    f.write(keystream.hex())

bit_string = ""
for byte in keystream:
    bit_string += f"{byte:08b}"  

n = len(bit_string)  
S_n = sum(1 if bit == '1' else -1 for bit in bit_string)

s_obs = abs(S_n) / math.sqrt(n)

p_value = math.erfc(s_obs / math.sqrt(2))

print(f"(input) ε = {bit_string[:100]}")
print(f"n = {n}")
print(f"S_{n} = {S_n}")
print(f"S_obs = {s_obs:.6f}")
print(f"P-value = {p_value:.6f}")

if p_value < 0.01:
    print("Conclusion: Since P-value < 0.01, accept the sequence as non-random.")
else:
    print("Conclusion: Since P-value >= 0.01, accept the sequence as random.")
   
