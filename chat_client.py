import socket 
import threading

HOST = "FRANXIX"
PORT = 55500
ADDR = (HOST,PORT)
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client.connect(ADDR)

nickname = input("Please enter your nickname: ")

def recieve():
    while True:
        try:
            message = client.recv(1024).decode(FORMAT)
            if message == "NICK":
                client.send(nickname .encode(FORMAT))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break



def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode(FORMAT))

recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

        
