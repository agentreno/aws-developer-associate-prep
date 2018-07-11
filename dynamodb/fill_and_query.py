import boto3

item = {
    'user_id': {
        'S': '123'
    },
    'email_address': {
        'S': 'karl@example.com'
    },
    'account_id': {
        'S': '456'
    }
}

client = boto3.client('dynamodb')

# First write an item
print('Written item')
client.put_item(
    TableName='dynamodb-prototype-users-by-email',
    Item=item,
    ReturnConsumedCapacity='TOTAL'
)

# Then query for it
data = client.query(
    TableName='dynamodb-prototype-users-by-email',
    ExpressionAttributeValues={
        ':email': {
            'S': 'karl@example.com'
        }
    },
    KeyConditionExpression='email_address = :email'
)
print('Queried item')
print(data)

# Then delete it
data = client.delete_item(
    TableName='dynamodb-prototype-users-by-email',
    Key={
        'email_address': {
            'S': 'karl@example.com'
        },
        'account_id': {
            'S': '456'
        }
    }
)
print('Deleted item')
print(data)
