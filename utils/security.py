import hashlib

#transformer le password en byte
def hash_password(password):
    return hashlib.sha256(
        password.encode()
    ).hexdigest()