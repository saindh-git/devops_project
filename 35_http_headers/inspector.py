import requests

url = "https://httpbin.org/get"
resp = requests.get(url)
print("--- SERVER HEADERS ---")
for key, value in resp.headers.items():
    print(f"{key}:{value}")
print("\n--- OUR REQUEST HEADERS ---")
for key, value in resp.request.headers.items():
    print(f"{key}: {value}")
