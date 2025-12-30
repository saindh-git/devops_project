import os

def get_security_grade(file_path):
    if not os.path.exists(file_path):
        return "NOT_FOUND"
    status = os.stat(file_path)
    lock = oct(status.st_mode)[-3:]
    if lock == "750": 
        return "SECURE"
    return "ACTION_REQUIRED"

estate_inventory = [
    "/home/sainadh/devops_projects/05_automated_inventory_management/inventory_check.py",
    "/home/sainadh/devops_projects/06_advanced_inventory_management/fleet_registry.py"
]

print("--- Starting Multi-Estate Security Audit ---")

for path in estate_inventory:
    resulth = get_security_grade(path)
    file_name = os.path.basename(path)
    print(f"File:{file_name} | Security Status: {resulth}")
