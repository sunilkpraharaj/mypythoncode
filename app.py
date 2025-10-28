import requests
import json


Json_String = '''{
  "NoOfConsumer": 10,
  "MessageType": "inv-inv-ViewItemCacheRebuild",
  "MinNoOfConsumer": 1,
  "MaxDesiredInstances": 6,
  "OrderLinePromisingInfo": {
    "LastPossibleDeliveryDate": null,
    "IsDeliveryByRequestedDate": false,
    "ExternalRouteId": "ecomorg:T0981"
  }
}'''
Json_Body = json.loads(Json_String)
print("Consumer Count -> ",Json_Body.get("NoOfConsumer"))
print("OrderLine Promising Info -> ",Json_Body.get("OrderLinePromisingInfo")).get("ExternalRouteId")
print("Logged in successfully ->> Test1!")
print("Hello from GitHub! Sunil")
