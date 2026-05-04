#!/bin/bash

echo "Creating DynamoDB tables..."

awslocal dynamodb create-table \
  --table-name players \
  --attribute-definitions AttributeName=player_id,AttributeType=S \
  --key-schema AttributeName=player_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST 
  
echo "Tables created successfully!"

