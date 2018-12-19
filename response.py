def base_request_response(body, statusCode):
    return {
        'statusCode': statusCode,
        'body': body,
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