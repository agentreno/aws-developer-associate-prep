aws cloudformation create-stack \
  --stack-name aurora-prototype \
  --template-body file://aurora-stack.yml \
  --parameters file://secret.json \
  --capabilities CAPABILITY_IAM
