import socket

client = socket.socket()
client.connect(('localhost', 12345))

client.send(b"Hello from Client!")
response = client.recv(1024).decode()
print(f"Server: {response}")

client.close()
