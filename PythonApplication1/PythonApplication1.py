import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

type(res)
if res.status_code == 200 :
    print(res.text[:250])