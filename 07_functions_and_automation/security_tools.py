import os

def get_security_grade(filename):
    if not os.path.exists(filename):
        return "MISSING!"
    status = os.stat(filename)
    lock = oct(status.st_mode)[-3:]
    if lock == "750": 
        return "SENIOR"
    elif lock == "755":
        return "JUNIOR"
    else:
        return "UNSAFE"
target = "inventory_check.py"
grade = get_security_grade(target)

print(f"Audit Result for {target}: {grade}")

