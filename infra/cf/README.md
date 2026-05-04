## CloudFormation

docker compose up -d

aws configure --profile localstack

AWS Access Key ID: test
AWS Secret Access Key: test
Default region: us-east-1


AWS_PROFILE=localstack aws --endpoint-url=http://localhost:4566 cloudformation deploy \
  --template-file template.yml \
  --stack-name xp-sqs-stack \
  --capabilities CAPABILITY_NAMED_IAM



Waiting for changeset to be created..
Waiting for stack create/update to complete
Successfully created/updated stack - xp-sqs-stack