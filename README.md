[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/humbertodias/python-snippets)

# Python Snippets

This repository contains a collection of Python examples and mini-projects demonstrating the use of Redis, AWS SQS (with LocalStack), CloudFormation, Terraform, Kubernetes, and various web frameworks.

## Projects

### 1. Redis (zadd)

* Example implementation of a leaderboard using Redis sorted sets.
* 📁 [redis/leaderboard](redis/leaderboard)

### 2. Redis (Pub/Sub)

* Basic Chat using Redis Pub/Sub to delivery message to clients.
* 📁 [redis/chat](redis/chat/README.md)

### 3. AWS SQS (Event Change XP)

* Demonstrates a simple event-driven system for chaging player XP using AWS SQS.
* 📁 [sqs/xp](sqs/xp/README.md)

### 4. AWS SQS (Daily Reward)

* Demonstrates a simple event-driven system for daily reward using AWS SQS.
* 📁 [sqs/daily_reward](sqs/daily_reward/README.md)

### 5. Infrastructure as Code (CloudFormation)

* AWS infrastructure examples using CloudFormation.
* 📁 [infra/cf](infra/cf/README.md)

### 6. Infrastructure as Code (Terraform)

* Infrastructure provisioning examples using Terraform.
* 📁 [infra/tf](infra/tf/README.md)

### 7. Kubernetes

* Basic Kubernetes manifests and deployments.
* 📁 [infra/k8s](infra/k8s/README.md)

### 8. Web Frameworks

* Simple applications using different Python web frameworks:

  * 📁 [web/fastapi](web/fastapi/README.md)
  * 📁 [web/flask](web/flask/README.md)
  * 📁 [web/tornado](web/tornado/README.md)
  
## Notes

* Some examples may use LocalStack to simulate AWS services locally.
* Each project contains its own README with setup instructions and details.
