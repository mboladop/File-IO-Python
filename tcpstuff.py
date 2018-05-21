import socket

IP = '127.0.0.1'
PORT = 5555
MAXIMUM_QUEUE_SIZE = 0

listening_socket= socket.socket()
listening_socket.bind((IP, PORT))

listening_socket.listen(MAXIMUM_QUEUE_SIZE)
print("waiting for connection")

(client_socket, client_ip_and_port)= listening_socket.accept()
response="my response".encode()
client_socket.send(response)

print("bye bye")