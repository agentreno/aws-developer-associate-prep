# aws-developer-associate-prep

## Description

Preparation for the AWS Developer Associate exam. For each of the services
likely to come up on the exam, do each of AWS CLI / Python SDK / AWS API access
to get familiar with API calls, command lines and Boto usage.

## TODO

- CloudFormation
    - Create all of the below using CloudFormation templates

- SQS and KMS
    - Create a new standard queue, post a message to it and immediately read
      it, allow visibility timeout to expire, read it again then remove it.
    - Send a batch of messages and retrieve it with long polling
    - Setup a DLQ
    - Encrypt a message with a KMS-stored master key, queue it, retrieve it and
      decrypt it again

- DynamoDB
    - Create a table and insert and read back some dummy data
    - Create global and local secondary indexes
    - Try a conditional operation for a counter (with some threads?)
    - Make a note of the API operations into flashcards from here:
      https://aws.amazon.com/dynamodb/faqs/

- IAM
    - Use the IAM AssumeRole call directly to get time-limited credentials for
      a particular role
    - Call STS GetSessionToken API for my IAM user
    - Create an Aurora/EC2/IAM role prototype showing how database credentials
      can be rotated and used automatically by the app instead of a password
    - Try out the policy simulator

- SNS
    - Create a topic, subscribe to it, send a mesage and verify receive
    - Send in two messages and use a filter policy to filter one out
