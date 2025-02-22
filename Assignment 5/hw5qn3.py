from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

key = bytes([0x81]*16)
iv = bytes([0x18]*16)

message = "Pay $2000 to Bob"
message_bytes = message.encode()

padded_message = pad(message_bytes, AES.block_size)

cipher = AES.new(key, AES.MODE_CBC, iv = iv)
ciphertext = cipher.encrypt(padded_message)

with open("ciphertext.txt", "w") as f:
    f.write(ciphertext.hex())

decoding = AES.new(key, AES.MODE_CBC, iv=iv)
padded_decrypted = decoding.decrypt(ciphertext)
plaintext = unpad(padded_decrypted, AES.block_size).decode()

print("Plaintext in text: " + message)
print("Key in hex: " + key.hex())
print("IV in hex: " + iv.hex())
print("Ciphertext in hex: "+ ciphertext.hex())
print("Decrypted text: " + plaintext)


