import socket

server = socket.socket()
server.bind(('localhost', 12345))
server.listen(1)
print("Waiting for connection...")

client, addr = server.accept()
print(f"Connected to {addr}")

msg = client.recv(1024).decode()
print(f"Client: {msg}")

client.send(b"Hello from Server!")
client.close()
server.close()

