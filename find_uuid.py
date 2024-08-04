import requests
import json

with open("tokens.json","r") as fp:
    tokens = json.load(fp)


friend_url = "https://kapi.kakao.com/v1/api/talk/friends"

#GET /v1/api/talk/friends HTTP/1.1
 #Host: kapi.kakao.com
#Authorization: Bearer {ACCESS_TOKEN}

headers={"Authorization" : "Bearer " + tokens["access_token"]}

result = json.loads(requests.get(friend_url, headers=headers).text)

print(type(result))
print("=============================================")
print(result)
print("=============================================")
friends_list = result.get("elements")
print(friends_list)
print(type(friends_list))
print("=============================================")
print(friends_list[0].get("uuid"))
friend_id = friends_list[0].get("uuid")
print(friend_id)