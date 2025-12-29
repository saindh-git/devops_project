import os
import sys
target_file = "inventory_check.py" 
senior_lock = 0o750
print(f"--- Architect Audit: Checking {target_file} ---")
if os.path.exists(target_file):
    current_status=os.stat(target_file)
    print(f"{current_status}")
    readable_perm = oct(current_status.st_mode)[-3:]
    print(f"Current Lock is: {readable_perm}")
    if readable_perm != "750":
        print("ACTION: Lock is weak! Upgrading to Senior Lock (750)...")
        os.chmod(target_file,senior_lock)
        print("RESULT: Estate Secured.")
    else:
        print("RESULT: Lock is already Senior Grade. No action needed.")
else:
    print(f"CRITICAL: {target_file} is missing from the Estate!")
    sys.exit(1)
sys.exit(0)
