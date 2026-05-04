#!/bin/bash

echo "Creating SQS queues..."

# Create DLQ first
awslocal sqs create-queue --queue-name daily-reward-dlq

# Create main queue with DLQ (Redrive policy)
awslocal sqs create-queue \
  --queue-name daily-reward \
  --attributes '{
    "RedrivePolicy": "{\"maxReceiveCount\":\"3\",\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:000000000000:daily-reward-dlq\"}"
  }'

echo "Queues created successfully!"