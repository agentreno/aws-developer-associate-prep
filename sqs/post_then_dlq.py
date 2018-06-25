from time import sleep

import boto3

session = boto3.Session(profile_name='sqs-kms-prototype')
client = session.client('sqs')

# Post message to queue
print('Sent message')
queue = client.get_queue_url(QueueName='sqs-kms-prototype-queue')['QueueUrl']
response = client.send_message(
    QueueUrl=queue,
    MessageBody='hello world',
)

# Read it back
# Technically this is long polling as WaitTimeSeconds is supplied
first_messages = client.receive_message(
    QueueUrl=queue,
    WaitTimeSeconds=1
)
print('First retrieval - after sent')
print(first_messages)


# Read it again to show there's nothing there
sleep(15)
second_messages = client.receive_message(
    QueueUrl=queue,
    WaitTimeSeconds=1
)
print('Second retrieval - after visibility timeout, message is gone to DLQ')
print(second_messages)

# Read from the DLQ
queue = client.get_queue_url(QueueName='sqs-kms-prototype-dlq')['QueueUrl']
messages = client.receive_message(
    QueueUrl=queue,
    WaitTimeSeconds=1
)
print('DLQ messages')
print(messages)

client.delete_message(
    QueueUrl=queue,
    ReceiptHandle=messages['Messages'][0]['ReceiptHandle']
)
