from secrets import GITHUB_TOKEN
from pprint import pprint
import requests
print('Piyush Verma')

API_URL = "https://api.github.com"
payload = '{"name":"piyush1"}'
headers = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3.json"
}

github = requests.post(API_URL+"/user/repos", data=payload, headers=headers)

pprint(github.json())
pprint(github)
