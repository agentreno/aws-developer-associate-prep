# https://docs.aws.amazon.com/cli/latest/userguide/cli-roles.html
# If you've set up your credentials and config files like so you don't need to
# assume roles explicitly and parse out temp creds anymore:
#
# ~/.aws/credentials:
# [sts-prototype]
# <some creds>
#
# ~/.aws/config:
# [profile sts-prototype-role]
# role_arn=arn:aws:iam::433473615199:role/sts-prototype-role
# source_profile=sts-prototype 
#
aws --profile sts-prototype-role \
  s3 cp test.txt s3://sts-prototype-bucket
