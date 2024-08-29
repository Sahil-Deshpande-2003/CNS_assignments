import socket

def xor_encrypt_decrypt(message, key):
    encrypted_decrypted = bytearray()
    for m, k in zip(message, key * (len(message) // len(key) + 1)):
        encrypted_decrypted.append(m ^ k)
    return bytes(encrypted_decrypted)

def main():
    host = '127.0.0.1'
    port = 65432

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen() # server_socket.listen() puts the server into listening mode, ready to accept connections.

    print(f"Server listening on {host}:{port}")
    
    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break

            # Decrypt received message
            decrypted_message = xor_encrypt_decrypt(data, b'secretkey')
            print(f"Received (encrypted): {data}")
            print(f"Received (decrypted): {decrypted_message.decode()}")

            if decrypted_message.decode().lower() == 'quit':
                print("Client has terminated the connection.")
                break

            # Ask for a response message from the server user
            response_message = input("Enter your response (type 'quit' to end): ").encode()
            if response_message.decode().lower() == 'quit':
                encrypted_response = xor_encrypt_decrypt(response_message, b'secretkey')
                conn.sendall(encrypted_response)
                print("Closing connection as requested.")
                break
            
            # Encrypt and send the response
            encrypted_response = xor_encrypt_decrypt(response_message, b'secretkey')
            print(f"Sending (encrypted): {encrypted_response}")
            conn.sendall(encrypted_response)

        conn.close()
        break

if __name__ == "__main__":
    main()
