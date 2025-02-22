from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter

key = bytes([0x81] * 16)
nonce = bytes ([0x18] * 8)

message = "Pay $2000 to Bob"
message_bytes = message.encode()

ctr = Counter.new(64, prefix = nonce, little_endian=False)

cipher = AES.new(key, AES.MODE_CTR, counter = ctr)
ciphertext = cipher.encrypt(message_bytes)

with open("ciphertext.txt", "w") as f:
    f.write(ciphertext.hex())

ctr = Counter.new(64, prefix = nonce, little_endian = False)
decoding = AES.new(key, AES.MODE_CTR, counter = ctr)
plaintext = decoding.decrypt(ciphertext).decode()

print("Plaintext in text:" + message)
print("Key in hex:" + key.hex())
print("Nonce in hex:" + nonce.hex())
print("Ciphertext in hex: " + ciphertext.hex())
print("Decrypted text: " + plaintext) 
