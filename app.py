import requests
import json


Json_Body = {
    "NoOfConsumer": 10,
    "MessageType": "inv-inv-ViewItemCacheRebuild",
    "MinNoOfConsumer": 1,
    "MaxDesiredInstances": 6
}
json_object = json.loads(Json_Body)
print("Logged in successfully ->> Test1!")
print("Hello from GitHub! Sunil")
