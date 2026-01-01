import json
report_file = "server_report.json"
try:
    with open(report_file,"r") as file:
        raw_data=file.read()
        data = json.loads(raw_data)
    name = data["hostname"]
    is_healthy = data["health_check"]
    print(f"--- Analyzing Report for {name} ---")
    if is_healthy:
        print(f"STATUS: SUCCESS. No action needed for {name}.")
    else:
        print(f"STATUS: WARNING! {name} requires immediate attention.")
except json.JSONDecodeError:
    print("ERROR: The report file is corrupted (Broken JSON)!")
except FileNotFoundError:
    print(f"ERROR: Could not find {report_file} in the estate.")
