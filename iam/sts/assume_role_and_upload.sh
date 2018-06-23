# Get temporary creds by assuming the role
CRED_OBJ=$(aws --profile sts-prototype \
  sts assume-role \
  --role-arn arn:aws:iam::433473615199:role/sts-prototype-role \
  --role-session-name my_session \
)

TEMP_ACCESS_KEY=$(echo $CRED_OBJ | jq -r '.Credentials.AccessKeyId')
TEMP_SECRET_KEY=$(echo $CRED_OBJ | jq -r '.Credentials.SecretAccessKey')
SESSION_TOKEN=$(echo $CRED_OBJ | jq -r '.Credentials.SessionToken')

# Use the temp creds to copy a file to the S3 bucket
AWS_ACCESS_KEY_ID=$TEMP_ACCESS_KEY \
AWS_SECRET_ACCESS_KEY=$TEMP_SECRET_KEY \
AWS_SESSION_TOKEN=$SESSION_TOKEN \
aws s3 cp test.txt s3://sts-prototype-bucket
