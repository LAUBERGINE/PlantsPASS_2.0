import hashlib

def sha512(password):
    
    encoded_string = password.encode()
    sha512_hash = hashlib.sha512()
    sha512_hash.update(encoded_string)
    sha512_hex = sha512_hash.hexdigest()
    
    return sha512_hex
