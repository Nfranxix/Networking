import socket
import threading

HOST = "FRANXIX"
PORT = 55500
ADDR = (HOST,PORT)
FORMAT = "utf-8"

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(ADDR)
server.listen()
print("[LISTENING].....")
print(ADDR)

clients = {}




def broadcast(message):
    for client in clients:
        # client.send("Somebody is typing ....".encode(FORMAT))
        client.send(message)
        # print(f"{nickname} is typing ....".encode(FORMAT))

for x,h in clients.items():
        key = x
        nickname = h




def handle(client):
        while True:
            try:
                message = client.recv(1024)
                broadcast(message)
            except:
                clients.pop(client)
                client.send("You have been disconnected from the group".encode(FORMAT))
                broadcast(f"{nickname} has left the chat".encode(FORMAT))
                break

def recieve():
        while True:
            client , address = server.accept()
            print(f"Connected to {str(address)}")
            # client = key
            client.send("NICK".encode(FORMAT))
            news = client.recv(1024).decode(FORMAT)
            clients[client] = news

            print(f"Nickname of client is {news}")
            broadcast(f"{news} joined the chat".encode(FORMAT))
            client.send("Connected to server".encode(FORMAT))

            thread = threading.Thread(target=handle , args=(client,))
            thread.start()     

            print(f"[ACTIVE CONNECTIONS] {threading.active_count()  -1}")



# thread = threading.Thread(target=handle , args=clients)
# thread.start()

recieve()
     



                
        

