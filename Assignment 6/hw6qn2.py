import hashlib

message = "Hello, World!"

sha256_hash = hashlib.sha256(message.encode())

hash_digest= sha256_hash.digest()

weak24_hash = hash_digest[:3].hex()

print("Message:", message)
print("WEAK24 Hash :", weak24_hash)