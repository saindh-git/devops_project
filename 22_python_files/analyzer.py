import os

error_count = 0

with open("estate.log","r") as file:
    for line in file:
        if "ERROR" in line:
            print(f"error found in{line.strip()}")
            error_count += 1
print("-------------------------------------------------")
print(f"total errors found in estate.log file:{error_count}")

