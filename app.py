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
scanned = input()
input_string = scanned
store_in_array(input_string)

print(hash_array)

print("Try to verify using the same input")

if convert_to_sha256(scanned) == hash_array[0]:
    print("verfied")
else:
    print("not verified")
