import sys

server_01 = {
"hostname": "web-prod-01",
"ip": "10.0.0.50",
"os": "Ubuntu 22.04",
"cpu": 2,
}

print("--- Accessing the Filing Cabinet ---")
print(f"Server Name:{server_01['hostname']}")
print(f"Target Ip:{server_01['ip']}")

requested_info = "Memory"

if requested_info in server_01:
    print(f"Memory:{server_01[requested_info]}")
else:
    print(f"ERROR:The Label {requested_info} was not found in the cabinet")

