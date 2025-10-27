import requests
import json


Json_Body = {
    "NoOfConsumer": 10,
    "MessageType": "inv-inv-ViewItemCacheRebuild",
    "MinNoOfConsumer": 1,
    "MaxDesiredInstances": 6,
    "OrderLinePromisingInfo": 
        {
            "LastPossibleDeliveryDate": null,
            "IsDeliveryByRequestedDate": false,
            "ExternalRouteId": "ecomorg:T0981"
        }
}
json_string = json.dumps(Json_Body)
response = json.loads(json_string)
print("Consumer Count -> ",response.get("NoOfConsumer"))
print("OrderLine Promising Info -> ",(response.get("OrderLinePromisingInfo")).get("ExternalRouteId"))
print("Logged in successfully ->> Test1!")
print("Hello from GitHub! Sunil")
