import subprocess
print("---python os commander")
result = subprocess.run(["uptime"],capture_output=True,text=True)
if result.returncode == 0:
    print("success! the result")
    print(result.stdout)
else:
    print("result unsucess")

