
for i in range (5):
    if i == 2:
        print("Hello World")
        break
    else:
        print("No World")

servers = ["server1", "server2", "server3"]
servers.append("server4")
for server in servers:
    print("Checking server", server)


print (servers)