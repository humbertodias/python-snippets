#!/bin/bash

set -e

echo "Criando recursos locais..."

# ----------------------------
# SQS - Criar fila
# ----------------------------
echo "Criando fila SQS..."

QUEUE_URL=$(awslocal sqs create-queue \
  --queue-name game-events \
  --query 'QueueUrl' \
  --output text)

echo "Queue URL: $QUEUE_URL"

# ----------------------------
# SQS FIFO (opcional)
# ----------------------------
echo "Criando fila FIFO..."

awslocal sqs create-queue \
  --queue-name game-events.fifo \
  --attributes FifoQueue=true,ContentBasedDeduplication=true

echo "FIFO criada"

# ----------------------------
# DynamoDB - Criar tabela Players
# ----------------------------
echo "Criando tabela Players..."

awslocal dynamodb create-table \
  --table-name Players \
  --attribute-definitions \
      AttributeName=player_id,AttributeType=S \
  --key-schema \
      AttributeName=player_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

echo "Tabela Players criada"

# ----------------------------
# DynamoDB - Criar tabela Events (idempotência)
# ----------------------------
echo "Criando tabela Events..."

awslocal dynamodb create-table \
  --table-name ProcessedEvents \
  --attribute-definitions \
      AttributeName=event_id,AttributeType=S \
  --key-schema \
      AttributeName=event_id,KeyType=HASH \
  --billing-mode PAY_PER_REQUEST

echo "Tabela ProcessedEvents criada"

# ----------------------------
# Esperar tabelas ficarem prontas
# ----------------------------
echo "Aguardando tabelas..."

awslocal dynamodb wait table-exists \
  --table-name Players

awslocal dynamodb wait table-exists \
  --table-name ProcessedEvents

echo "Tudo pronto!"