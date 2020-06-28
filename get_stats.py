# Example of getting stats out of pickle file
import pickle
from CheckServer import Server

servers = pickle.load( open( "servers.pickle", "rb" ) )

for server in servers:
    server_up = 0
    for point in server.history:
        if point[1]:
            server_up += 1
    print(f"----------\n{server.name} has been up {server_up / len(server.history) * 100}\nTotal History: {len(server.history)}\n----------\n")