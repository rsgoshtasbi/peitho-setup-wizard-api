API overview
============

<!-- ## Contents

- [Methods](#methods)
  - [Brand Registration](#accounts)
  - [Influencer Registration](#apps)
___ -->

## Methods

### Endpoints: 
    https://qhoovbdv91.execute-api.us-west-2.amazonaws.com/default/registration-auth-api/v1/brand
    https://qhoovbdv91.execute-api.us-west-2.amazonaws.com/default/registration-auth-api/v1/influencer

### Brand Endpoint
    POST https://qhoovbdv91.execute-api.us-west-2.amazonaws.com/default/registration-auth-api/v1/brand

###### Headers to set
    1. Content-Type = application/json
##### Brand JSON Request Body
```
{
    "brand_name": "john.doe",
    "email": "john.doe@test.com",
    "password": "john.doe",
    "phone": "1231231234"
    "bu" : "instagram",
}
```
| Attribute                | Description                                                                        | Nullable |
| ------------------------ | ---------------------------------------------------------------------------------- | -------- |
| `brand_name`             | The name of the account                                                            | no       |
| `email`                  | The email of the account                                                           | no       |
| `password`               | Password of account                                                                | no       |
| `phone_number`           | Brand contact number                                                               | no       |
| `bu`                     | Business Unit (IG, YouTube, etc)                                                   | no       |

##### Brand JSON Response Body
```
{
  "body": {
    "email": "john.doe@test.com",
    "status_code": "200",
    "uuid": "7cbf94dc-95d1-40ba-a57f-a2226f10a841",
    "brand_name": "john.doe"
    "bu" : "instagram",
  },
  "headers": {
    "Content-Type": "application/json"
  },
  "statusCode": "200"
}
```
| Attribute                | Description                                                                        | Nullable |
| ------------------------ | ---------------------------------------------------------------------------------- | -------- |
| `uuid`                   | UUID of account                                                                    | yes      |
| `brand_name`             | The name of the account                                                            | no       |
| `email`                  | The email of the account                                                           | no       |
| `status_code`            | status code of request                                                             | no       |
| `bu`                     | Business Unit (IG, YouTube, etc)                                                   | no       |

### Influencer Endpoint
    POST https://qhoovbdv91.execute-api.us-west-2.amazonaws.com/default/registration-auth-api/v1/influencer

##### Influencer JSON Request Body
```
{
    "first_name" : "john",
    "last_name" : "doe",
    "bu" : "instagram",
    "email" : "john.doe@test.com",
    "password" : "john.doe",
    "phone" : "1231231234"
}
```
| Attribute                | Description                                                                        | Nullable |
| ------------------------ | ---------------------------------------------------------------------------------- | -------- |
| `first_name`             | The first name of the influencer                                                   | no       |
| `last_name`              | The last name of the influencer                                                    | no       |
| `email`                  | The email of the account                                                           | no       |
| `password`               | Password of account                                                                | no       |
| `phone_number`           | Brand contact number                                                               | no       |
| `bu`                     | Business Unit (IG, YouTube, etc)                                                   | no       |


##### Influencer JSON Response Body
```
{
  "body": {
    "email": "john.doe@test.com",
    "status_code": "200",
    "uuid": "7cbf94dc-95d1-40ba-a57f-a2226f10a841",
    "first_name": "john"
    "last_name": "doe"
    "bu" : "instagram",
  },
  "headers": {
    "Content-Type": "application/json"
  },
  "statusCode": "200"
}
```
| Attribute                | Description                                                                        | Nullable |
| ------------------------ | ---------------------------------------------------------------------------------- | -------- |
| `uuid`                   | UUID of account                                                                    | yes      |
| `first_name`             | The first name of the influencer                                                   | no       |
| `last_name`              | The last name of the influencer                                                    | no       |
| `email`                  | The email of the account                                                           | no       |
| `status_code `           | status code of request                                                             | no       |
| `bu`                     | Business Unit (IG, YouTube, etc)                                                   | no       |



### Notes
```
{
    "body-json": {},
    "params": {
      "path": {},
      "querystring": {},
      "header": {}
    },
    "stage-variables": {},
    "context": {
      "cognito-authentication-type": "",
      "http-method": "POST",
      "account-id": "647591104505",
      "resource-path": "/registration-auth-api/v1/brand",
      "authorizer-principal-id": "",
      "user-arn": "arn:aws:iam::647591104505:root",
      "request-id": "96c009f3-ec95-11e8-b448-c79a683c0ccf",
      "source-ip": "test-invoke-source-ip",
      "caller": "647591104505",
      "api-key": "test-invoke-api-key",
      "user-agent": "aws-internal/3 aws-sdk-java/1.11.447 Linux/4.9.124-0.1.ac.198.71.329.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.192-b12 java/1.8.0_192",
      "user": "647591104505",
      "cognito-identity-pool-id": "",
      "api-id": "qhoovbdv91",
      "resource-id": "6699eq",
      "stage": "test-invoke-stage",
      "cognito-identity-id": "",
      "cognito-authentication-provider": ""
    }
}
```