from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter

key = bytes([0x81] * 16)
nonce = bytes([0x18]*8)

with open ("ciphertext1.txt", "r") as f:
    modified_ciphertext_hex = f.read().strip()

ciphertext_bytes = bytes.fromhex(modified_ciphertext_hex)

ctr = Counter.new(64, prefix = nonce, little_endian = False)
decoding = AES.new(key, AES.MODE_CTR, counter = ctr)
decoded_text = decoding.decrypt(ciphertext_bytes).decode()

print("Modified ciphertext: " + modified_ciphertext_hex)
print("Decrypted plaintext: " + decoded_text)
