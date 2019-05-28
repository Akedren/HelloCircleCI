from hellocircle import HelloWorld
import json
import requests

def hello_world(event, context):
    world = HelloWorld()

    response = {
        "statusCode": 200,
        "body": json.dumps(world.say_hello(event))
    }

    return response