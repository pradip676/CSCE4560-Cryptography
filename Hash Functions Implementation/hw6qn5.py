from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256

# (1) Generate a key pair and store in the file
secret_key = ECC.generate(curve="P-256")
pk = secret_key.public_key()

with open("sk.key", "wt") as file_sk:
    file_sk.write(secret_key.export_key(format="PEM"))

with open("pk.key", "wt") as file_pk:
    file_pk.write(pk.export_key(format="PEM"))

# 2) Create a file “message.txt” containing the text “Hello, World!”, 
message = "Hello, World!"
message_bytes = message.encode('utf-8')  

with open("message.txt", "wb") as file_msg:
    file_msg.write(message_bytes)

# Compute the digital sig with secret key and store in file
with open("sk.key", "rt") as file_sk:
    secret_key = ECC.import_key(file_sk.read())

hash_value = SHA256.new(message_bytes)
signer = DSS.new(secret_key, 'fips-186-3')
signature = signer.sign(hash_value)

with open("sig.bin", "wb") as sig_file:
    sig_file.write(signature)

# (3)Verify digital signature with public key
with open("pk.key", "rt") as file_pk:
    pk = ECC.import_key(file_pk.read())

with open("message.txt", "rb") as f:
    initial_msg = f.read()

print("Original Message:", message)
print("Original Hash in hex:", hash_value.hexdigest())

with open("sig.bin", "rb") as f:
    signature = f.read()

initial_hash = SHA256.new(initial_msg)
toVerify = DSS.new(pk, 'fips-186-3')
try:
    toVerify.verify(initial_hash, signature)
    print("Verifiction 1 Successful: Valid Signature.")
except ValueError:
    print("Verifiction 1 failed: Invalid Signature.")

# (4) Modify message
with open("message.txt", "rb") as f:
    message2 = f.read()

replace = b'J' + message2[1:]  

with open("message.txt", "wb") as f:
    f.write(replace)

with open("message.txt", "rb") as f:
    modified_message = f.read()

print("\nModified Message:", modified_message.decode())

modified_hash = SHA256.new(modified_message)
print("Modified Hash in hex:", modified_hash.hexdigest())

try:
    toVerify.verify(modified_hash, signature)
    print("Verifiction 2 Successful: Valid Signature.")
except ValueError:
    print("Verifiction 2 failed: Invalid Signature.")
