import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

type(res)
res.status_code == requests.codes.ok
print(res.text[:250])