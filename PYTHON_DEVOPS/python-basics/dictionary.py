thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

server_list = {
    "name": "web-server",
    "cpu": 75,
    "disk": 60
}

print("Server:", server_list["name"])
print("CPU Usage:", server_list["cpu"])
print("Disk Usage:", server_list["disk"])


servers = [
    {"name": "web1", "status": "running", "cpu": 50},
    {"name": "web2", "status": "stopped", "cpu": 85},
    {"name": "db1", "status": "running", "cpu": 90}
]
for server in servers:
    if server["cpu"] > 80:
        print("The server name is", server["name"])
