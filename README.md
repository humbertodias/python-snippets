[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/humbertodias/python-snippets)

# Python Snippets

A collection of small Python projects showing how to use Redis, AWS SQS (with LocalStack), Infrastructure as Code, Kubernetes, web frameworks, etc.

## Projects

### Redis

* [Leaderboard (zadd)](redis/leaderboard/README.md) → simple ranking system using sorted sets

* [Chat (Pub/Sub)](redis/chat/README.md) → real-time messaging using Redis Pub/Sub

### AWS SQS

* [XP system](sqs/xp/README.md) → event-driven player XP updates

* [Daily reward](sqs/daily_reward/README.md) → event-based daily rewards
  
### Infrastructure as Code

* [CloudFormation](infra/cf/README.md) → AWS infrastructure examples

* [Terraform](infra/tf/README.md) → infrastructure provisioning examples

### Kubernetes

* [k8s](infra/k8s/README.md) → Basic deployments and manifests

### Web Frameworks

Simple apps using:

* [FastAPI](web/fastapi/README.md)
* [Flask](web/flask/README.md)
* [Tornado](web/tornado/README.md)

## Notes

* Some projects use LocalStack to simulate AWS locally.
* Each folder has its own README with setup instructions.
