import json
import base64

import boto3
from Crypto.Cipher import AES

session = boto3.Session(profile_name='sqs-kms-prototype')
sqs_client = session.client('sqs')
kms_client = session.client('kms')

# Encrypt a message using KMS
data_key = kms_client.generate_data_key(
    KeyId='alias/sqs-kms-prototype/main',
    KeySpec='AES_256'
)
encryption_suite = AES.new(data_key['Plaintext'], AES.MODE_CBC, 'thisismyiv123456')
cipher_text = encryption_suite.encrypt('secretmessage123')
message = {
    'key': base64.b64encode(data_key['CiphertextBlob']),
    'message': base64.b64encode(cipher_text)
}
print('Encrypted message')
print(message)

# Send to SQS
print('Sent message')
queue = sqs_client.get_queue_url(QueueName='sqs-kms-prototype-queue')['QueueUrl']
response = sqs_client.send_message(
    QueueUrl=queue,
    MessageBody=json.dumps(message)
)

# Read it back
# Technically this is long polling as WaitTimeSeconds is supplied
messages = sqs_client.receive_message(
    QueueUrl=queue,
    WaitTimeSeconds=1
)
print('Retrieved messages')
print(messages)

# Decrypt as if from scratch
message = json.loads(messages['Messages'][0]['Body'])
ciphertext_data_key = base64.b64decode(message['key'])
ciphertext_message = base64.b64decode(message['message'])
plaintext_data_key = kms_client.decrypt(
    CiphertextBlob=ciphertext_data_key
)['Plaintext']
decryption_suite = AES.new(plaintext_data_key, AES.MODE_CBC, 'thisismyiv123456')
plaintext_message = decryption_suite.decrypt(ciphertext_message)
print('Decrypted message')
print(plaintext_message)
