import requests
import base64

username = 'admin'
password = 'admin'

user_info_str = username + ':' + password
user_info = base64.b64encode(user_info_str.encode())
url = 'https://ssr3.scrape.center'
headers ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Authorization': "Basic " + user_info.decode()
}

resp = requests.get(url, headers=headers)
