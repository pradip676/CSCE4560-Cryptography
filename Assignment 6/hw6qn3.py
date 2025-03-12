import hashlib
import random
import uuid

def weak24_hash(data):
    return hashlib.sha256(data.encode()).digest()[:3]

def generate_random_string():
    return uuid.uuid4().hex[:8]  

def find_collision():
    hashes = {}
    while True:
        msg = generate_random_string()
        hash_value = weak24_hash(msg)

        if hash_value in hashes:
            prev_msg = hashes[hash_value]
            if msg != prev_msg:
                print("Collision found between these inputs!")
                print(f"Message m0: {prev_msg}")
                print(f"Message m1: {msg}")
                print(f"WEAK24 Hash Value [H(m0) = H(m1)]: {hash_value.hex()}")
                return
        else:
            hashes[hash_value] = msg

find_collision()
