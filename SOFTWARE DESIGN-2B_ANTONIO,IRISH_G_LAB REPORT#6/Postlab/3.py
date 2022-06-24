import socket
import select
import sys
from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# checks whether sufficient arguments have been provided
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
exit()
# takes the first argument from command prompt as IP address
IP_address = str(sys.argv[1])
# takes second argument from CMD as port number
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(100)
list_of_clients = []
def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!")
    while True:
            message = conn.recv(2048)
            if message:
                print ("<" + addr[0] + "> " + message)
# Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            try:
                remove(conn)
            except:
                continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()
# if the link is broken, we remove the client
    remove(clients)
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
    while True:
        conn, addr = server.accept()
list_of_clients.append(conn)
print (addr[0] + " connected")
start_new_thread(clientthread,(conn,addr))
conn.close()
server.close()

#CLIENT SIDE SCRIPT
import socket
import select
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print ("Correct usage: script, IP address, port number")
exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
while True:
    sockets_list = [sys.stdin, server]
read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
for socks in read_sockets:
    if socks == server:
        message = socks.recv(2048)
    print(message)
else:
    message = sys.stdin.readline()
server.send(message)
sys.stdout.write("<You>")
sys.stdout.write(message)
sys.stdout.flush()
server.close()