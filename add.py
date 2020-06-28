# Simple program to add a server after you have 
# Created your pickle file
# Could create a file to delete or modify servers as well

import pickle
from CheckServer import Server

servers = pickle.load( open( "servers.pickle", "rb" ) )

print("Example to add server")

servername = input("enter server name")
port = int(input("Enter a port number as integer"))
connection = input("Enter a type ping/plain/ssl")
priority = input("Enter priority high/low")

new_server = Server(servername, port, connection, priority)
servers.append(new_server)

pickle.dump(servers, open("servers.pickle", "wb" ))