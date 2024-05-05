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

# Create an empty array to store the SHA-256 hashes and strings
hash_array = []
string_array = []

# Inputting to an array of strings
while True:
    print("Input string ('end' will end the string input): ", end="")
    scanned = input()
    if scanned == "end":
        break
    string_array.append(scanned)

# Converting array of strings to SHA-256 hashes

for i in range(string_array):
    hash_array.append(convert_to_sha256(string_array[i]))
    
# Testing the stored SHA-256 using regular string

while True:
    print("Input string to check if string exists in hash array ('end' will end this process): ", end="")
    scanned = input()
    if scanned != "end":
        for i in range(hash_array):
            if scanned == hash_array[i]:
                print("String found!")
                found = True
    
        if not found:
            print("String not found")
    else:
        break