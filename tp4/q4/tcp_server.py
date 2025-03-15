import socket

HOST = 'flavioshost'
PORT = 12345

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening in {HOST}:{PORT}")
        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connection established in {addr}")
                conn.sendall(b"Hello client TCP!")
                data = conn.recv(1024)
                print(f"Message received from client: {data.decode()}")

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        data = client_socket.recv(1024)
        print(f"Message received from server: {data.decode()}")
        client_socket.sendall(b"Hello server TCP!")

if __name__ == "__main__":
    import threading
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    import time
    time.sleep(3)
    start_client()