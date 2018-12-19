import boto3
from response import *

dynamo = boto3.client('dynamodb', region_name='us-west-2')

def createBrandDynamoItem(jsonData):
    if jsonData['address_line_2'] == "":
        jsonData['address_line_2'] = "None"
    user_table_response = dynamo.put_item(
        TableName='BRAND_INFO',
        Item={
            "UUID":{
                "S":jsonData['uuid']
            },
            "address_line_1":{
                "S":jsonData['address_line_1']
            },
            "address_line_2":{
                "S":jsonData['address_line_2']
            },
            "city":{
                "S":jsonData['city']
            },
            "state":{
                "S":jsonData['state']
            },
            "zipcode":{
                "S":jsonData['zipcode']
            },
            "about_me_description":{
                "S":jsonData['about_me_description']
            },
            "categories":{
                "SS":jsonData['categories']
            }
        }
    )
    print("pushed brand info to dynamo")
    return respond("pushed brand info to dynamo")
    
def createInfluencerDynamoItem(jsonData):
    if jsonData['address_line_2'] == "":
        jsonData['address_line_2'] = "None"
    user_table_response = dynamo.put_item(
        TableName='INFLUENCER_INFO',
        Item={
            "UUID":{
                "S":jsonData['uuid']
            },
            "address_line_1":{
                "S":jsonData['address_line_1']
            },
            "address_line_2":{
                "S":jsonData['address_line_2']
            },
            "city":{
                "S":jsonData['city']
            },
            "state":{
                "S":jsonData['state']
            },
            "zipcode":{
                "S":jsonData['zipcode']
            },
            "about_me_description":{
                "S":jsonData['about_me_description']
            },
            "categories":{
                "SS":jsonData['categories']
            },
            "socialmedia":{
                "SS":jsonData['socialmedia']
            },
            "gender":{
                "S":jsonData['gender']
            }
        }
    )
    print("pushed influencer info to dynamo")
    return respond("pushed influencer info to dynamo")