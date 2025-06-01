import hashlib

def double_sha256(data: bytes) -> bytes:
    hash1 = hashlib.sha256(data).digest()
    hash2 = hashlib.sha256(hash1).digest()
    return hash2

message = b'Hello, Bitcoin'
single_hash = hashlib.sha256(message).digest()
double_hash = double_sha256(message)

print(f"\nMessage: {message}")
print("\nSingle Hash")
print("=================")
print(f"SHA-256 (Raw bytes): {single_hash}")
print(f"SHA-256 (Hex string): {single_hash.hex()}")
print("\nDouble Hash")
print("=================")
print(f"SHA-256 (Raw bytes): {double_hash}")
print(f"SHA-256 (Hex string): {double_hash.hex()}")
