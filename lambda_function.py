from __future__ import print_function
import boto3
import json
import uuid

print('Loading function')
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
    
def base_request_response(msg, code):
    return {
        'statusCode': '400',
        'body': msg,
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def respond(err, res=None):
    return {
        'statusCode': '200' if err else '400',
        'body': err,
        'headers': {
            'Content-Type': 'application/json',
        },
    }

def lambda_handler(event, context):
    
    jsonConfig = event['body-json']
    if 'socialmedia' in jsonConfig:
        createInfluencerDynamoItem(jsonConfig)
    else:
        createBrandDynamoItem(jsonConfig)

    return respond(jsonConfig)