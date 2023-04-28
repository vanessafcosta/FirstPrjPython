def encode(text, key):
    #print(f"Here we get the parameters text: {text} and key:{key}")
    cipher = make_cipher(key)
    #print(f"Cipher: {cipher}")

    ciphertext_chars = []
    
    for i in text:
        # print(f"This is the i variable: {i}")
        # print(f"This is the cipher.index(i): {cipher.index(i)}")
        ciphered_char = chr(65 + cipher.index(i))
        #print(f"ciphertext_chars: {ciphertext_chars} inside for loop // cipher.index(i): {cipher.index(i)}")
        ciphertext_chars.append(ciphered_char)
        #print (f"final ciphertext_chars: {ciphertext_chars}")

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    #print(f"Here we get the parameters encrypted: {encrypted} and key:{key}")
    cipher = make_cipher(key)
    #print(f"Cipher: {cipher}")

    plaintext_chars = []
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        #print(f"plain_char: {plain_char} inside for loop // cipher[65 - ord(i): {cipher[ord(i)  - 65]}")
        plaintext_chars.append(plain_char)
        #print (f"final plaintext_chars: {plaintext_chars}")

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 96) for i in range(1, 27)]
    #print(f"Alphabet variable: {alphabet}")
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
