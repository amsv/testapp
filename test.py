import requests
import import_config

api_link = "https://api.telegram.org/bot"+ import_config.token


updates = requests.get(api_link + "/getUpdates?offset=-1").json()

print(updates)

message = updates["result"][0]["message"]

chat_id = message["from"]["id"]
text =  message["text"]

sent_message  = requests.get(api_link + f"/sendMessage?chat_id={chat_id}&text=Привет ты написал {text}") 