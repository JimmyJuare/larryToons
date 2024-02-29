import secrets

secret_key = secrets.token_hex(32)  # 32 bytes (256 bits)

print(secret_key)
