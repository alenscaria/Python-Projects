import requests
r=requests.get('http://api.open-notify.org/astros.json')
r.status_code
r.headers['content-type']
r.encoding
r.text
print(r.json())
