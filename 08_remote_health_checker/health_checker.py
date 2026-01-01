import requests

def check_site_health(url):
    try:

        response = requests.get(url, timeout=5)
        print(response)
        return {
            "site" : url,
            "status_code": response.status_code,
            "is_up" : response.status_code == 200

         }
    except Exception as e:
        return {"site":url,"status_code":"ERROR","is_up": False}

site_to_check = [
    "https://google.com",
    "https://github.com",
    "https://this-site-does-not-exist-123.com"
]

print("---remote health audit----")
for site in site_to_ckeck:
    report = check_site_health(site)
    status = "online" if report["is_up"] else "OFFLINE"
    print(f"Website: {report['site']} | Status: {status} ({report['status_code']})")

