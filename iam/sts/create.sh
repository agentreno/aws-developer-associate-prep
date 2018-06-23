aws cloudformation create-stack \
  --stack-name sts-prototype \
  --template-body file://sts.yml \
  --capabilities CAPABILITY_NAMED_IAM
