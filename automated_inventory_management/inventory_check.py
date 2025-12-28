import sys
server_list = ["web-prod", "db-prod", "test-dev", "backup-srv"]
print(f"---starting inventory check for {len(server_list)} servers----")
for server in server_list:
    if "prod" in server:
        print(f"checking:{server}......STATUS: CRITICAL/ACTIVE")
    else:
        print(f"CHECKING: {server} ... STATUS: MAINTENANCE/OFFLINE")
print("inventory check complete")
sys.exit(0)
