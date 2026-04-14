with open ("servers.txt", "r") as file:
    for server in file:
        print("Server is:", server.strip())

