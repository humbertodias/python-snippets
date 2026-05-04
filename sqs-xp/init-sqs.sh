#!/bin/bash

echo "Creating SQS queues..."

# Create DLQ first
awslocal sqs create-queue --queue-name xp-dlq

# Create main queue with DLQ (Redrive policy)
awslocal sqs create-queue \
  --queue-name xp-queue \
  --attributes '{
    "RedrivePolicy": "{\"maxReceiveCount\":\"3\",\"deadLetterTargetArn\":\"arn:aws:sqs:us-east-1:000000000000:xp-dlq\"}"
  }'

echo "Queues created successfully!"