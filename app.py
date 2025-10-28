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
  },
  "OrderLine": [
        {
            "OrderLineId": "1",
            "IsOnHold": false,
            "ServiceLevelCode": "UPS Express",
            "CarrierCode": "UPS",
            "ShippingMethodId": null,
            "IsCancelled": false,
            "ItemId": "Laptop1",
            "UnitPrice": "5",
            "Quantity": "1",
            "IsReturnable": true,
            "UOM": "EA",
            "ShipToLocationId": null,
            "RequestedDeliveryDate": "2023-05-15T10:42:22.664",
            "OrderLinePromisingInfo": {
                "LastPossibleDeliveryDate": null,
                "IsDeliveryByRequestedDate": false,
                "ExternalRouteId": "ecomorg:T0981"
            },
            "OrderLineNote": [
                {
                    "NoteType": "Gift From",
                    "NoteCode": "INS",
                    "NoteText": "Instruction - Line",
                    "NoteId": "2",
                    "NoteCategory": "Instruction"
                }
            ],
            "DeliveryMethod": {
                "DeliveryMethodId": "ShipToAddress"
            },
            "ShipToAddress": {
                "AddressTypeId": "Shipping",
                "IsAddressVerified": true,
                "Address": {
                    "Address1": "14131 Midway Road",
                    "Address2": "",
                    "City": "Addison",
                    "Country": "US",
                    "Email": "jSmith@manh.com",
                    "FirstName": "John",
                    "LastName": "Smith",
                    "Phone": "423-306-1973",
                    "PostalCode": "30039",
                    "State": "TX"
                }
            }
        }
    ]
}'''
Json_Body = json.loads(Json_String)
print("Consumer Count -> ",Json_Body.get("NoOfConsumer"))
print("OrderLine Promising Info -> ", Json_Body["OrderLinePromisingInfo"]["ExternalRouteId"])
print("Logged in successfully ->> Test1!")
print("Hello from GitHub! Sunil")
