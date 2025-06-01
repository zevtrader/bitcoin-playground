import hashlib

def hash_160(data: bytes) -> bytes:
    sha_hash = hashlib.sha256(data).digest()
    ripemd_hash = hashlib.new('ripemd160', sha_hash).digest()
    return ripemd_hash

public_key_hex = '08810f03577c62e5762318880a85a326'
public_key_bytes = bytes.fromhex(public_key_hex)
public_key_hash = hash_160(public_key_bytes)

print(f"Public Key Hash: {public_key_hash}")
