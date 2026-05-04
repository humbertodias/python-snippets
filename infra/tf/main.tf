terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# -------------------------
# Provider pointing to LocalStack
# -------------------------
provider "aws" {
  region     = var.aws_region
  access_key = "test"
  secret_key = "test"

  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    sqs = "http://localhost:4566"
  }
}

# -------------------------
# Dead Letter Queue (DLQ)
# -------------------------
resource "aws_sqs_queue" "xp_dlq" {
  name = "xp-dlq"
}

# -------------------------
# Main queue
# -------------------------
resource "aws_sqs_queue" "xp_queue" {
  name = "xp-queue"
}

# -------------------------
# Redrive policy (DLQ link)
# -------------------------
resource "aws_sqs_queue_redrive_policy" "xp_redrive" {
  queue_url = aws_sqs_queue.xp_queue.id

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.xp_dlq.arn
    maxReceiveCount     = 3
  })
}