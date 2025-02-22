from Cryptodome.Cipher import ChaCha20
from Cryptodome.Random import get_random_bytes

message = "Pay $2000 to Bob"

key = bytes([0x81] * 32)  
nonce = bytes([0x18] * 12) 

cipher = ChaCha20.new(key=key, nonce=nonce)
ciphertext = cipher.encrypt(message.encode())

with open("ciphertext.txt", "w") as f:
    f.write(ciphertext.hex())

cipher_decode = ChaCha20.new(key=key, nonce=nonce)
decoded_text = cipher_decode.decrypt(ciphertext).decode()

print(f"Plaintext in text: {message}")
print(f"Plaintext in hex: {message.encode().hex()}")
print(f"Key in hex: {key.hex()}")
print(f"Nonce in hex: {nonce.hex()}")
print(f"Ciphertext in hex: {ciphertext.hex()}")
print(f"Decrypted plaintext: {decoded_text}")
