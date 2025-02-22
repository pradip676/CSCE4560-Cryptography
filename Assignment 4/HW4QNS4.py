from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad

key = bytes.fromhex('11821781' * 4)
message = "Hello, World!!!_Hello, Alice!!_"

padded_message = pad(message.encode(), AES.block_size)
cipher = AES.new(key,AES.MODE_ECB)
ciphertext = cipher.encrypt(padded_message)

unpadded_message = cipher.decrypt(ciphertext)
decoded_text = unpad(unpadded_message, AES.block_size).decode()

print("Message:", message)
print("Ciphertext in Hex:",ciphertext.hex())
print("Decrypted text:", decoded_text)
