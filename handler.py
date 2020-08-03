import json
from twilio.rest import Client


def lambda_handler(event, context):
    account_sid = os.environ.get("twilio_sid")
    auth_token = os.environ.get("twilio_auth_token")

    client = Client(account_sid, auth_token)

    client.api.account.messages.create(
    to="+7036280597",
    from_="+15555555555",
    body="Hello there!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

