import os
import socket  


client= socket.socket(socket.AF_INET, socket.SOCK_STREAM, )
client.connect(("localhost",9999))

file = open("logo2.jpg","rb")                                           # name = input("Enter your name")
                                                                         # c.send(bytes(name,'utf-8'))
file_size = os.path.getsize("logo2.jpg")

client.send("recieved_logo2.jpg".encode())
client.send(str(file_size).encode())

data= file.read()
client.sendall(data)
client.send(b"<END>")

file.close()
client.close()
