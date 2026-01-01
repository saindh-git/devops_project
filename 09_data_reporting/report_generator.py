import json

server_data = {
    "hostname": "prod-app-01",
    "ip": "10.0.0.100",
    "services": ["nginx", "postgresql", "redis"],
    "health_check": True
}

json_string = json.dumps(server_data,indent=4)

print("----The JSON Translator Output-----")
print(json_string)


with open("server_report.json","w") as file:
    file.write(json_string)
print("\n[SUCCESS] Report saved as 'server_report.json'")
