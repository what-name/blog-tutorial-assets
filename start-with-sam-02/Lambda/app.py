import json
import boto3
import os

# Initialize dynamodb boto3 object
dynamodb = boto3.resource('dynamodb')
# Set dynamodb table name variable from env
ddbTableName = os.environ['databaseName']
table = dynamodb.Table(ddbTableName)

def lambda_handler(event, context):
    # Update item in table or add if doesn't exist
    ddbResponse = table.update_item(
        Key={
            'id': 'HelloThere'
        },
        UpdateExpression='SET generalle = :value',
        ExpressionAttributeValues={
            ':value': 'Hello there, general Kenobi.'
        },
        ReturnValues="UPDATED_NEW"
    )

    # Format dynamodb response into variable
    responseBody = json.dumps({"HelloThere": ddbResponse["Attributes"]["generalle"]})

    # Create api response object
    apiResponse = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": responseBody
    }

    # Return api response object
    return apiResponse