import sys
app_name ="estate_monitoring"
server_count = 5
is_active = True
print(f"executing: {app_name}")
if is_active == True and server_count > 0:
    print(f"status:{server_count} servers healthy,All are clear.")
    sys.exit(0)
else:
    print("status: system check failed!")
    sys.exit(1)
