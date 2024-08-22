import socket

def xor_encrypt_decrypt(message, key):
    encrypted_decrypted = bytearray() #  mutable sequence of bytes
    for m, k in zip(message, key * (len(message) // len(key) + 1)): # key should be repeated enough times so that it can match the len of message
        encrypted_decrypted.append(m ^ k) # XOR operation
    return bytes(encrypted_decrypted)

def main():
    host = '127.0.0.1'
    port = 65432

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.socket(socket.AF_INET, socket.SOCK_STREAM) initializes a new socket using IPv4 addressing (AF_INET) and TCP protocol (SOCK_STREAM).
    client_socket.connect((host, port))

    while True:
        # Ask for a message from the client user
        message = input("Enter your message (type 'quit' to end): ")
        # Encrypting the message
        encrypted_message = xor_encrypt_decrypt(message.encode(), b'secretkey')
        print(f"Sending (encrypted): {encrypted_message}")
        client_socket.sendall(encrypted_message)

        if message.lower() == 'quit':
            print("Exiting as requested.")
            break

        # Receiving and decrypting response
        data = client_socket.recv(1024) # the 1024 specifies the maximum number of bytes of data that the recv function should read from the socket at one time
        print(f"Received (encrypted): {data}")
        decrypted_message = xor_encrypt_decrypt(data, b'secretkey')
        print(f"Received (decrypted): {decrypted_message.decode()}")

        if decrypted_message.decode().lower() == 'quit':
            print("Server has terminated the connection.")
            break

    client_socket.close()

if __name__ == "__main__":
    main()
