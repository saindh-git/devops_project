import requests
import json

url ="https://jsonplaceholder.typicode.com/todos/1"
print(f"--- Consultant: Sending Courier to {url} ---")

response=requests.get(url)

if response.status_code == 200:
    print("Courier Returned Successfully!")
    
    data=response.json()
    print(f"Data Received: {data['title']}")
else:
    print(f"Courier Failed. Status Code: {response.status_code}")


