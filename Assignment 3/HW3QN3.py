from Cryptodome.Cipher import ChaCha20

key = bytes([0x81] * 32)  
nonce = bytes([0x18] * 12)  

with open("ciphertext1.txt", "r") as f:
    modified_ciphertext_hex = f.read().strip() 

ciphertext_bytes = bytes.fromhex(modified_ciphertext_hex)
print("Modified Ciphertext in Hex:", modified_ciphertext_hex)

cipher_decode = ChaCha20.new(key=key, nonce=nonce)
decoded_text = cipher_decode.decrypt(ciphertext_bytes).decode()

print(f"Decrypted plaintext: {decoded_text}")
