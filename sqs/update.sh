aws cloudformation update-stack \
  --stack-name sqs-kms-prototype \
  --template-body file://sqs.yml \
  --capabilities CAPABILITY_NAMED_IAM
