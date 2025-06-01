from ecdsa import SigningKey, SECP256k1

private_key = SigningKey.generate(curve=SECP256k1)
public_key = private_key.verifying_key
message = b'Send 1 BTC to Justin'

# Sign the message using the private key.
signature = private_key.sign(message)

# Verify the signature using the public key.
is_valid = public_key.verify(signature, message)

print(f"\nPrivate Key: {private_key.to_string().hex()}")
print(f"Public Key: {public_key.to_string().hex()}")
print(f"\nSigning: {message}")
print(f"Signature Valid?: {is_valid}")
