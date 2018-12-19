API overview
============

## Methods

### Endpoint: 
    https://aqj2plvnbi.execute-api.us-west-2.amazonaws.com/default/setup-wizard-api

###### Headers to set
    1. Content-Type = application/json


##### Brand JSON Request Body
```
{
    "uuid": "123-1234-123",
    "address_line_1": "68 Tallowood",
    "address_line_2": "",
    "city": "instagram",
    "state": "john.doe@test.com",
    "zipcode": "john.doe",
    "categories": [
      "food",
      "travel"
    ],
    "about_me_description": "I'm fucking awesome"
  }
```
Note: Only 'address_line_2' can be empty

##### Brand JSON Response Body
```
{
  "body": "Pushed to dynamo",
  "headers": {
    "Content-Type": "application/json"
  },
  "statusCode": "200"
}
```

##### Influencer JSON Request Body
```
{
    "uuid": "123-1234-123",
    "address_line_1": "68 Tallowood",
    "address_line_2": "",
    "city": "instagram",
    "state": "john.doe@test.com",
    "zipcode": "john.doe",
    "categories": [
      "food",
      "travel"
    ],
    "socialmedia": [
        "instagram",
        "youtube"
    ],
    "gender": "male",
    "about_me_description": "I'm fucking awesome"
  }
```
Note: Only 'address_line_2' can be empty

##### Influencer JSON Response Body
```
{
  "body": "Pushed to dyanmo",
  "headers": {
    "Content-Type": "application/json"
  },
  "statusCode": "200"
}
```
