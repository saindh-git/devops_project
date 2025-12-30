import sys

servers =[
 {
"hostname": "web-prod-01",
"ip": "10.0.0.50",
"os": "Ubuntu 22.04",
"cpu": 2,
"status": "active"
},
{
"hostname": "web-prod-02",
"ip": "10.0.0.51",
"os": "Ubuntu 22.04",
"cpu": 3,
"status": "maintenance"
},
{
"hostname": "web-prod-0",
"ip": "10.0.0.52",
"os": "Ubuntu 22.04",
"cpu": 4,
# Notice: This server is MISSING the 'status' label!
}
]

print(f"--- Starting Fleet Security Audit ({len(servers)} Servers) ---")

for server in servers:
    name = server['hostname']

    if "status" in server:
        current_status = server['status']
        print(f"[warning] server:{name} | status:{current_status}")
    else:
        print(f"[WARNING] Server: {name} | Status: MISSING! (Check Required)")



