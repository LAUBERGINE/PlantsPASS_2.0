from aes import chiffrement_aes, dechiffrement_aes

def aes(hash_password, password):
    firstKey = bytes.fromhex(hash_password[:64]) 
    firstIv = bytes.fromhex(hash_password[:32])
    
    secondKey = bytes.fromhex(hash_password[64:128]) 
    secondIv = bytes.fromhex(hash_password[64:96])
    
    nPassword = chiffrement_aes(password, firstKey, firstIv)
    finalPassword = chiffrement_aes(nPassword, secondKey, secondIv)
    
    return finalPassword

def daes(hash_password, finalPassword):
    firstKey = bytes.fromhex(hash_password[:64]) 
    firstIv = bytes.fromhex(hash_password[:32])
    
    secondKey = bytes.fromhex(hash_password[64:128]) 
    secondIv = bytes.fromhex(hash_password[64:96])
    
    d1Password = dechiffrement_aes(finalPassword, secondKey, secondIv)
    clearPassword = dechiffrement_aes(d1Password, firstKey, firstIv)
    
    return clearPassword
    