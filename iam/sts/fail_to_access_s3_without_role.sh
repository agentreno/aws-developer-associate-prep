# This is expected to fail, this user needs to assume a role to do this
# operation
aws --profile sts-prototype \
  s3 cp test.txt s3://sts-prototype-bucket
