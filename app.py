import requests
import json


Json_Body = {
    "NoOfConsumer": 10,
    "MessageType": "inv-inv-ViewItemCacheRebuild",
    "MinNoOfConsumer": 1,
    "MaxDesiredInstances": 6
}
json_string = json.dumps(Json_Body)
print(json_string)
print("Logged in successfully ->> Test1!")
print("Hello from GitHub! Sunil")
