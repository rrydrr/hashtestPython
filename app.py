import hashlib

def convert_to_sha256(string):
    sha256_hash = hashlib.sha256(string.encode()).hexdigest()
    return sha256_hash

def store_in_array(string):
    sha256_hash = convert_to_sha256(string)
    hash_array.append(sha256_hash)

# Create an empty array to store the SHA-256 hashes
hash_array = []

# Example usage
input_string = "Hello, World!"
store_in_array(input_string)

print(hash_array)
