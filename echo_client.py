import socket

HOST= socket.gethostbyname(socket.gethostname())
PORT= 5050
ADDR =(HOST,PORT)


with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    print(ADDR)
    s.connect((HOST,PORT))
    
    s.sendall("hello world".encode('utf-8'))
    data = s.recv(1024).decode('utf-8')

print(f"Recieved {data}")

