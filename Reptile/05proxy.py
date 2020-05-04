import requests

proxies = {
    "http":"http://59.44.78.30"
}

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}

response = requests.get("https://www.google.com", proxies=proxies, headers=headers)
print(response.status_code)