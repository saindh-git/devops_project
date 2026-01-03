print(f"---estate security system booting----")

target_file = "secret_code.txt"

try:
    with open("secret_code.txt","r") as file:
        data =file.read()
        print(data)
except FileNotFoundError:
    print(f"ALERT:the file '{target_file} is missing from the vault'")
    print(f"Action: Generating a temporary guest pass instead.")
except Exception as e:
    print(f"CRITICAL ERROR: Something went wrong: {e}")
finally:
   print("LOG: Security scan attempt complete. Shutting down scanner.")
