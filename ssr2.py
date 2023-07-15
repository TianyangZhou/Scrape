import requests

url = 'https://ssr2.scrape.center'
headers ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers,verify=False)
print(resp)