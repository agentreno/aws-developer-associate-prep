aws cloudformation create-stack \
  --stack-name dynamodb-prototype \
  --template-body file://dynamodb.yml \
  --capabilities CAPABILITY_NAMED_IAM
