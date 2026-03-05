servers = [
    {"name": "web1", "cpu": 50},
    {"name": "web2", "cpu": 85},
    {"name": "db1", "cpu": 90}
]

def check_cpu (server):
    if server["cpu"] > 80:
        print("The server", server["name"], "has critial cpu usgae", server["cpu"])

for server in servers:
    check_cpu(server)

    