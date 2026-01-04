import json

estate_data = {
    "gate_status": "locked",
    "guards_on_duty": 4,
    "cameras_active": True
}


print("---consultant packing the ledger---")
json_string = json.dumps(estate_data)

print(f"json string for network:{json_string}")

new_string = json.loads(json_string)
print(f"back to python:{new_string['gate_status']}")

