# Python3 code to implement Hill Cipher

keyMatrix = [[0] * 3 for i in range(3)]

# Generate vector for the message
messageVector = [[0] for i in range(3)]

# Generate vector for the cipher
cipherMatrix = [[0] for i in range(3)]

# Function to generate the key matrix for the key string
def getKeyMatrix(key):
    k = 0
    for i in range(3):
        for j in range(3):
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1

# Function to encrypt the message
def encrypt(messageVector):
    for i in range(3):
        for j in range(1):
            cipherMatrix[i][j] = 0
            for x in range(3):
                cipherMatrix[i][j] += (keyMatrix[i][x] *
                                       messageVector[x][j])
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26

def HillCipher(message, key):
    # Get key matrix from the key string
    getKeyMatrix(key)

    # Generate vector for the message
    for i in range(3):
        messageVector[i][0] = ord(message[i]) % 65

    # Encrypt the message
    encrypt(messageVector)

    # Generate the ciphertext from the encrypted vector
    CipherText = []
    for i in range(3):
        CipherText.append(chr(cipherMatrix[i][0] + 65))

    # Print the ciphertext
    print("Ciphertext: ", "".join(CipherText))

# Main function to take input from the user
def main():
    # Take message input from the user
    message = input("Enter the 3-letter message (in uppercase): ")

    # Validate message input
    while len(message) != 3 or not message.isalpha() or not message.isupper():
        message = input("Please enter a valid 3-letter message (in uppercase): ")

    # Take key input from the user
    key = input("Enter the 9-letter key (in uppercase): ")

    # Validate key input
    while len(key) != 9 or not key.isalpha() or not key.isupper():
        key = input("Please enter a valid 9-letter key (in uppercase): ")

    HillCipher(message, key)

if __name__ == "__main__":
    main()
