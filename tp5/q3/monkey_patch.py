import socket, ssl

SERVER, PORT = "flavioshost", 4444

context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations("certificate.pem")
context.check_hostname = False
context.verify_mode = ssl.CERT_REQUIRED

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
secure = context.wrap_socket(client, server_hostname=SERVER)

secure.connect((SERVER, PORT))
print(f'Connected to {SERVER}')

_send = secure.send
def send_intercepted(data):
    data = bytes(data)
    print(f"Itercepted(send):", data.decode())
    return _send(data)
secure.send = send_intercepted

_recv = secure.recv
def receipt_intercepted(data):
    data = _recv(data)
    print(f"Intercepted(recv):", data.decode())
    return data
secure.recv = receipt_intercepted

message = "Hello server TLS"
secure.sendall(message.encode())

data = secure.recv(1024)
print(f'Received from server: {data.decode()}')
secure.close()