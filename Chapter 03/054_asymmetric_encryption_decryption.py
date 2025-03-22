# Script: 054_asymmetric_encryption_decryption.py

# Importing necessary modules from cryptography for RSA encryption and decryption
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Generate private and public RSA keys
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=default_backend())
public_key = private_key.public_key()

# Encrypting the data using the public key and OAEP padding
encrypted = public_key.encrypt(
    b"secret data",
    padding.OAEP(
        padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypting the data using the private key and the same padding scheme
decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
