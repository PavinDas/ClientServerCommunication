import socket
import time

def start_server(host='127.0.0.1', port=5050):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    print("Connection closed by client")
                    break
                message = data.decode()
                print(f"Received: {message}")
                log_message_to_file(addr[0], message) 
                conn.sendall(data)  

def log_message_to_file(ip, message):
    with open("network_logs.txt", "a") as log_file:
        log_file.write(f"{ip} - - [{time.strftime('%d/%b/%Y:%H:%M:%S %z')}] \"{message}\"\n")

if __name__ == "__main__":
    start_server()
