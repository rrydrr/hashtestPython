import hashlib


def convert_to_sha256(string):
    """
    Converts a given string to its SHA-256 hash value.

    Args:
        string (str): The string to be converted.

    Returns:
        str: The SHA-256 hash value of the input string.
    """
    sha256_hash = hashlib.sha256(string.encode()).hexdigest()
    return sha256_hash

def store_in_array(string):
    """
    Stores the SHA256 hash of a string in an array.

    Args:
        string (str): The string to be hashed and stored.

    Returns:
        None
    """
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
