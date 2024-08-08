def encrypt(message, shift):
    encrypted = ""
    for i, char in enumerate(message):
        if char.isalpha():  # Check if the character is a letter
            shift_amount = (shift + i) % 26  # Variable shift based on position
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            encrypted += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            encrypted += char  # Non-alphabetical characters are not encrypted
    return encrypted

def decrypt(message, shift):
    decrypted = ""
    for i, char in enumerate(message):
        if char.isalpha():  # Check if the character is a letter
            shift_amount = (shift + i) % 26  # Variable shift based on position
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            decrypted += chr((ord(char) - start - shift_amount) % 26 + start)
        else:
            decrypted += char  # Non-alphabetical characters are not decrypted
    return decrypted

# Example usage
original_message = "Hello, World!"
shift = 4  # The initial shift value for the encryption

encrypted_message = encrypt(original_message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print("Original:", original_message)
print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
