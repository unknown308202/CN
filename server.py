import socket

def send_file(file_name):
    # Create a socket object
    s = socket.socket()

    # Define the port and host
    host = socket.gethostname()  # Use local machine name
    port = 12345  # Port to listen on

    # Bind the socket to the host and port
    s.bind((host, port))

    # Put the socket into listening mode
    s.listen(5)
    print(f"Waiting for connection on {host}:{port}")

    # Wait for a connection
    conn, addr = s.accept()
    print(f"Got connection from {addr}")

    # Open the file to send in binary mode
    with open(file_name, 'rb') as f:
        print(f"Sending file {file_name}...")
        data = f.read(1024)
        while data:
            conn.send(data)
            data = f.read(1024)

    print("File transfer complete.")
    conn.close()

if __name__ == "__main__":
    file_name = input("Enter the file name to send: ")
    send_file(file_name)
