import requests
import os
import json
import subprocess
from datetime import datetime

def task_logger(func):
    def wrapper(*args, **kwargs):
        print(f"starting the task {func.__name__.upper()}___")
        result = func(*args, **kwargs)
        print(f"--- FINISHED TASK: {func.__name__.upper()} ---\n")
        return result
    return wrapper

@task_logger
def check_gate():
    res = subprocess.run(["ping","-c","1","8.8.8.8"],capture_output=True,text=True)
    return "GATE OPEN" if res.returncode == 0 else "GATE CLOSEED"


@task_logger
def audit_files():
    return os.listdir('.')
@task_logger
def fetch_status():
    try:

        resp = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        return resp['title'] if resp.status_code == 200 else "API ERROR"
    except:
        return "CONNECTION FAILED"
report = {
    "timestamp": str(datetime.now()),
    "network": check_gate(),
    "vault": audit_files(),
    "market": fetch_status()
}
with open("daily_report.json","w") as f:
    json.dump(report,f,indent=4)

print("MASTER REPORT GENERATED: daily_report.json")
