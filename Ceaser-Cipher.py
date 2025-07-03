def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # ord(char) gives the unicode number for the character, e.g., ord('A') = 65
            shifted = (ord(char) - start + shift) % 26 if mode == "encrypt" else (ord(char) - start - shift) % 26
            result += chr(start + shifted)
        else:
            result += char  # leave spaces/punctuation unchanged
    return result

# Example usage
message = "Hello, World!"
shift = 3

encrypted = caesar_cipher(message, shift, "encrypt")
decrypted = caesar_cipher(encrypted, shift, "decrypt")

print("Original: ", message)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)