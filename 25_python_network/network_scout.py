import subprocess

target = "www.google.com"

result=subprocess.run(["ping","-c","1",target],capture_output=True,text+True)

if result.returncode == 0:
    print(f"SUCCESS: The Scout reached {target}")
else:
    print(f"FAILURE: {target_address} is unreachable or silent.")
