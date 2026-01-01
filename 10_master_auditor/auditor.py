import json
import os

def is_emergency(filepath):
    try:
        with open(filepath,"r") as file:
            data=json.load(filepath)
        if data.get("health_check") == False or data.get("load",0) > 90:
            return True
        return False
    except Exception:
        return False
files_to_audit = ["broken_server.json"]
print("--- Master Auditor Starting ---")

for report in files_to_audit:
   if is_emergency(report):
       print(f"[ALERT] {report} represents a CRITICAL system state!")
   else:
       print(f"[INFO] {report} is within normal parameters.")
