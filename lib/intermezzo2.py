def encode(text, key):
    cipher = make_cipher(key)
    print("The below prints cipher variable")  
    print(cipher)
   # Defining a function taking two args (text and key). 
    # Creating a variable "cipher" and passing key through 
    # a function that we define later (make_cipher)

  #The below function is Looping through ech letter and changing it into a different letter 
# Then appending that to a new list called ciphertext_chars 
    ciphertext_chars = []
    for i in text:
        print(i)
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)
        #print("The below prints the ciphertext_chars variable")
        #print(ciphertext_chars)
    print("The below prints the completed ciphertext_chars list")
    print(ciphertext_chars)
    print("The below prints "".join(ciphertext_chars)")
    print("".join(ciphertext_chars))
    return "".join(ciphertext_chars)
  

#The below function reverses the encode function. It does this by looping through each item and appending the decoded character to a new list. It returns a string, created from a this list of decoded characters.

def decode(encrypted, key):
    cipher = make_cipher(key)

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[65 - ord(i)]
        print("the below prints the plain_char character")
        print(plain_char)
        plaintext_chars.append(plain_char)

    print("The below prints "".join(plaintext_chars) ")
    print("".join(plaintext_chars))
    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 98) for i in range(1, 26)]
    print("the below is alphabet variable")  
    print(alphabet)
    cipher_with_duplicates = list(key) + alphabet
    print("the below is cipher_with_duplicates variable")  
    print(cipher_with_duplicates)
    #print(len(cipher_with_duplicates))


    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        print(f"The item in this loop is {i}")
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    print(f"The length of the cipher variable is {len(cipher)}")
    return cipher


print(encode("theswiftfoxjumpedoverthelazydog", "secretkey"))

# Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
#   Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
# """)