def encode(text, key):
    cipher = make_cipher(key)

    # Defining a function taking two args (text and key). 
    # Creating a variable "cipher" and passing key through 
    # a function that we define later (make_cipher)

    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)

# Looping through ech letter and changing it into a different letter 
# Then appending that to a new list called ciphertext_chars 

def decode(encrypted, key):
    ciphertext_chars = []
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        print("the below prints ciphered_char:")
        print(ciphered_char)
        ciphertext_chars.append(ciphered_char)
    return "".join(ciphertext_chars)
print("the below prints ciphertext_chars:")
print("".join(ciphertext_chars))


def make_cipher(key): # Defined function with 1 arg "key" which was defined 
    # on line 1 
    alphabet = [chr(i + 98) for i in range(1, 26)]
    print("the below is alphabet variable")  
    print(alphabet)
    # Creating an alphabet variable which is a list. 
    # Within list they are creating a coded alphabet 
    cipher_with_duplicates = list(key) + alphabet
    print("the below is cipher_with_duplicates variable:")  
    print(cipher_with_duplicates)
    # Creating variable 

    # print(cipher_with_duplicates)

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

print("the below is the result of encode function:")
print(encode("theswiftfoxjumpedoverthelazydog", "secretkey"))

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.

# print(f"""
#  Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)

# print(f"""
#  Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
# Expected: theswiftfoxjumpedoverthelazydog
#   Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
# """)
