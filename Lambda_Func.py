import json


def lambda_handler(event, context):
    print('event:', json.dumps(event))
    print('queryStringParameters:', json.dumps(event['queryStringParameters']))

    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmounts = event['queryStringParameters']['amount']

    print("TransactionId=" + transactionId)
    print("TransactionType=" + transactionType)
    print("TransactionAmount=" + transactionAmounts)

    TransactionResponse = {}
    TransactionResponse['TransactionId'] = transactionId
    TransactionResponse['TransactionType'] = transactionType
    TransactionResponse['TransactionAmount'] = transactionAmounts
    TransactionResponse['message'] = "Hello from lambda land"

    responeObject = {}
    responeObject['statusCode'] = 200
    responeObject['headers'] = {}
    responeObject['headers']['Content-Type'] = 'application/json'
    responeObject['body'] = json.dumps(TransactionResponse)

    return responeObject
