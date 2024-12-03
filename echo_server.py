import socket

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR =(HOST , PORT)
print(socket.gethostname())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(ADDR)
    s.listen(1)
    print("[LISTENING].....")
    
    
    
    while True:
            conn, addr = s.accept()
            print(f"[CONNECTED BY] {addr}")
            data = conn.recv(1024).decode('utf-8')
            print(f"Message from client : {data}")
            
            conn.sendall(data.encode('utf-8'))
            
