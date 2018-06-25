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
second_messages = client.receive_message(
    QueueUrl=queue,
    WaitTimeSeconds=1
)
print('Second retrieval - within visibility timeout')
print(second_messages)

# Wait visibility timeout and read again, the message should be magically back
# on the queue
sleep(10)
third_messages = client.receive_message(
    QueueUrl=queue,
    WaitTimeSeconds=1
)
print('Third retrieval - after visibility timeout')
print(third_messages)

# Delete it this time and read again
client.delete_message(
    QueueUrl=queue,
    ReceiptHandle=third_messages['Messages'][0]['ReceiptHandle']
)
fourth_messages = client.receive_message(
    QueueUrl=queue,
    WaitTimeSeconds=1
)
print('Fourth retrieval - after deletion')
print(fourth_messages)
