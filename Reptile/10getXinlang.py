import requests


url = "https://jable.tv/b7a474bc-4ea0-4540-8993-663019f38907"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.7 Safari/537.36",
    "cookie": "__cfduid=d3b398dd8b273547ad19dfa3a274932921588497545; kt_referer=https%3A%2F%2Ftheporndude.com%2F; kt_tcookie=1; kt_is_visited=1; _ga=GA1.2.97232125.1588497544; _gid=GA1.2.1028853451.1588497544; PHPSESSID=nju6q097qjh750i2ma17cfsra7; kt_qparams=dir%3Dssni-631; kt_ips=47.91.137.13%2C47.52.157.36; __cf_bm=ea758cc0d5e495f5e50dbbc5b515f434eb4fc096-1588573297-1800-AfLbQVMflI1jB2wJ3c9lhFXWNUX2yrE72VCdUQg0aMbP2q1iE2cVIt/c1jyXQ6WSn1myir0ukLVeCC9q0Eu4NZXKs2dbIB2R8MuAzasdCuV2"
}

response = requests.post(url, headers=headers)
print(response)