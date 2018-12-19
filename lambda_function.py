from __future__ import print_function
import boto3
import json
import uuid
from dynamodb import *
from response import *
from validation import *

def lambda_handler(event, context):
    jsonConfig = event['body-json']
    
    if validate(jsonConfig) == 1:
        if 'socialmedia' in jsonConfig:
            return createInfluencerDynamoItem(jsonConfig)
        else:
            return createBrandDynamoItem(jsonConfig)
    else:
        return base_request_response('Invalid Schema', 400)