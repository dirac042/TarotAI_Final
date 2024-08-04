import requests
import json

data = {
    'grant_type':'authorization_code',
    'client_id':'a8fd41d334e15d3d38ae81df28637cdb',
    'redirect_uri':'https://localhost.com',
    'code': '6OjTxA_aPFdl4wBY41XbBxl79r4zXrCQsmVYuae420l-6iQ3FHh4IQAAAAQKPCSZAAABkRXXry8icpf3YNJZ6g'
    }

response = requests.post('https://kauth.kakao.com/oauth/token', data=data)
tokens = response.json()

with open("tokens.json","w") as kakao:
    json.dump(tokens, kakao)