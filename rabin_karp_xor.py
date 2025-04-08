def rolling_hash(text, base=256, prime=101):
    hash_val = 0
    for char in text:
        hash_val = (hash_val * base + ord(char)) % prime
    return hash_val
