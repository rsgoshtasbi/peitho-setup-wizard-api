import json
from response import *

def validate(jsonConfig):
    if 'socialmedia' in jsonConfig:
        return validate_influencer(jsonConfig)
    else:
        return validate_brand(jsonConfig)
        
def validate_brand(jsonConfig):
    if 'uuid' not in jsonConfig:
        return base_request_response("Required: uuid", 400)
    elif 'address_line_1' not in jsonConfig:
        return base_request_response("Required: address_line_1", 400)
    elif 'address_line_2' not in jsonConfig:
        return base_request_response("Required: address_line_2", 400)
    elif 'city' not in jsonConfig:
        return base_request_response("Required: city", 400)
    elif 'state' not in jsonConfig:
        return base_request_response("Required: state", 400)
    elif 'zipcode' not in jsonConfig:
        return base_request_response("Required: zipcode", 400)
    elif 'categories' not in jsonConfig:
        return base_request_response("Required: categories", 400)
    elif 'about_me_description' not in jsonConfig:
        return base_request_response("Required: about_me_description", 400)
    else:
        return 1
        
def validate_influencer(jsonConfig):
    if 'uuid' not in jsonConfig:
        return base_request_response("Required: uuid", 400)
    elif 'address_line_1' not in jsonConfig:
        return base_request_response("Required: address_line_1", 400)
    elif 'address_line_2' not in jsonConfig:
        return base_request_response("Required: address_line_2", 400)
    elif 'city' not in jsonConfig:
        return base_request_response("Required: city", 400)
    elif 'state' not in jsonConfig:
        return base_request_response("Required: state", 400)
    elif 'zipcode' not in jsonConfig:
        return base_request_response("Required: zipcode", 400)
    elif 'categories' not in jsonConfig:
        return base_request_response("Required: categories", 400)
    elif 'socialmedia' not in jsonConfig:
        return base_request_response("Required: socialmedia", 400)
    elif 'gender' not in jsonConfig:
        return base_request_response("Required: gender", 400)
    elif 'about_me_description' not in jsonConfig:
        return base_request_response("Required: about_me_description", 400)
    else:
        return 1