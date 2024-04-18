import requests

response = requests.get('http://api.open-notify.org/astros.json', verify=False)
json = response.json()

print(json)

