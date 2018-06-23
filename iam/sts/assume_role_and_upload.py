import boto3

# First, the hard way, getting the temp creds directly from STS
print('FIRST METHOD')
session = boto3.Session(profile_name='sts-prototype')
client = session.client('sts')
temp_creds = client.assume_role(
    RoleArn='arn:aws:iam::433473615199:role/sts-prototype-role',
    RoleSessionName='my_session'
)
temp_session = boto3.Session(
    aws_access_key_id=temp_creds['Credentials']['AccessKeyId'],
    aws_secret_access_key=temp_creds['Credentials']['SecretAccessKey'],
    aws_session_token=temp_creds['Credentials']['SessionToken']
)
client = temp_session.client('s3')
with open('test.txt') as test_file:
    response = client.put_object(
        Body=test_file,
        Bucket='sts-prototype-bucket',
        Key='test.txt'
    )
print(response)

# Next, the much easier way with boto3's AssumeRole provider
# Bit like awscli, if ~/.aws/config has a profile entry, boto3 will do the
# AssumeRole calls under the hood
print('SECOND METHOD')
session = boto3.Session(profile_name='sts-prototype-role')
client = session.client('s3')
with open('test.txt') as test_file:
    response = client.put_object(
        Body=test_file,
        Bucket='sts-prototype-bucket',
        Key='test.txt'
    )
print(response)
