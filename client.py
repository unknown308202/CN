import socket

def receive_file(file_name):
    # Create a socket object
    s = socket.socket()

    # Define the host and port (same as server)
    host = socket.gethostname()
    port = 12345

    # Connect to the server
    s.connect((host, port))
    print(f"Connected to server {host}:{port}")

    # Open a file to write the incoming data
    with open(file_name, 'wb') as f:
        print(f"Receiving file {file_name}...")
        data = s.recv(1024)
        while data:
            f.write(data)
            data = s.recv(1024)

    print("File transfer complete.")
    s.close()

if __name__ == "__main__":
    file_name = input("Enter the file name to save as: ")
    receive_file(file_name)
