import requests
import json
from openai import OpenAI

class Send_kakao:
    def __init__(self):
        with open("tokens.json","r") as kakao:
            self.token = json.load(kakao)
        self.url = "https://kapi.kakao.com/v1/api/talk/friends"
        self.headers={
            "Authorization" : "Bearer " + self.token["access_token"]
        }
        result = json.loads(requests.get(self.url, headers=self.headers).text)
        friends_list = result.get("elements")
        self.friend_id = friends_list[0].get("uuid")
    
    def message_data(self, name, file_address, content):
        self.url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
        with open("my_api_key", "r") as mak:
                api_key = mak.read().strip("\n").strip().strip('"').strip("'")
        client = OpenAI(
                api_key = api_key
            )
        completion = client.chat.completions.create(
                        model="gpt-4o",
                        messages = [{"role":"user", "content":f"{content}를 40글자 이하로 요약해줘"}]
                )
        data={
            'receiver_uuids': '["{}"]'.format(self.friend_id),
            "template_object": json.dumps({
                "object_type":"feed",
                "content": {
                            "title": f"{name}님의 타로 결과가 도착했어요~~!!",
                            "description": completion.choices[0].message.content,
                            "image_url": 'https://drive.google.com/uc?export=view&id=16nKph6nQMYtVs1BGy-FRv8qs6IMxEByK',
                            "image_width": 379,
                            "image_height": 547,
                            "link": {
                                "web_url": f"{file_address}",
                                "mobile_web_url": f"{file_address}",
                                "android_execution_params": "contentId=100",
                                "ios_execution_params": "contentId=100"
                            }
                        },
                        "item_content" : {
                            "profile_text" :"AI조",
                            "profile_image_url" :"https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMzEyMDlfMTk2%2FMDAxNzAyMDk2MzA4ODUz.8cl3cHBm7z8js4yLoJJ5yVDqMl4gtfuuCrY_r-G9yxEg.JnEUDgYwYyWIaoa3OM4VjDo2fkdZqvFaX_WOchXoKMkg.PNG.bon8361%2Fimage.png&type=a340",
                            "items" : [
                                {
                                    "item" :"타로카드1"
                                },
                                {
                                    "item" :"타로카드2"
                                },
                                {
                                    "item" :"타로카드3"
                                }
                            ]
                        },
                        "buttons": [
                            {
                                "title": "결과 다운로드 받기",
                                "link": {
                                    "web_url": f"{file_address}",
                                    "mobile_web_url": f"{file_address}"
                                }
                            }
                        ]
            })
        }
   
        response = requests.post(self.url, headers=self.headers, data=data)
        response.status_code